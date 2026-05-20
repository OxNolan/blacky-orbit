"""Base agent class — common lifecycle and MiMo interaction primitives."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any

from src.mimo_client import MiMoClient, MiMoResponse


class BaseAgent(ABC):
    """Abstract base class for all Blacky Orbit agents."""

    name: str = "base"
    model: str = "mimo-v2.5-pro"

    def __init__(self, mimo: MiMoClient, config: dict[str, Any]) -> None:
        self.mimo = mimo
        self.config = config
        self.log = logging.getLogger(f"agent.{self.name}")
        self.model = config.get("model", self.model)

    async def start(self) -> None:
        self.log.debug(f"{self.name} starting (model={self.model})")

    async def stop(self) -> None:
        self.log.debug(f"{self.name} stopping")

    async def reason(
        self,
        system: str,
        user: str,
        max_tokens: int = 4096,
    ) -> MiMoResponse:
        """Single-turn reasoning call to MiMo."""
        return await self.mimo.chat(
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            model=self.model,
            max_tokens=max_tokens,
        )

    @abstractmethod
    async def handle(self, task: dict[str, Any]) -> dict[str, Any]:
        """Handle a task dispatched by the orchestrator."""
        raise NotImplementedError
