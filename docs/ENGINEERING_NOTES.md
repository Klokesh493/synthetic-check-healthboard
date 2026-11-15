# Skills and verification

## What this repository demonstrates

A synthetic monitoring summary that groups results by user journey and flags pass rates below 95%. This makes a failing journey visible even if other checks are healthy.

## Reproduce the result

Checkout is the only journey flagged by the bundled fixture. Reproduce the primary fixture with `python3 synthetic_healthboard.py sample_checks.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The program summarizes supplied check results. An external probe scheduler and alerting integration are separate components.

Inspect sample count and test window for a degraded journey before escalating based on its pass rate.

[synthetic_healthboard.py](../synthetic_healthboard.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
