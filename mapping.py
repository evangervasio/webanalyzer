from flask import Flask, render_template, request
from SimilarApi import SimilarApi

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    raw_data = None
    if request.method == "POST":
        website = request.form["website"]
        api_caller = SimilarApi(website)
        raw_data = api_caller.call_api_once()
    return render_template("index.html", raw_data=raw_data)

if __name__ == "__main__":
    app.run(debug=True)
