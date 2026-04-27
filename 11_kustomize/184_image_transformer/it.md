```yaml
### web-depl.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: web
  template:
    metadata:
      labels:
        component: web
    spec:
      containers:
        - name: web
          image: nginx
#  +
---
### kustomization.yaml
images:
  - name: nginx
    newName: haproxy
```

If we do this kustomization.yaml, it will replace the image with name 'nginx' with new name
then it becomes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      component: web
  template:
    metadata:
      labels:
        component: web
    spec:
      containers:
        - name: web
          image: haproxy
```

We can also use "newTag" for modifiying image tag
