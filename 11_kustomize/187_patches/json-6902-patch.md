### Json 6902 patch

```yaml
### api-depl.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: api
  template:
    metadata:
      labels:
        component: api
    spec:
      containers:
        - name: nginx
          image: nginx
---
# +
---
#### kustomization.yaml
patches:
  - target:
      kind: Deployment
      name: api-deployment

    # This symbol `|-` is required, explained why in next lecture
    patch: |-
      - op: replace
        path: /metadata/name
        value: web-deployment

  - target:
      kind: Deployment
      name: web-deployment
    patch: |-
      - op: replace
        path: /spec/replicas
        value: 5
```

This modifies the yaml like this

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 5
  selector:
    matchLabels:
      component: web
  template:
    metadata:
      labels:
        component: web
    spec:
      containers:
        - name: nginx
          image: nginx
```
