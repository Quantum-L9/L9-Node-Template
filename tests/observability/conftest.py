"""OTel in-memory fixtures — Fix-B design."""

from __future__ import annotations

import pytest
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

import l9_service.observability.tracing as tracing_mod
from l9_service.observability.metrics import Metrics


@pytest.fixture
def span_exporter() -> InMemorySpanExporter:
    exporter = InMemorySpanExporter()
    provider = TracerProvider(resource=Resource.create({"service.name": "test"}))
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    tracing_mod._provider_override = provider
    yield exporter
    tracing_mod._provider_override = None
    exporter.clear()


@pytest.fixture
def metric_reader() -> InMemoryMetricReader:
    reader = InMemoryMetricReader()
    Metrics._test_provider = MeterProvider(
        resource=Resource.create({"service.name": "test"}),
        metric_readers=[reader],
    )
    yield reader
    Metrics._test_provider = None
