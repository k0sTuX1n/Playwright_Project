import requests

class ApiClient:
    

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def get(self, url):
        return requests.get(self.base_url + url)

    def post(self, url, data):
        return requests.post(url, json=data)

    def put(self, url, data):
        return requests.put(url, json=data)

    def patch(self, url, data):
        return requests.patch(url, json=data)

    def delete(self, url):
        return requests.delete(url)