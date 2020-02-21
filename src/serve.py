import requests

url = 'http://127.0.0.2:3000/'

params = {'data': '5.,3.,2.,1.,3.,1.,1.,1.,1.'}

response = requests.get(url, params)
print(response.json())
