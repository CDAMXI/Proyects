import requests

def getCurrencyRates(Base, Target, Amount):
    API_KEY = "5de90943678974951c39f487"          # pon aquí tu key

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{Base}"

    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    if data["result"] != "success":
        raise RuntimeError(f"API error: {data.get('error-type', 'unknown')}")
    
    rate = data["conversion_rates"][Target]
    converted = Amount * data["conversion_rates"][Target]
    print(f"{Amount} {Base} = {converted:.2f} {Target}")

Base = input("From (currency code): ").upper()
Amount = float(input("Amount: "))
Target = input("To (currency code): ").upper()

getCurrencyRates(Base, Target, Amount)
