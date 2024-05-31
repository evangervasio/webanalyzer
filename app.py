from flask import Flask, render_template, request
from CoinloreApi import CoinloreApi

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    raw_data = None
    if request.method == "POST":
        coin = request.form["coin"]
        exchange = request.form["exchange"]

        api_caller = CoinloreApi(coin,exchange)
        raw_data = api_caller.determine()
    return render_template("index.html", raw_data=raw_data)

if __name__ == "__main__":
    app.run(debug=True)
