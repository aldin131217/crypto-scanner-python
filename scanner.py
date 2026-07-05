import requests

coins = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT"]

for coin in coins:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}"
    data = requests.get(url).json()

    print(f"Coin: {coin}")
    print(f"Cijena: {data['price']}")
    print("-" * 20)
