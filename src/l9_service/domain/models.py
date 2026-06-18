# <!-- L9_META role: domain_models version: 1.0.0 /L9_META -->
"""Pydantic domain models for {{node_slug}}.

Define request/response payloads and domain entities here.
Reference these from enginehandlers.py action handlers.
"""
from __future__ import annotations
from pydantic import BaseModel


# Example — replace with real domain models from nodespec.yaml § domain_models
class ExampleRequest(BaseModel):
    id: str
    payload: dict


class ExampleResponse(BaseModel):
    success: bool
    result: dict | None = None
