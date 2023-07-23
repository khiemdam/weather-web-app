import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "task/0", {"name": "Finish EECS HW!",
                                          "month": 7,
                                          "day": 23,
                                          "year": 2023})
print(response.json())
input()
response = requests.get(BASE + "task/0")
print(response.json())