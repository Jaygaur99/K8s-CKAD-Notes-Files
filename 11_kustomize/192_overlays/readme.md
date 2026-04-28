# Overlays

### Really benificial when dealing with different environment with same config

```
k8s/
|--- base/
|     |--- kustomization.yaml
|     |--- nginx-depl.yaml
|     |--- service.yaml
|     |--- redis-depl.yaml
|
|--- overlays/
      |--- dev/
      |     |--- kustomization.yaml
      |     |--- config-map.yaml
      |--- stg/
      |     |--- kustomization.yaml
      |     |--- config-map.yaml
      |--- prod/
            |--- kustomization.yaml
            |--- config-map.yaml
```

Let's say we go tihs nginx-depl.yaml in base

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
---
### kustomization.yaml
resources:
  - nginx-depl.yaml
  - service.yaml
  - redis-depl.yaml
```

and we want to change it across environments.

```yaml
### dev/kustomization
bases:
  - ../../base

patch: |-
  - op: replace
    path: /spec/replicas
    value: 2

---
### prod/kustomization
bases:
  - ../../base

patch: |-
  - op: replace
    path: /spec/replicas
    value: 5
```

### We can also add stuff not present in other environments

```
k8s/
|--- base/
|     |--- kustomization.yaml
|     |--- nginx-depl.yaml
|     |--- service.yaml
|     |--- redis-depl.yaml
|
|--- overlays/
      |--- dev/
      |     |--- kustomization.yaml
      |     |--- config-map.yaml
      |     |--- volume.yaml.            <- like this
      |--- stg/
      |     |--- kustomization.yaml
      |     |--- config-map.yaml
      |--- prod/
            |--- kustomization.yaml
            |--- config-map.yaml
            |--- grafana-depl.yaml       <- like this
```

so kustomization.yaml file becomes

```yaml
### prod/kustomization
bases:
  - ../../base

resources:
  - grafana-depl.yaml

patch: |-
  - op: replace
    path: /spec/replicas
    value: 5
```
