from flask import Flask, render_template
from SimilarApi import SimilarApi
app=Flask(__name__)

@app.route("/")
def home():
    api_caller=SimilarApi("http://google.com")
    api_caller.call_api_repeatedly()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)