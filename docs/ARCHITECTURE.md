# Synthetic Check Healthboard architecture

Summarizes synthetic check pass rates and highlights degraded journeys.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
