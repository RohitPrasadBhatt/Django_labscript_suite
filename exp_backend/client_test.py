import json
import requests

payload = {'idle_time': 1 }
url="http://127.0.0.1:8000/upload/"
r = requests.post(url, data={'json':json.dumps(payload)})
