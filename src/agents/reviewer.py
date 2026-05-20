"""Reviewer Agent — security audit + style check + dependency scan."""

from __future__ import annotations

from typing import Any

from src.agents.base import BaseAgent

SYSTEM_PROMPT = """You are the Reviewer Agent for Blacky Orbit.

Audit code passed by the Coder Agent across three dimensions:

1. Security: OWASP Top 10 + Web3-specific (reentrancy, front-running,
   oracle manipulation, signature replay, unsafe delegatecall)
2. Style: language-idiomatic, readable, type-safe
3. Dependencies: known CVEs, version pinning, license compatibility

Block on critical findings. Output: structured report with severity + fix.
"""


class ReviewerAgent(BaseAgent):
    name = "reviewer"
    model = "mimo-v2.5"

    async def handle(self, task: dict[str, Any]) -> dict[str, Any]:
        code = task.get("code", "")
        result = await self.reason(
            system=SYSTEM_PROMPT,
            user=f"Code under review:\n\n{code}",
            max_tokens=8000,
        )
        return {
            "agent": self.name,
            "tokens": result.total_tokens,
            "output": result.content,
        }
