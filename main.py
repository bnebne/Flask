from flask import Flask, request, abort


app = Flask(__name__)


@app.route("/")
def callback():

    return 'OK'


if __name__ == "__main__":
    app.run()
