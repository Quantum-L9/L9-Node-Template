<!-- L9_META
role: architecture_doc
version: 1.0.0
status: template
tags: [l9, architecture, boundaries, invariants]
/L9_META -->

# Architecture — {{node_slug}}

## System Boundaries

This node follows the L9 single-responsibility architecture contract:

- **`enginehandlers.py` is the sole SDK bridge.** No other file in this repo imports from `l9_sdk.transport`.
- **Gate is the sole router.** No direct node-to-node HTTP. All packets arrive and depart via `TransportPacket` through Gate.
- **`PacketEnvelope` is forbidden.** Any usage is a HIGH audit violation.
- **Domain logic lives in `src/l9_service/domain/`.** This package must not import from the SDK transport layer.
- **`/healthz` and `/readyz` are unauthenticated.** Always return 200 when the process is alive.

## File Responsibility Map

| File | Role | L9 Constraint |
|------|------|---------------|
| `src/l9_service/enginehandlers.py` | SDK bridge — only SDK transport importer | Must export one `async handle_<action>()` per ENGINESPEC action |
| `src/l9_service/domain/` | Pure business logic | No SDK transport imports |
| `src/l9_service/main.py` | FastAPI app factory | healthz/readyz only at template birth |
| `contracts/NODECONTRACT.yaml` | Authority + ownership boundary | Defines what this node owns and may do |
| `contracts/ENGINESPEC.yaml` | Action registration | Read by SDK at startup; must align with handlers |

## Handler-Spec Alignment Gate

The number and names of `async handle_<action>` functions in `enginehandlers.py` MUST match the `actions[]` list in `contracts/ENGINESPEC.yaml` exactly. The contract verifier (`tools/verify_contracts.py`) and CI audit gate enforce this at every PR.

## Observability

All telemetry flows through `src/l9_service/observability/`. No `print()` in `src/`. The Fix-B pattern isolates OTel providers in test scope without affecting production init.

## What Belongs Here vs. Gate/Chassis

| Concern | Owner |
|---------|-------|
| HTTP auth, tenancy, rate limiting | Chassis/Gate — never this node |
| Routing logic between nodes | Gate — never this node |
| Domain business rules | `src/l9_service/domain/` |
| SDK transport | `src/l9_service/enginehandlers.py` only |
| Observability init | `src/l9_service/observability/bootstrap.py` |
