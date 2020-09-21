import os
import sentry_sdk

from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

app = Bottle()


# @app.route('/success')
@app.route('/')
def success():
    return "Ok"


@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")
    return


sentry_sdk.init(
    dsn= "https://451dcbfea8954a5293d16d6d531cd99d@o450835.ingest.sentry.io/5435828",
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
