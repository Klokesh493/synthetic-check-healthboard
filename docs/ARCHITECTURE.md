# Synthetic Check Healthboard architecture

Summarizes synthetic check pass rates and highlights degraded journeys.

```mermaid
flowchart LR
    N0["sample_checks.csv"]
    N1["synthetic_healthboard.py"]
    N2["summarize / degraded"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
