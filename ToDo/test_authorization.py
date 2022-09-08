import requests
from requests.auth import HTTPBasicAuth


# auth = HTTPBasicAuth(username='admin', password='admin')
# response = requests.get('http://127.0.0.1:8000/api/project/', auth=auth)
# print(response.json())
#
# data = {'username': 'admin', 'password': 'admin'}
# response = requests.post('http://127.0.0.1:8000/api-token-auth/', data=data)
# token = response.json().get('token')
# response_project = requests.get('http://127.0.0.1:8000/api/project/', headers={'Authorization': f'Token {token}'})
# print(response_project.json())

headers = {'Accept': 'application/json; version=v2'}
response = requests.get('http://127.0.0.1:8000/api/users/', headers=headers)
print(response.json())
