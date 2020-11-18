import requests
import json
url = 'http://127.0.0.1:5000/cars/test'
datastring = {'make': 'Ford','model':'Kuga'}  
response = requests.put(url,json=datastring)
#data  =response.json()
print(response.status_code)
print(response.text)
