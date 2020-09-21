import os
import sentry_sdk
from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration
import env

app = Bottle()


@app.route('/success')
def success():
    return "Ok"


@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")
    return


sentry_sdk.init(
    dsn=env.SENTRY_DSN,
    integrations=[BottleIntegration()]
)


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)


# app.run(host='localhost', port=8080)
