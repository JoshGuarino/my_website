import requests

class GraphQL:
    def __init__(self, token, url):
        self.headers = { 'Authorization' : f'token  {token}' }
        self.url = url
        self.query = None

    def get(self, query):
        self.query = { 'query' : query }\
        response = requests.get(url=self.url, json=self.query, headers=self.headers)
        if response.status_code == 200:
            return response.json
        return f'Got unexpected status code {response.status_code}: {response.content}'

    def post(self, query):
        self.query = { 'query' : query }
        response = requests.post(url=self.url, json=self.query, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return f'Got unexpected status code {response.status_code}: {response.content}'