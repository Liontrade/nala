# nala

Open terminal in repository directory and run following commands:

### Build container

```
podman build -t stock-prices-api-app .
```

### Run container 

```
podman run -d -p 5000:5000 --name stock-prices-api-container stock-prices-api-app
```
