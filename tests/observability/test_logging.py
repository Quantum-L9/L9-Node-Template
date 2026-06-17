"""Logging unit tests."""

from __future__ import annotations

from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

from l9_service.observability.logging import (
    _add_log_level,
    _inject_trace_context,
    configure_logging,
    get_logger,
)
from l9_service.observability.tracing import get_trace_context, span


def test_configure_no_raise() -> None:
    configure_logging(level="DEBUG", json=False)


def test_configure_idempotent() -> None:
    configure_logging()
    configure_logging()


def test_get_logger() -> None:
    assert get_logger("t") is not None


def test_get_logger_bindings() -> None:
    assert get_logger("t", svc="l9") is not None


def test_get_logger_chain() -> None:
    assert get_logger("t").bind(rid="x") is not None


def test_json_mode() -> None:
    configure_logging(json=True)
    configure_logging(json=False)


def test_trace_ctx_in_span(span_exporter: InMemorySpanExporter) -> None:
    ctx: dict[str, str] = {}
    with span("log.test"):
        ctx = get_trace_context()
    assert len(ctx.get("trace_id", "")) == 32


def test_no_trace_ctx_outside_span() -> None:
    assert get_trace_context() == {}


def test_inject_trace_context_no_span() -> None:
    """_inject_trace_context with no active span returns event_dict unchanged."""

    event: dict = {"event": "test"}
    result = _inject_trace_context(None, "info", event)  # type: ignore[arg-type]
    assert "trace_id" not in result


def test_add_log_level_processor() -> None:
    """_add_log_level stamps the level key correctly."""

    event: dict = {"event": "test"}
    result = _add_log_level(None, "warning", event)  # type: ignore[arg-type]
    assert result["level"] == "WARNING"
