## CI Convergence to L9 Shared Model

This PR implements the full L9 shared CI pipeline based on the gap audit report.

### What was built

| Phase | Artifact | Status |
|-------|----------|--------|
| 1 | Namespaced labels (`type:*`, `area:*`, `status:*`) | Provisioned via API |
| 2 | `.github/scripts/classify_pr.py` | Deployed |
| 3 | `.github/governance/routing_policy.yaml`, `blocking_policy.yaml`, `comment_protocol.yaml` | Deployed |
| 4 | `.github/workflows/pr-pipeline.yml` (canonical merge gate) | Deployed |
| 5 | `.github/workflows/gitleaks.yml`, `dependency-review.yml`, `.gitleaks.toml` | Deployed |

### Auditor Gap Report (Input)

Prior audit showed `overall_status: divergent` with:
- Missing classifier foundation
- Missing canonical PR Pipeline Gate
- Missing namespaced label taxonomy
- Missing security/supply chain workflows
- Missing governance policy files

### Verification

- Local `verify_convergence.py`: **PASS** (no critical or structural gaps)
- Classifier runs without errors
- All workflows have `permissions:` and `concurrency:` blocks
- Gate job uses `if: always()` pattern

### Expected CI Behavior

The PR Pipeline Gate will run against this PR itself:
1. **classify** — detects `.py`, `.yaml`, `.yml`, `.toml` changes → routes to lint + security
2. **lint** — runs ruff check/format
3. **test** — runs pytest if test config exists
4. **security** — runs semgrep scan
5. **gate** — evaluates all job results, passes if none failed

### Post-Merge

After this PR merges, branch protection should be configured:
- Required status check: `PR Pipeline Gate`
- Squash merge only
- Delete head branches on merge

### Handoff

If CI fails on this PR, `l9-ci-ops` will diagnose and push fixes to this branch.
