from flask import Flask
import os

app = Flask(__name__)


@app.route("/members")

def members():

    return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":

    #app.run(debug=True)
    app.run(debug="True", host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))