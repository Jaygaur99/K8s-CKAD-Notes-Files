### 4 prefix

#### 🛠️ Common Transformations Overview

| Transformer                   | Purpose                                                  | Effect                                                        | Use Case Example                                                  |
| :---------------------------- | :------------------------------------------------------- | :------------------------------------------------------------ | :---------------------------------------------------------------- |
| **`commonLabels`**            | Adds standardized labels to every resource.              | Injects key-value pairs (e.g., `org: KodeKloud`).             | Tracking resources in CI/CD or identifying application ownership. |
| **`namePrefix`/`nameSuffix`** | Modifies the names of all created resources.             | Appends a prefix or suffix to deployment, service, etc. name. | Environment separation (e.g., `my-app-dev`).                      |
| **`namespace`**               | Sets a default namespace for all objects.                | Places every resource into a specified Kubernetes Namespace.  | Organizing resources by environment (`staging`, `production`).    |
| **`commonAnnotations`**       | Adds standardized metadata annotations to all resources. | Injects key-value pairs under `metadata.annotations`.         | Applying security or observability tags (e.g., logging handler).  |
