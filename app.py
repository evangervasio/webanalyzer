from flask import Flask, render_template, request
from CoinloreApi import CoinloreApi

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    api_caller = CoinloreApi()
    exchanges_data = api_caller.getAllExchanges()
    coins_data = api_caller.getAllCoins()
    
    exchange_names = []
    coin_names = []

    for exc in exchanges_data:
        exchange = exchanges_data[exc]
        exchange_names.append(exchange["name"])
    
    for coin in coins_data:
        coin_names.append({"id": coin["id"], "name": coin["name"]})

    return render_template("index.html", exchanges=exchange_names, coins=coin_names)

@app.route("/exchange", methods=["POST"])
def exchange():
    coin_id = request.form["coin"]
    exchange_name = request.form["exchange"]
    exchange_id = None

    api_caller = CoinloreApi()

    # Fetch all exchanges to find the selected one by name
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

if __name__ == "__main__":
    app.run(debug=True)