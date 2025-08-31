import requests

def ask_curr(currency1, currency2, amount=1):
    url = f"https://api.frankfurter.dev/v1/latest?base={currency1}&symbols={currency2}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # lanza excepción si el status != 200
        data = response.json()

        rate = data["rates"][currency2]
        converted = amount * rate

        print(f"{amount} {currency1} = {converted:.2f} {currency2} (rate {rate}, date {data['date']})")
        return converted
    except Exception as e:
        print("Error fetching exchange rate:", e)

# Ejemplo de uso:
if __name__ == "__main__":
    curr1 = input("Moneda origen (ej. USD): ").strip().upper()
    curr2 = input("Moneda destino (ej. EUR): ").strip().upper()
    amt = float(input("Cantidad a convertir: ").strip())
    ask_curr(curr1, curr2, amt)
