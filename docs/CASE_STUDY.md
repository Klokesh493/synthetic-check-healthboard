# Synthetic Check Healthboard walkthrough

## Business problem

Summarizes synthetic check pass rates and highlights degraded journeys.

## Reproduce the workflow

Run `python3 synthetic_healthboard.py sample_checks.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
checkout
```

The sample supplies these fields. `journey`, `status`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
