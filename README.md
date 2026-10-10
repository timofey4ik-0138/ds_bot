# Setup
Копируем файл .env.example и переименновываем его в .env

В него вставляем нужную информацию.

ВАЖНО: не вставлять важную информацию в .env.example

## mac os
```bash
export SSL_CERT_FILE=$(python -m certifi)
export REQUESTS_CA_BUNDLE=$(python -m certifi)
```

# Run
```bash
python main.py
```

