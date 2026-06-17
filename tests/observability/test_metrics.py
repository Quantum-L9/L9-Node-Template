"""Metrics unit tests."""

from __future__ import annotations

import time

from opentelemetry.sdk.metrics.export import InMemoryMetricReader

from l9_service.observability.metrics import Metrics


def _names(r: InMemoryMetricReader) -> list[str]:
    d = r.get_metrics_data()
    return (
        []
        if not d
        else [m.name for rm in d.resource_metrics for sm in rm.scope_metrics for m in sm.metrics]
    )


def test_count(metric_reader: InMemoryMetricReader) -> None:
    Metrics("l9.test").count("req", value=5, labels={"m": "GET"})
    assert any("req" in n for n in _names(metric_reader))


def test_count_default(metric_reader: InMemoryMetricReader) -> None:
    Metrics("l9.test").count("evt")
    assert any("evt" in n for n in _names(metric_reader))


def test_timer(metric_reader: InMemoryMetricReader) -> None:
    m = Metrics("l9.test")
    with m.timer("db.ms"):
        time.sleep(0.01)
    assert any("db.ms" in n for n in _names(metric_reader))


def test_record(metric_reader: InMemoryMetricReader) -> None:
    Metrics("l9.test").record("sz", value=1024.0, unit="By")
    assert any("sz" in n for n in _names(metric_reader))


def test_updown(metric_reader: InMemoryMetricReader) -> None:
    m = Metrics("l9.test")
    m.updown("conn", value=10)
    m.updown("conn", value=-3)
    assert any("conn" in n for n in _names(metric_reader))


def test_namespaces(metric_reader: InMemoryMetricReader) -> None:
    Metrics("svc.a").count("ops")
    Metrics("svc.b").count("ops")
    names = _names(metric_reader)
    assert any("svc.a" in n for n in names)
    assert any("svc.b" in n for n in names)
