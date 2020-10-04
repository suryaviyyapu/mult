import requests
from utils.colors import *

def check_network():
    print("%s Checking for network%s"% (info, end))
    URL = "http://google.com"
    req = requests.get(URL)
    print("Recieved " + str(req.status_code) + " from " + URL)
