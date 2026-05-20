"""MiMo API client wrapper.

Thin async wrapper over the MiMo OpenAI-compatible endpoint. Handles
retries, rate limiting, and per-agent token accounting.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

log = logging.getLogger(__name__)


@dataclass
class MiMoResponse:
    content: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class MiMoClient:
    """Async client for the MiMo API platform."""

    def __init__(
        self,
        api_key: str | None = None,
        api_base: str = "https://api.xiaomimimo.com/v1",
        timeout: float = 60.0,
    ) -> None:
        self.api_key = api_key or os.environ.get("MIMO_API_KEY", "")
        self.api_base = api_base.rstrip("/")
        self.timeout = timeout
        if not self.api_key:
            raise RuntimeError("MIMO_API_KEY not set")
        self._client = httpx.AsyncClient(
            base_url=self.api_base,
            timeout=timeout,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
        )

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
    async def chat(
        self,
        messages: list[dict],
        model: str = "mimo-v2.5-pro",
        max_tokens: int = 4096,
        temperature: float = 0.3,
    ) -> MiMoResponse:
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        resp = await self._client.post("/chat/completions", json=payload)
        resp.raise_for_status()
        data = resp.json()
        usage = data.get("usage", {})
        return MiMoResponse(
            content=data["choices"][0]["message"]["content"],
            model=data.get("model", model),
            prompt_tokens=usage.get("prompt_tokens", 0),
            completion_tokens=usage.get("completion_tokens", 0),
            total_tokens=usage.get("total_tokens", 0),
        )

    async def aclose(self) -> None:
        await self._client.aclose()
