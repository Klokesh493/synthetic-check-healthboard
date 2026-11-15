# Synthetic Check Healthboard

A noisy synthetic check stream can hide a degraded user journey. Operators need a pass rate grouped by journey.

[Skills and verification](docs/ENGINEERING_NOTES.md)

## What I built

I built a synthetic monitoring summary that groups results by user journey and flags pass rates below 95%. This makes a failing journey visible even if other checks are healthy.

## How it works

```mermaid
flowchart LR
    A["Synthetic results CSV"]
    B["Group by journey and calculate pass rates"]
    C{"Pass rate below threshold?"}
    D["List degraded journey"]
    E["Omit healthy journey"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [synthetic_healthboard.py](synthetic_healthboard.py) implements the CLI and decision rules. Uses `collections` to group or count records, `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 synthetic_healthboard.py sample_checks.csv
```

Checkout is the only journey flagged by the bundled fixture. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 synthetic_healthboard.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The program summarizes supplied check results. An external probe scheduler and alerting integration are separate components.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
