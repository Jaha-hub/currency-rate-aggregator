import httpx
import redis
import json

url = "https://api.exchangerate.host/live"

API_key = "6c6afbe59e93916599b1977d10db6252"


def get_list():
    params = {
        "access_key": API_key,
        "currencies": "USD, EUR, JPY, CNH,  UZS, RUB, CAD",
    }

    response = httpx.get(url, params=params)
    data = response.json()
    return data["quotes"]


rates = get_list()



r = redis.Redis(host="localhost", port=6379, decode_responses=True)

r.set("currency_rates", json.dumps(rates))


data = r.get("currency_rates")
rate = json.loads(data)


for pair, value in rate.items():
    print(F"1 {pair[3:]} = {value} {pair[:3]}")

