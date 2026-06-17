# Parametric Cursor Rule Rendering

This pack closes the domain-cartridge gap: reusable `.mdc.template` files become concrete `.cursor/rules/*.mdc` files using per-repo values from `plugin-config.yaml`.

## First migration

```bash
uv add --dev pyyaml
uv run python scripts/render_cursor_rules.py --force
uv run python scripts/render_cursor_rules.py --check --diff
```

Use `--force` only once when migrating existing hand-authored `.mdc` files. After that, rendered files contain an `L9_RENDERED` header and can be updated without `--force`.

## Ongoing workflow

```bash
make render-rules   # apply template/config changes
make check-rules    # fail if rendered rules drift
make drift-check    # alias for check-rules today; future home for ADR/graph drift
```

## Template syntax

Templates use Python `string.Template` placeholders:

```md
Repo: `${repo_name}`
Protected paths:
${protected_paths_bullets}
```

List values expose these forms:

- `${protected_paths}` — bullet list
- `${protected_paths_bullets}` — bullet list
- `${protected_paths_csv}` — inline code CSV
- `${protected_paths_json}` — JSON block

## Drift detection

`--check` re-renders in memory and compares expected output against committed `.cursor/rules/*.mdc` files. If any target differs, it exits non-zero. With `--diff`, it prints unified diffs.

## Graphable output

Every render writes `.cursor/rules/.render-manifest.json` with config hash, template hash, output hash, and render IDs. This is the graphable event record for the L9 Compounding Leverage Kernel.
