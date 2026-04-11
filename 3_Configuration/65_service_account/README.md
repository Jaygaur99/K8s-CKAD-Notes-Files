## Service account

### Create service account

```bash
kubectl create serviceaccount <account-name>
```

### Check service accounts

```bash
kuebctl get serviceaccounts
```

### Check token (basically describe)

```bash
kubectl describe serviceaccount <account-name>
```

This gives us a link to the actual token. To check the token

```bash
kubectl describe secret <token-name>
```
