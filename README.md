# DS2002CapTime

Working IP address: 34.48.132.123

# API Overview

Base URL: `http://YOUR_VM_EXTERNAL_IP:5000`

Authorization header required:
```
Authorization: Bearer supersecrettoken123
```

Endpoints:
- `GET /api/hello`
- `GET /api/secure-data`
- `GET /api/time?capital=CityName`

Example:
```
curl -H "Authorization: Bearer supersecrettoken123" "http://YOUR_VM_EXTERNAL_IP:5000/api/time?capital=London"
```
