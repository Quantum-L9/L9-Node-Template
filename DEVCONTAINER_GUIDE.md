<!-- L9_META role: devcontainer_guide version: 1.0.0 updated: 2026-06-07 /L9_META -->

# Devcontainer Guide — L9 Service

## Architecture

```
devcontainer = runtime body   →  OS, Python 3.12, uv, Docker-in-Docker, tools
.cursor/rules/ = agent mind   →  rules, skills, MCP config, agent constraints
```

These two layers compose. The devcontainer bootstraps the runtime. The plugin layer (`.cursor/rules/` + `SKILL.md`) governs agent behavior. Neither replaces the other.

## Opening the Container

### VS Code / Cursor
1. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open the repo root
3. Command Palette → `Dev Containers: Reopen in Container`
4. Wait for `onCreateCommand` and `postCreateCommand` to complete (~2–3 min on first build)
5. Terminal shows: `✅ L9 container ready — run: make ci`

### Confirming ready state
```bash
make ci   # MUST pass: format-check → lint → type → test-cov
```

## What's Installed Automatically

| Concern | Mechanism |
|---------|-----------|
| Python 3.12 | Base image |
| uv | `pip install uv` in `onCreateCommand` |
| All project deps | `uv sync --locked` in `onCreateCommand` |
| pre-commit hooks | `uv run pre-commit install` in `postCreateCommand` |
| Node LTS | devcontainer feature (for npx-based tools) |
| Docker CLI | docker-in-docker feature (for `make obs-up`) |
| GitHub CLI | github-cli feature |
| VS Code extensions | `customizations.vscode.extensions` auto-installed |

## Port Forwarding

| Port | Service | Notes |
|------|---------|-------|
| 8000 | FastAPI app | Notify on auto-forward |
| 3000 | Grafana | Silent auto-forward |
| 9090 | Prometheus | Silent auto-forward |
| 3200 | Tempo | Silent auto-forward |
| 4317 | OTel Collector gRPC | Silent auto-forward |
| 4318 | OTel Collector HTTP | Silent auto-forward |

## Debugging

All launch configs use `debugpy` with `.venv/bin/python`. Select from the VS Code Run & Debug panel (Ctrl+Shift+D):

| Config | Use for |
|--------|---------|
| `Python: Current File` | Quick debug of any `.py` file |
| `FastAPI: uvicorn --reload` | Full app debug with hot-reload |
| `FastAPI: fastapi dev (fastapi-cli)` | Debug via fastapi-cli module |
| `Pytest: All Tests` | Debug entire test suite |
| `Pytest: Current File` | Debug single test file |
| `Python: Module (prompt)` | Debug any module by name |

**Never use** `"program": "uv", "args": ["run", ...]` — debugpy cannot attach to the uv binary ([uv#7803](https://github.com/astral-sh/uv/issues/7803)).

## Plugin Layer (Agent Mind)

The agent cognitive layer lives in `.cursor/rules/`:

| File | Type | Purpose |
|------|------|---------|
| `00-global.mdc` | Always | Global invariants, quality gates, protected paths |
| `fastapi.mdc` | Auto (*.py) | FastAPI route conventions |
| `l9-agents.mdc` | Agent-requested | Autonomous task guardrails, Fix-B contract |
| `10-domain-cartridge.mdc` | Auto (rules/**) | Parametric template enforcement |

**All rules are domain-cartridge-aware** via `plugin-config.yaml`. Current rules are first-pass concrete instances — the parametric render step is a planned next action.

## Renaming for a New Service

1. Update `plugin-config.yaml`: `repo_name`, `package_name`, `app_entrypoint`
2. `grep -r "l9_service" src/ tests/ pyproject.toml` → replace with your package name
3. Update `devcontainer.json` `"name"` and `workspaceFolder`
4. Update `OTEL_SERVICE_NAME` in `.env.example`
5. `uv lock` → `make ci`

## Drift Detection (Planned)

A future `make drift-check` target will compare:
- Installed `.mdc` rule versions against `plugin-config.yaml` template registry
- `uv.lock` staleness against `pyproject.toml` changes

Until implemented, run `make ci` before every commit as the manual gate.
