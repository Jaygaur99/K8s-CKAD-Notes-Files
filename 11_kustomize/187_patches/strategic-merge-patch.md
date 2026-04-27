### Strategic-merge-patch

While we used

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

this patch uses the standard k8s syntax and updates whatever is written in it

```yaml
patches:
	- patch: |-
			apiVersion: apps/v1
			kind: Deployment
			metadata:
				name: api-deployment
			spec:
				replicas: 5
```
