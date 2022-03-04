from flask import Flask, request    # From the flask module import the Flask class.
from datetime import datetime
app = Flask(__name__)               # Instantiating the Flask class into the app variable

PHONEBOOK = {
    "Kvon": {
        "last_name": "Smith",
        "numbers": [
            "956-956-9569",
            "000-000-0000",
        ],
    },
    "John": {
        "last_name": "Doe",
        "numbers": [
            "111-111-1111",
            "222-222-2222",
        ],
    },
    "Jane": {
        "last_name": "Doe",
        "numbers": [
            "333-333-3333",
        ],

    },
}

HOMEWORK = {
    "About":{
        "first_name": "Kvon",
        "last_name": "Smith",
        "hobby": "Note Investing",
    },
}

@app.route("/")                     # The "route" decorator.
def index():                        # the wrapped function                      
    return"<h1>Kvon Smith</h1>"   # the return statement

@app.route("/version")
def get_version():
    timestamp = datetime.now().strftime("%F %H:%M:%S")
    out = {
        "version": "1.0.0",
        "server_time": timestamp,
        "ok": True
        }
    return out

@app.route("/numbers/<name>")
def get_numbers(name):
    out = PHONEBOOK.get(name)
    return out

@app.route("/numbers")
def get_all_numbers():
    return PHONEBOOK

@app.route("/numbers", methods=["POST"])
def add_number():
    number = request.json
    PHONEBOOK[number.get("name")] = number["data"]
    return "OK", 204

@app.route("/homework")
def get_homework():
    return HOMEWORK
