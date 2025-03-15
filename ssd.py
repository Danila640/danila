
import requests

response = requests.get('https://www.kapitalbank.az/ru')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error -", response.status_code)
