"""Orchestrator — task routing and multi-agent coordination hub.

Boots all 8 agents, owns the message bus, and routes work using
MiMo-V2.5-Pro for high-level decision making.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any

from src.agents.chain import ChainAgent
from src.agents.coder import CoderAgent
from src.agents.eligibility import EligibilityAgent
from src.agents.guardian import GuardianAgent
from src.agents.hunter import HunterAgent
from src.agents.reviewer import ReviewerAgent
from src.agents.scribe import ScribeAgent
from src.mimo_client import MiMoClient

log = logging.getLogger(__name__)


class Orchestrator:
    """Multi-agent orchestrator powered by MiMo-V2.5-Pro."""

    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config
        self.mimo = MiMoClient(
            api_base=config["mimo"]["api_url"],
        )
        self.agents: dict[str, Any] = {}
        self._tasks: list[asyncio.Task] = []

    async def start(self) -> None:
        log.info("Bootstrapping agent fleet (8 agents)...")
        agents_cfg = self.config.get("agents", {})

        if agents_cfg.get("hunter", {}).get("enabled", True):
            self.agents["hunter"] = HunterAgent(self.mimo, agents_cfg["hunter"])
        if agents_cfg.get("eligibility", {}).get("enabled", True):
            self.agents["eligibility"] = EligibilityAgent(self.mimo, agents_cfg["eligibility"])
        if agents_cfg.get("guardian", {}).get("enabled", True):
            self.agents["guardian"] = GuardianAgent(self.mimo, agents_cfg["guardian"])
        if agents_cfg.get("chain", {}).get("enabled", True):
            self.agents["chain"] = ChainAgent(self.mimo, agents_cfg["chain"])
        if agents_cfg.get("coder", {}).get("enabled", True):
            self.agents["coder"] = CoderAgent(self.mimo, agents_cfg["coder"])
        if agents_cfg.get("reviewer", {}).get("enabled", True):
            self.agents["reviewer"] = ReviewerAgent(self.mimo, agents_cfg["reviewer"])
        if agents_cfg.get("scribe", {}).get("enabled", True):
            self.agents["scribe"] = ScribeAgent(self.mimo, agents_cfg["scribe"])

        for name, agent in self.agents.items():
            await agent.start()
            log.info(f"  [green]✓[/green] {name} agent online")

    async def route(self, task: dict[str, Any]) -> dict[str, Any]:
        """Route a task to the appropriate agent using MiMo decision making."""
        kind = task.get("kind")
        agent = self.agents.get(kind)
        if not agent:
            raise ValueError(f"No agent registered for task kind: {kind}")
        return await agent.handle(task)

    async def run_forever(self) -> None:
        while True:
            await asyncio.sleep(60)

    async def shutdown(self) -> None:
        log.info("Shutting down agents...")
        for name, agent in self.agents.items():
            await agent.stop()
            log.info(f"  ✓ {name} stopped")
        await self.mimo.aclose()
