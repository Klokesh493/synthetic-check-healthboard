# Synthetic Check Healthboard

Summarizes synthetic check pass rates and highlights degraded journeys.

Focus: Consumer-scale SRE monitoring.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 synthetic_healthboard.py sample_checks.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.
