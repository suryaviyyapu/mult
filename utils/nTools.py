import requests


def check_network():
    URL = "http://google.com"
    req = requests.get(URL)
    print("Recieved " + str(req.status_code) + " from " + URL)
