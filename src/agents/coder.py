"""Coder Agent — autonomous code generation with TDD iteration loops."""

from __future__ import annotations

from typing import Any

from src.agents.base import BaseAgent

SYSTEM_PROMPT = """You are the Coder Agent for Blacky Orbit.

Generate production-quality code following TDD methodology:

Pass 1 — Spec Decomposition: break the high-level intent into testable units
Pass 2 — TDD Skeleton: write failing tests first, define contracts
Pass 3 — Implementation: generate code, run tests, iterate until green
Pass 4 — Refactor + Reviewer Handoff: pass to Reviewer Agent

Output: structured artifact bundle (tests, implementation, docs).
"""


class CoderAgent(BaseAgent):
    name = "coder"

    async def handle(self, task: dict[str, Any]) -> dict[str, Any]:
        spec = task.get("spec", "")
        iterations = self.config.get("tdd_iterations", 5)
        passes_output: list[str] = []
        total_tokens = 0
        for i in range(iterations):
            self.log.info(f"Coder TDD iteration {i+1}/{iterations}")
            r = await self.reason(
                system=SYSTEM_PROMPT,
                user=f"Spec: {spec}\nIteration: {i+1}\nPrevious work: {passes_output[-1] if passes_output else 'none'}",
                max_tokens=8000,
            )
            passes_output.append(r.content)
            total_tokens += r.total_tokens
        return {
            "agent": self.name,
            "iterations": iterations,
            "tokens": total_tokens,
            "output": passes_output,
        }
