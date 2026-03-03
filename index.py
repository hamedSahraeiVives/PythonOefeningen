from functions import is_even
import requests
response = requests.get("https://api.chucknorris.io/jokes/random")
print(f"statuscode: {response.status_code}")
print(responsetext)
