import requests
import json

response = requests.get("http://0.0.0.0:8000/api-authlogin/")
print(response)
print(response.text)
