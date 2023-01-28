import requests

js = "https://randomuser.me/api/?results=200&gender=male"

response = requests.get(js)

print(response.status_code)
