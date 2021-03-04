import requests

class PythonAnywhere:
    def __init__(self, token):
        self.headers = { 'Authorization' : f'Token {token}' }
        self.host = 'https://www.pythonanywhere.com'

    def get(self, url):
        response = requests.get(url=f'{self.host}{url}', headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return f'Got unexpected status code {response.status_code}: {response.content}'

    def post(self, url):
        response = requests.post(url=f'{self.host}{url}', headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return f'Got unexpected status code {response.status_code}: {response.content}'