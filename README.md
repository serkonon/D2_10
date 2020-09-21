##### Для проверки интеграции с Sentry нужно в env.py указать значение переменной SENTRY_DSN:
```python
SENTRY_DSN="адрес DSN Sentry"
```

##### Далее запустить сервер:
```
python server.py
```

##### И в браузере перейти по адресу:
```
http://localhost:8080/fail
```
