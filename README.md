##### Чтобы проверить, что сервер действительно интегрирован с Sentry IO, нужно параметру dsn передать свои данные:
```python
sentry_sdk.init(
    dsn= "", # Укажите свои данные
    integrations=[BottleIntegration()]
)
```

##### Далее нужно запустить сервер:
```
python server.py
```

##### И в браузере перейти по адресу:
```
http://localhost:8080/fail
```
