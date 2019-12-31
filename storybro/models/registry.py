import os
import urllib.request
import json


class ModelRegistry:

    def __init__(self, url):
        self.url = url
        self.models = self.fetch(url)

    def fetch(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        return json.loads(text)

    def refresh(self):
        self.models = self.fetch(self.url)
