"""Hunter Agent — Web3 opportunity discovery.

Continuously polls Galxe, Layer3, Zealy, DefiLlama, and X alpha feeds
for new airdrop / quest / testnet opportunities. Uses MiMo-V2.5-Pro
to score and filter signal from noise.
"""

from __future__ import annotations

from typing import Any

from src.agents.base import BaseAgent

SYSTEM_PROMPT = """You are the Hunter Agent for Blacky Orbit.

Your role: continuously scan Web3 opportunity sources (Galxe, Layer3,
Zealy, DefiLlama, X alpha feeds) and surface high-signal opportunities.

For each opportunity, evaluate:
1. Reward expectancy (token allocation likelihood)
2. Effort required (time, capital, technical complexity)
3. Anti-sybil ruleset (one wallet vs multi-wallet feasibility)
4. Deadline urgency

Output structured JSON with: project_name, source, reward_expectancy,
effort_score (1-10), anti_sybil_strict (bool), deadline, action_required.
"""


class HunterAgent(BaseAgent):
    name = "hunter"

    async def handle(self, task: dict[str, Any]) -> dict[str, Any]:
        sources = self.config.get("sources", [])
        self.log.info(f"Hunter scanning {len(sources)} sources...")
        result = await self.reason(
            system=SYSTEM_PROMPT,
            user=f"Scan these sources for new opportunities: {sources}\n\nContext: {task.get('context', '')}",
            max_tokens=8192,
        )
        return {
            "agent": self.name,
            "model": result.model,
            "tokens": result.total_tokens,
            "output": result.content,
        }
