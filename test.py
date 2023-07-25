import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "Finish EECS HW!", "month": 7, "day": 23, "year": 2023},
        {"name": "Finish MATH HW!", "month": 8, "day": 24, "year": 2024},
        {"name": "Finish BIO HW!", "month": 2, "day": 28, "year": 2024},
        {"name": "Finish CHEM HW!", "month": 1, "day": 13, "year": 2024},
        {"name": "Finish DEEZ HW!", "month": 1, "day": 3, "year": 2024}]

for i in range(len(data)):
    response = requests.put(BASE + "task/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "task/0")
print(response)
input()
response = requests.get(BASE + "task/2")
print(response.json())