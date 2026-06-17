"""Root conftest — Fix-B cleanup autouse."""

from __future__ import annotations

import pytest

import l9_service.observability.bootstrap as bootstrap_mod
import l9_service.observability.tracing as tracing_mod
from l9_service.observability.metrics import Metrics


@pytest.fixture(autouse=True)
def clear_fixb_overrides() -> None:
    tracing_mod._provider_override = None
    Metrics._test_provider = None
    bootstrap_mod._initialized = False
