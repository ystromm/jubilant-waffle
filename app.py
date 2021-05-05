import os

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    search = requests.get("https://api.thecatapi.com/v1/images/search").json()
    print(search)
    url = search[0]["url"]
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))