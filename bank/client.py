import requests

url = "http://159.223.233.145/transfer"


class Client:

    def __init__(self):
        pass

    def post(self, json):
        return requests.post(url, json)
