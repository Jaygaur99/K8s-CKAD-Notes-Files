# Components

## Folder structure

```
/project-root
├── base/                 # Shared configurations (API deployment, etc.)
│   └── kustomization.yaml
├── components/           # <-- NEW: Holds all reusable features
│   ├── caching/          # Component 1
│   │   ├── kustomization.yaml # Internal config for the component
|   |   ├── deployment-patch.yaml
│   │   └── redis-deployment.yaml  # Feature resource
│   └── database/         # Component 2 (Example focus)
│       ├── kustomization.yaml
│       ├── postgres-deployment.yaml # Feature resource
│       └── deployment-patch.yaml    # Patch applied to the BASE API
├── overlays/             # Environment specific implementations
    ├── dev/              # Consumes components needed for Dev (e.g., database)
    |   ├── kustomization.yaml
    ├── premium/          # Consumes both caching and database
    |   ├── kustomization.yaml
    └── selfhosted/
        ├── kustomization.yaml
```

Component will have a separate kind

```yaml
### db/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1alpha1
kind: Component

resources:
  - postgres-deployment.yaml

# storing secret for db
secretGenerator:
  - name: postgres-cred
    literals:
      - password=postgres123

patches:
  - deployment-patch.yaml

### db/deployment-patch.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
      - name: api
        env:
          - name: POSTGRES_PASSWORD
            valueFrom:
              secretKeyRef:
                name: postgres-cred
                key: password

### overlays/premium/kustomization.yaml
bases:
  - ../../base

components:
  - ../../components/db

# Rest of the overlays...
```
