"""Guardian Agent — 4-pass anti-sybil + scam contract detection."""

from __future__ import annotations

from typing import Any

from src.agents.base import BaseAgent

PASS_PROMPTS = {
    1: "Pass 1 — Wallet fingerprint analysis. Examine TX history pattern, gas usage profile, token interaction graph. Output: fingerprint summary.",
    2: "Pass 2 — Cluster analysis. Cross-correlate behavior with related wallets. Detect IP / timing / amount collisions. Output: cluster verdict.",
    3: "Pass 3 — Counter-heuristic. Test pattern against known sybil-detection algorithms (LayerZero, zkSync, Linea, Arbitrum STIP). Output: estimated detection probability.",
    4: "Pass 4 — Synthesis (MiMo-V2.5-Pro long-chain reasoning). Combine passes 1-3 into final risk score with actionable hygiene recommendations.",
}


class GuardianAgent(BaseAgent):
    name = "guardian"

    async def handle(self, task: dict[str, Any]) -> dict[str, Any]:
        passes = self.config.get("passes", 4)
        wallet = task.get("wallet")
        results: list[str] = []
        total_tokens = 0
        for i in range(1, passes + 1):
            self.log.info(f"Guardian pass {i}/{passes}")
            r = await self.reason(
                system=PASS_PROMPTS[i],
                user=f"Wallet under analysis: {wallet}\nPrevious passes: {results}",
                max_tokens=6000,
            )
            results.append(r.content)
            total_tokens += r.total_tokens
        return {
            "agent": self.name,
            "passes": passes,
            "tokens": total_tokens,
            "output": results,
        }
