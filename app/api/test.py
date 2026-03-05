import httpx
import redis
import json
from apscheduler.schedulers.background import BackgroundScheduler


url = "https://api.exchangerate.host/live"
API_key = "6c6afbe59e93916599b1977d10db6252"

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def update_rates():

    params = {
        "access_key": API_key,
        "currencies": "USD, EUR, JPY, CNH, UZS, RUB, CAD",
    }

    response = httpx.get(url, params=params)
    data = response.json()

    rates = data["quotes"]

    r.set("currency_rates", json.dumps(rates))

    print("Rates updated")


scheduler = BackgroundScheduler()

scheduler.add_job(update_rates, "interval", hours=1)

scheduler.start()


update_rates()