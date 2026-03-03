import httpx
import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

data = r.get("currency_rates")
rate = json.loads(data)


for pair, value in rate.items():
    print(F"1 {pair[3:]} = {value} {pair[:3]}")
