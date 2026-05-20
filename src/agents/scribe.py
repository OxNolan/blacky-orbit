"""Scribe Agent — documentation, daily summaries, knowledge persistence."""

from __future__ import annotations

from typing import Any

from src.agents.base import BaseAgent

SYSTEM_PROMPT = """You are the Scribe Agent for Blacky Orbit.

Your role: persist agent activity into a structured knowledge base.

For each input:
1. Generate a concise human-readable summary
2. Tag with relevant categories (project, chain, action, status)
3. Output Markdown suitable for Obsidian / Notion

At end-of-day, generate a daily report aggregating all agent activity.
"""


class ScribeAgent(BaseAgent):
    name = "scribe"
    model = "mimo-v2.5"

    async def handle(self, task: dict[str, Any]) -> dict[str, Any]:
        events = task.get("events", [])
        result = await self.reason(
            system=SYSTEM_PROMPT,
            user=f"Summarize and tag these events:\n\n{events}",
            max_tokens=4000,
        )
        return {
            "agent": self.name,
            "tokens": result.total_tokens,
            "output": result.content,
        }
