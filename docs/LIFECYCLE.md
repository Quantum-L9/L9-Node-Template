<!-- L9_META
role: lifecycle_doc
version: 1.0.0
status: template
tags: [l9, lifecycle, states, transitions]
/L9_META -->

# Lifecycle — {{node_slug}}

Generated from `nodespec.yaml § lifecycle`. Replace all placeholder sections with real state machine definition.

## States

| State | Description | Terminal? |
|-------|-------------|-----------|
| `PENDING` | Waiting for initial data or dependency | No |
| `ACTIVE` | Processing normally | No |
| `SUSPENDED` | Temporarily paused by orchestrator | No |
| `COMPLETED` | Terminal success state | Yes |
| `FAILED` | Terminal failure state | Yes |

## Valid Transitions

```
PENDING → ACTIVE
ACTIVE → SUSPENDED | COMPLETED | FAILED
SUSPENDED → ACTIVE | FAILED
```

## Invalid Transitions

The following transitions are PROHIBITED and will raise a lifecycle guard error:

- `COMPLETED → any`
- `FAILED → any` (use compensating action instead)
- Any transition not listed above

## Guard Logic

Handler guards in `enginehandlers.py` MUST check current state before mutating.
State transitions MUST be written atomically through the SDK lifecycle API.
