"""Blacky Orbit entry point.

Boots the orchestrator and registers all 8 agents. Loads config from YAML
and starts the agent message bus.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import sys
from pathlib import Path

import yaml
from rich.console import Console
from rich.logging import RichHandler

from src.orchestrator import Orchestrator

console = Console()


def setup_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, rich_tracebacks=True)],
    )


def load_config(path: Path) -> dict:
    if not path.exists():
        console.print(f"[red]Config not found: {path}[/red]")
        sys.exit(1)
    return yaml.safe_load(path.read_text())


async def amain(config_path: Path) -> None:
    config = load_config(config_path)
    setup_logging(config.get("logging", {}).get("level", "INFO"))

    log = logging.getLogger("blacky-orbit")
    log.info("[bold cyan]Blacky Orbit booting...[/bold cyan]")
    log.info(f"Config loaded from: {config_path}")

    orchestrator = Orchestrator(config)
    await orchestrator.start()

    log.info("[green]All agents online. Entering main loop.[/green]")
    try:
        await orchestrator.run_forever()
    except KeyboardInterrupt:
        log.info("Shutdown requested.")
    finally:
        await orchestrator.shutdown()


def main() -> None:
    parser = argparse.ArgumentParser(prog="blacky-orbit")
    parser.add_argument(
        "--config", type=Path, default=Path("config/default.yaml"),
        help="Path to config YAML",
    )
    args = parser.parse_args()
    asyncio.run(amain(args.config))


if __name__ == "__main__":
    main()
