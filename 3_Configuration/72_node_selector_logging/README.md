### To label node

```bash
kubectl label nodes <node-name> <label-key>=<label-value>
```

For example

```bash
kubectl label nodes node-1 size=large
```

but node selector can't do complex stuff like AND, OR etc.
