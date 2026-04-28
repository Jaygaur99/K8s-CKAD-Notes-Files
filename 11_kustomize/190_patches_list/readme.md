## Patches in list

### Replacing Item

#### In json patch (replace)

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
### kustomization.yaml
patches:
  - target:
      kind: Deployment
      name: api-deployment
    patch: |-
      - op: replace
        path: /spec/template/spec/containers/0
        value:
          name: haproxy
          image: haproxy
```

This leads to

```yaml
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
        - name: haproxy
          image: haproxy
```

#### Strategic merge patch (replace)

```yaml
### api-depl.yml
# same
---
### kustomization.yaml
patches:
  - label-patch.yaml
---
### label-patch.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - name: haproxy
          image: haproxy
```

### Adding Item

#### In Json patch

```yaml
patches:
  - target:
      kind: Deployment
      name: api-deployment

    # - in the path means append to end of list. Use int otherwise
    patch: |-
      - op: add
        path: /spec/template/spec/containers/- 
        value:
          name: haproxy
          image: haproxy
```

### Deleting Item

#### In Json patch

```yaml
patches:
  - target:
      kind: Deployment
      name: api-deployment

    # Remove value at index 1
    patch: |-
      - op: add
        path: /spec/template/spec/containers/1
```

#### In strategic patch

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - $patch: delete
          name: database

# This removes
# spec:
#   containers:
#     - name: database <---- This
#       image: mongo
#     - name: web
#       image: nginx
```
