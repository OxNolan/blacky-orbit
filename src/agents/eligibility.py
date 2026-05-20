"""Eligibility Agent — per-wallet eligibility scoring across projects."""

from __future__ import annotations

from typing import Any

from src.agents.base import BaseAgent

SYSTEM_PROMPT = """You are the Eligibility Agent for Blacky Orbit.

Given a wallet address and a list of target projects, perform a deep
eligibility check across multiple chains. For each project:

1. Check on-chain interaction history relevant to the project
2. Estimate qualification likelihood (none / low / medium / high)
3. Identify missing actions to improve eligibility
4. Flag potential anti-sybil red flags

Output: structured JSON per project with verdict + recommended actions.
"""


class EligibilityAgent(BaseAgent):
    name = "eligibility"

    async def handle(self, task: dict[str, Any]) -> dict[str, Any]:
        wallet = task.get("wallet")
        projects = task.get("projects", [])
        chains = self.config.get("chains", [])
        result = await self.reason(
            system=SYSTEM_PROMPT,
            user=f"Wallet: {wallet}\nProjects: {projects}\nChains to scan: {chains}",
            max_tokens=12000,
        )
        return {
            "agent": self.name,
            "model": result.model,
            "tokens": result.total_tokens,
            "output": result.content,
        }
