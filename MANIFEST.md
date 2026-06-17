<!-- L9_META role: pack_manifest version: 1.3.0 /L9_META -->
# L9_REPO_TEMPLATE — MANIFEST v1.3.0

Generated: 2026-06-08T00:46:53Z  
Total files: 49 (excl. MANIFEST.md itself)  
Checksum: SHA-256 first 12 hex chars  

| # | Path | Category | Purpose | Pass | SHA-256[:12] |
|---|------|----------|---------|------|--------------|
| 1 | `.cursor/mcp.json` | editor | Cursor rules (.mdc) + MCP config | devcontainer-pass | `2fcf03ab0701` |
| 2 | `.cursor/rules/00-global.mdc` | editor | Cursor rules (.mdc) + MCP config | optimize-pass | `b8acbe76566e` |
| 3 | `.cursor/rules/10-domain-cartridge.mdc` | editor | Cursor rules (.mdc) + MCP config | devcontainer-pass | `c0f7ad95d4b9` |
| 4 | `.cursor/rules/fastapi.mdc` | editor | Cursor rules (.mdc) + MCP config | optimize-pass | `49a69655ccd0` |
| 5 | `.cursor/rules/l9-agents.mdc` | editor | Cursor rules (.mdc) + MCP config | optimize-pass | `9f636ddd710d` |
| 6 | `.cursor/rules/templates/00-global.mdc.template` | tooling | Parametric .mdc.template source files | renderer-merge | `d2d7516dc8af` |
| 7 | `.cursor/rules/templates/10-domain-cartridge.mdc.template` | tooling | Parametric .mdc.template source files | renderer-merge | `9eb1c85dbfa2` |
| 8 | `.cursor/rules/templates/fastapi.mdc.template` | tooling | Parametric .mdc.template source files | renderer-merge | `069513de8279` |
| 9 | `.cursor/rules/templates/l9-agents.mdc.template` | tooling | Parametric .mdc.template source files | renderer-merge | `d163134735eb` |
| 10 | `.devcontainer/devcontainer.json` | devenv | Dev Container — Python 3.12, uv, Docker-in-Docker | devcontainer-pass | `fbff0cd3ce15` |
| 11 | `.env.example` | project | Env var template | optimize-pass | `e90f3c9b0724` |
| 12 | `.github/workflows/ci.yml` | ci | GitHub Actions CI ladder | prior-turn | `52f035a549ce` |
| 13 | `.gitignore` | project | Git ignore rules | prior-turn | `87e1b25f6124` |
| 14 | `.pre-commit-config.yaml` | quality | pre-commit hooks: ruff + pyright | prior-turn | `649501866669` |
| 15 | `.python-version` | project | Python version pin | prior-turn | `7b55f8e67b56` |
| 16 | `.vscode/extensions.json` | editor | VS Code/Cursor: settings, extensions, launch | devcontainer-pass | `1e4d42a87a08` |
| 17 | `.vscode/launch.json` | editor | VS Code/Cursor: settings, extensions, launch | devcontainer-pass | `8752b8ee0405` |
| 18 | `.vscode/settings.json` | editor | VS Code/Cursor: settings, extensions, launch | devcontainer-pass | `eb6c499d7d22` |
| 19 | `AGENTS.md` | project | Agent contract — INVARIANTS, tool authority | optimize-pass | `4ca0b1921450` |
| 20 | `DEVCONTAINER_GUIDE.md` | project | Body/mind architecture, port map, debug configs | devcontainer-pass | `4505ea0fff85` |
| 21 | `Justfile` | task-runner | Just recipes — includes render-rules, check-rules | optimize-pass | `68c0974f568d` |
| 22 | `Makefile` | task-runner | GNU Make — includes render-rules, check-rules | optimize-pass | `b8d341e0b307` |
| 23 | `README.md` | project | Quickstart, tree, Fix-B, rename checklist | optimize-pass | `d72813d19e9a` |
| 24 | `docs/PARAMETRIC_CURSOR_RULES.md` | docs | Renderer usage guide | renderer-merge | `e480fdd1e600` |
| 25 | `observability/docker-compose.observability.yml` | obs | Grafana/Prometheus/Tempo/OTel Collector | prior-turn | `d339aac464eb` |
| 26 | `observability/grafana/provisioning/dashboards/dashboards.yaml` | obs | Grafana/Prometheus/Tempo/OTel Collector | prior-turn | `ca43a3d543cc` |
| 27 | `observability/grafana/provisioning/datasources/datasources.yaml` | obs | Grafana/Prometheus/Tempo/OTel Collector | prior-turn | `82fe16771aa9` |
| 28 | `observability/otel-collector-config.yaml` | obs | Grafana/Prometheus/Tempo/OTel Collector | prior-turn | `86dfe4596b11` |
| 29 | `observability/prometheus.yml` | obs | Grafana/Prometheus/Tempo/OTel Collector | prior-turn | `46f21147b12b` |
| 30 | `observability/tempo-config.yaml` | obs | Grafana/Prometheus/Tempo/OTel Collector | prior-turn | `53f1e4a30b1f` |
| 31 | `plugin-config.yaml` | project | Domain cartridge — per-repo values for renderer | devcontainer-pass | `97ef462b3fdf` |
| 32 | `pyproject.toml` | project | Project metadata + all tool config | prior-turn | `32e096f6fb1d` |
| 33 | `scripts/render_cursor_rules.py` | tooling | Parametric .mdc renderer — reads plugin-config.yaml | renderer-merge | `d6938de5eee0` |
| 34 | `src/l9_service/__init__.py` | source | FastAPI + Fix-B OTel observability | prior-turn | `fb6de1aab9e1` |
| 35 | `src/l9_service/main.py` | source | FastAPI + Fix-B OTel observability | prior-turn | `b602b3c9726e` |
| 36 | `src/l9_service/observability/__init__.py` | source | FastAPI + Fix-B OTel observability | prior-turn | `ec826bb0fc69` |
| 37 | `src/l9_service/observability/bootstrap.py` | source | FastAPI + Fix-B OTel observability | prior-turn | `c09c36cbe404` |
| 38 | `src/l9_service/observability/logging.py` | source | FastAPI + Fix-B OTel observability | prior-turn | `7a23f74d56bd` |
| 39 | `src/l9_service/observability/metrics.py` | source | FastAPI + Fix-B OTel observability | prior-turn | `5a02fd0ab178` |
| 40 | `src/l9_service/observability/tracing.py` | source | FastAPI + Fix-B OTel observability | prior-turn | `29a145de2268` |
| 41 | `src/l9_service/py.typed` | source | FastAPI + Fix-B OTel observability | prior-turn | `e3b0c44298fc` |
| 42 | `tests/__init__.py` | tests | pytest — 24 tests, 70.44% coverage | prior-turn | `e3b0c44298fc` |
| 43 | `tests/conftest.py` | tests | pytest — 24 tests, 70.44% coverage | prior-turn | `a38444bb318a` |
| 44 | `tests/observability/__init__.py` | tests | pytest — 24 tests, 70.44% coverage | prior-turn | `e3b0c44298fc` |
| 45 | `tests/observability/conftest.py` | tests | pytest — 24 tests, 70.44% coverage | prior-turn | `c453d72dd1e8` |
| 46 | `tests/observability/test_logging.py` | tests | pytest — 24 tests, 70.44% coverage | prior-turn | `8d75c85a7fe2` |
| 47 | `tests/observability/test_metrics.py` | tests | pytest — 24 tests, 70.44% coverage | prior-turn | `e7ab2ea29312` |
| 48 | `tests/observability/test_tracing.py` | tests | pytest — 24 tests, 70.44% coverage | prior-turn | `71328874085c` |
| 49 | `uv.lock` | project | Locked dep manifest | prior-turn | `d023ff026211` |

## Pass Key
| Tag | Meaning |
|-----|---------|
| renderer-merge | Merged from renderer pack in this consolidation pass |
| devcontainer-pass | Written/improved in devcontainer pass |
| optimize-pass | Improved in recursive-optimization pass |
| prior-turn | Created and validated in earlier turns; unchanged |

## CI Gate Results
| Gate | Result |
|------|--------|
| `ruff format --check` | ✅ pass |
| `ruff check` | ✅ pass |
| `pyright src/` | ✅ 0 errors |
| `pytest` (24 tests) | ✅ pass |
| Coverage | ✅ 70.44% (threshold 70%) |

## Separation Contract
This ZIP is the **repo template** (body). It contains a filled-in `plugin-config.yaml` (cartridge values)
and rendered `.cursor/rules/*.mdc` files. The renderer templates and script are present here for
operational convenience, but their canonical home is `l9_parametric_rule_renderer_pack.zip`.
When the renderer pack is updated, run `make render-rules` or `just render-rules` to re-render.
