import httpx
import redis
import os
import json
from apscheduler.schedulers.background import BackgroundScheduler

url = "https://api.exchangerate.host/live"
API_key = "757727891951bce0158cc1f9ba9de207"

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)


def update_rates():
    params = {
        "access_key": API_key,
        "currencies": "USD,EUR,JPY,CNH,UZS,RUB,CAD",
    }

    response = httpx.get(url, params=params)
    data = response.json()

    if not data.get("success"):
        print("API error:", data)
        return

    rates = data["quotes"]


    r.hset("currency_rates", mapping=rates)

    print("Rates updated")


scheduler = BackgroundScheduler()
scheduler.add_job(update_rates, "interval", hours=24)