import os
import urllib.request
import json

def fetch_model_registry(registry):
    response = urllib.request.urlopen(registry)
    data = response.read()
    text = data.decode('utf-8')
    return json.loads(text)
