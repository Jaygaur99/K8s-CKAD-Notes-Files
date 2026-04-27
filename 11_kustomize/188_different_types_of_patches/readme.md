### Different kind of patches

#### Inline patch

```yaml
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: replace
        path: /spec/replicas
        value: 5
```

#### Separate file patch

```yaml
### kustomization.yaml
patches:
  - path: replica-patch.yaml
    target:
      kind: Deployment
      name: api-deployment
---
### replica-patch.yaml
- op: replace
  path: /spec/replicas
  value: 5
```
