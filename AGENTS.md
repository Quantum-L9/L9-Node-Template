<!-- L9_META
skill_schema: 1
role: workspace_invariant
tags: [l9, agents, contract, enforcement]
owner: igor_beylin
status: active
version: 1.1.0
updated: 2026-06-07
/L9_META -->

# L9 Service — Agent Contract

**Read this at the start of every session. Honor without exception. Do NOT skip sections.**

## Validation Ladder

Run in this exact order. Do NOT skip a step to reach the next.

```bash
uv run ruff format --check src/ tests/   # 1. format gate
uv run ruff check src/ tests/            # 2. lint gate
uv run pyright src/                      # 3. type gate
uv run pytest tests/ -v --tb=short       # 4. behavior gate
```

`make ci` / `just ci` runs all four sequentially. A failing gate MUST be resolved before moving forward.

## Safe Commands (no approval needed)

- `uv run ruff format --check src/ tests/`
- `uv run ruff check src/ tests/`
- `uv run pyright src/`
- `uv run pytest tests/ -v --tb=short`
- `make ci` / `just ci`
- `make obs-up` / `make obs-down` / `make obs-ps`

## Requires Context Before Running

- `uv add <package>` — modifies `pyproject.toml` + `uv.lock`; confirm package and version first
- `uv lock --upgrade` — upgrades all locked packages; confirm scope
- `uv run ruff format src/ tests/` — modifies files; confirm before running
- `uv run ruff check --fix src/ tests/` — modifies files; confirm before running

## Requires Explicit Human Approval — STOP and Ask

- `git push` — always confirm before pushing
- `git push --force` — STOP; never execute without explicit written approval
- `docker compose down -v` — STOP; destroys volumes and data
- `rm -rf .venv` — confirm with human
- Any change to `.github/workflows/*.yml`
- Any change to `observability/docker-compose.observability.yml`

## Protected Files — Do NOT Modify Without Approval

| File | Reason |
|------|--------|
| `uv.lock` | Generated only by `uv lock` or `uv add`; never hand-edit |
| `pyproject.toml` | Run `uv lock` after any change |
| `.github/workflows/*.yml` | CI contract; change requires human review |
| `observability/docker-compose.observability.yml` | Stack contract; change may break obs stack |
| `src/l9_service/observability/bootstrap.py` | OTel init is idempotent by design; changes break Fix-B |

## Tool Authority Map

| Concern        | Owner      | Enforcement gate      |
|----------------|------------|-----------------------|
| Format         | Ruff       | CI hard gate          |
| Lint           | Ruff       | CI hard gate          |
| Type checking  | Pyright    | CI hard gate          |
| Behavior       | pytest     | CI hard gate          |
| Dependencies   | uv         | `uv.lock` committed   |
| OTel runtime   | Obs stack  | Manual + smoke test   |

**No tool owns a responsibility that belongs to another tool in this table.**

## INVARIANTS — Never Violate

1. `uv.lock` MUST be committed and current. `uv sync --locked` MUST succeed.
2. All four CI gates MUST pass before any commit to `main` or `develop`.
3. `bootstrap._initialized` sentinel MUST remain the only idempotency guard for `setup_telemetry`.
4. `_provider_override` and `Metrics._test_provider` MUST only be set by test fixtures. Never in production paths.
5. No `print()` anywhere in `src/`. Use `get_logger(__name__)`.
6. No `eval`, `exec`, or `compile` anywhere in `src/` or `tests/`.
7. Tests MUST isolate OTel providers via Fix-B fixtures — never call `set_tracer_provider()` / `set_meter_provider()` directly in test bodies.
8. `healthz` and `readyz` endpoints MUST remain unauthenticated and always return 200 when the process is alive.

## Fix-B Pattern — OTel Test Isolation

OTel SDK 1.28+ uses a `do_once` sentinel that blocks repeated `set_*_provider()` calls in a single process. Fix-B bypasses this by injecting providers directly into module-level override slots:

- `tracing._provider_override` — injected by `span_exporter` fixture in `tests/observability/conftest.py`
- `Metrics._test_provider` — injected by `metric_reader` fixture in `tests/observability/conftest.py`
- Root `conftest.py` clears both overrides and resets `bootstrap._initialized` between every test via autouse fixture

**Production code MUST NEVER reference these override slots.**

## Rename Checklist

When forking this template for a new service:

1. `grep -r "l9_service" src/ tests/ pyproject.toml` → replace with your package name
2. Update `OTEL_SERVICE_NAME` in `.env.example`
3. Update `packages` in `[tool.hatch.build.targets.wheel]` in `pyproject.toml`
4. Run `uv lock` to regenerate lock file
5. Run `make ci` — all gates MUST pass before first commit

## Failure Handling

| Situation | Action |
|-----------|--------|
| `uv sync --locked` fails | Do NOT remove `uv.lock`; diagnose first |
| Pyright reports new errors after adding a dep | Fix types; do not suppress blindly |
| Coverage drops below 70% | Add targeted tests; do not lower threshold |
| `obs-up` fails | Check Docker is running; check port conflicts on 3000/9090/3200/4317 |
