"""Chain Agent — on-chain TX simulation, slippage check, gas optimization."""

from __future__ import annotations

from typing import Any

from src.agents.base import BaseAgent

SYSTEM_PROMPT = """You are the Chain Agent for Blacky Orbit.

For each on-chain transaction request:
1. Simulate the call against current state (eth_call / debug_traceCall)
2. Verify expected outcome matches user intent
3. Check slippage stays within configured max (default 1.0%)
4. Optimize gas: recommend EIP-1559 priority fee + base fee buffer
5. Flag suspicious recipient or contract patterns

Output: simulation result + go/no-go verdict + final gas params.
"""


class ChainAgent(BaseAgent):
    name = "chain"
    model = "mimo-v2.5"

    async def handle(self, task: dict[str, Any]) -> dict[str, Any]:
        tx = task.get("tx", {})
        result = await self.reason(
            system=SYSTEM_PROMPT,
            user=f"TX request: {tx}\nSimulate and verify before send.",
            max_tokens=6000,
        )
        return {
            "agent": self.name,
            "tokens": result.total_tokens,
            "output": result.content,
        }
