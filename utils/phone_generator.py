import requests
from random import choice, randint

URL = "http://127.0.0.1:5000/numbers"
names = ["Jack", "Jill", "Tom", "Mark", "Sally", "Jorge"]
last_names = ["Ford", "Jackson", "Hughes", "Martinez", "Wu"]

def post_random_number():
    number = {}
    number["name"] = choice(names)
    number["data"] = {
        "last_name": choice(last_names),
        "numbers": [
            "333-333-%s%s%s%s" % (
                randint(1, 9), randint(1, 9),
                randint(1, 9), randint(1,9)
            )
        ]
    }
    response = requests.post(URL, json=number)
    if response.status_code == 204:
        print("OK")
    else:
        print("Something went wrong.")

if __name__ == "__main__":
    for _ in range(5):
        post_random_number()