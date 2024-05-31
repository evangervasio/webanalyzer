from flask import Flask, render_template, request
from CoinloreApi import CoinloreApi

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    raw_data = None
    coin = ""
    exchange = ""

    # Fetch all exchanges to populate the combobox
    api_caller = CoinloreApi()
    exchanges_data = api_caller.getAllExchanges()

    if request.method == "POST":
        coin = request.form["coin"]
        exchange = request.form["exchange"]

        api_caller = CoinloreApi(coin, exchange)
        raw_data = api_caller.determine()

    #get names to put in comboboxs
    names=[]
    for exc in exchanges_data:
        exchange=(exchanges_data[exc])
        names.append(exchange["name"])

    return render_template("index.html", raw_data=raw_data, exchanges=names)

if __name__ == "__main__":
    app.run(debug=True)