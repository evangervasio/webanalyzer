from flask import Flask, render_template, request
from CoinloreApi import CoinloreApi

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    api_caller = CoinloreApi()
    exchanges_data = api_caller.getAllExchanges()
    coins_data = api_caller.getAllCoins()
    
    exchange_names = []
    exchange_volumes = []
    coin_names = []

    for exc in exchanges_data:
        exchange = exchanges_data[exc]
        exchange_names.append(exchange["name"])
        exchange_volumes.append(exchange["volume_usd"])
    
    for coin in coins_data:
        coin_names.append({"id": coin["id"], "name": coin["name"]})

    return render_template("index.html", exchanges=exchange_names, coins=coin_names, exchange_names=exchange_names, exchange_volumes=exchange_volumes)

@app.route("/exchange", methods=["POST"])
def exchange():
    coin_id = request.form.get("coin", "")
    exchange_name = request.form["exchange"]
    exchange_id = None

    api_caller = CoinloreApi()

    exchanges_data = api_caller.getAllExchanges()

    for exc in exchanges_data:
        if exchanges_data[exc]["name"] == exchange_name:
            exchange_id = exchanges_data[exc]["id"]
            break

    if exchange_id:
        api_caller = CoinloreApi(coin_id, exchange_id)
        exchange_data = api_caller.getExchange()
        return render_template("exchange.html", exchange_data=exchange_data)
    else:
        return "Exchange not found", 404

@app.route("/coin", methods=["POST"])
def coin():
    coin_id = request.form["coin"]

    api_caller = CoinloreApi(coin=coin_id)
    coin_data = api_caller.getCoin()

    return render_template("coin.html", coin_data=coin_data)

if __name__ == "__main__":
    app.run(debug=True)