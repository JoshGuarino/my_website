import requests

class Api:
    def __init__(self, key, url):
        self.key = None
        self.url = None

    def get():
        try:
            response = requests.get()
            return
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    
    def post():
        try:
            response = requests.post()
            return
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)    
        