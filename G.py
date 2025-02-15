'''
import requests

response = https://fake-json-api.mock.beeceptor.com/users')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error -", response.status_code)
'''
import requests
import inspect

print(inspect.ismodule(requests.get))
print(inspect.isclass(requests.get))
print(inspect.isfunction(requests.get))