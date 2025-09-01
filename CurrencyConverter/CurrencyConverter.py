import requests

def getCurrencyRates(Base, Target):
    API_KEY = "5de90943678974951c39f487"          # pon aquí tu key

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{Base}"

    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    if data["result"] != "success":
        raise RuntimeError(f"API error: {data.get('error-type', 'unknown')}")

    rate = data["conversion_rates"][Target]  # EUR -> USD
    print(f"1 {Base} = {rate} {Target}")

Base = input("From (currency code): ").upper()
Target = input("To (currency code): ").upper()
getCurrencyRates(Base, Target)
