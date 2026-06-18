<!-- This file contains ADDITIONS to AGENTS.md as part of the PR Pack.
     Merge the sections below into the appropriate sections of AGENTS.md -->

## New Section: L9 Contract Invariants

Add after the existing INVARIANTS section:

### L9 Transport + Architecture Invariants

9.  `enginehandlers.py` is the **sole SDK bridge** — it is the only file allowed to import from `l9_sdk.transport`.
10. Every `async handle_<action>` in `enginehandlers.py` MUST match an action in `contracts/ENGINESPEC.yaml`. Run `python tools/verify_contracts.py` after any change.
11. `PacketEnvelope` MUST NOT appear anywhere in this repo. `TransportPacket` only.
12. No direct node-to-node HTTP (`httpx`/`aiohttp`/`requests`) in `src/`. Gate is the sole router.
13. `src/l9_service/domain/` MUST NOT import from `l9_sdk.transport`.

## New Section: New Tools

Add to the Safe Commands section:

### Contract + Audit Tools

```bash
python tools/verify_contracts.py                         # contract presence + reference check
python tools/audit_engine.py --path src/ --fail-on HIGH  # HIGH-severity L9 audit
python tools/review/analyzers/template_compliance.py     # template manifest compliance
```

## Protected Files Additions

Add to the Protected Files table:

| `contracts/NODECONTRACT.yaml` | Node authority contract — codegen-generated |
| `contracts/ENGINESPEC.yaml` | Action registration — must align with handlers |
| `src/l9_service/enginehandlers.py` | Sole SDK bridge — alignment gate enforced |
| `.github/governance/blocking_policy.yaml` | Merge gate config |
| `.l9-template-version` | Template version pin — used by drift detection |
