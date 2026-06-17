"""Tracing unit tests."""

from __future__ import annotations

import asyncio

import pytest
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.trace import StatusCode

from l9_service.observability.tracing import add_event, get_trace_context, instrument, span


def test_span_attributes(span_exporter: InMemorySpanExporter) -> None:
    with span("op", attributes={"k": "v"}):
        pass
    spans = span_exporter.get_finished_spans()
    assert len(spans) == 1
    assert spans[0].attributes is not None
    assert spans[0].attributes.get("k") == "v"


def test_span_records_exception(span_exporter: InMemorySpanExporter) -> None:
    with pytest.raises(ValueError, match="boom"), span("fail"):
        raise ValueError("boom")
    s = span_exporter.get_finished_spans()[0]
    assert s.status.status_code == StatusCode.ERROR
    assert any(e.name == "exception" for e in s.events)


def test_nested_spans(span_exporter: InMemorySpanExporter) -> None:
    with span("parent"), span("child"):
        pass
    assert {s.name for s in span_exporter.get_finished_spans()} == {"parent", "child"}


def test_instrument_sync(span_exporter: InMemorySpanExporter) -> None:
    @instrument("sync.fn")
    def fn(x: int) -> int:
        return x * 2

    assert fn(21) == 42
    assert any(s.name == "sync.fn" for s in span_exporter.get_finished_spans())


def test_instrument_async(span_exporter: InMemorySpanExporter) -> None:
    @instrument("async.fn")
    async def fn() -> str:
        return "ok"

    assert asyncio.run(fn()) == "ok"
    assert any(s.name == "async.fn" for s in span_exporter.get_finished_spans())


def test_trace_context_inside_span(span_exporter: InMemorySpanExporter) -> None:
    ctx: dict[str, str] = {}
    with span("ctx"):
        ctx = get_trace_context()
    assert len(ctx.get("trace_id", "")) == 32
    assert len(ctx.get("span_id", "")) == 16


def test_trace_context_outside_span() -> None:
    assert get_trace_context() == {}


def test_add_event(span_exporter: InMemorySpanExporter) -> None:
    with span("ev"):
        add_event("cache.hit", {"key": "x"})
    assert any(e.name == "cache.hit" for e in span_exporter.get_finished_spans()[0].events)
