import httpx

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

for pair, value in rates.items():
    print(F"1 {pair[3:]} = {value} {pair[:3]}")