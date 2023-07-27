import requests

BASE = "http://127.0.0.1:5000/"

response = requests.delete(BASE + "task/2")

input()

response = requests.put(BASE + "task/2", {"name": "NUTS"})
print(response.json())