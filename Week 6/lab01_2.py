import requests
import json
url = 'http://127.0.0.1:5000/cars'
datastring = {'reg': '08 C 1223','make': 'Ford','model':'Galaxy', 'price':2995}  
response = requests.post(url,json=datastring)
#data  =response.json()
print(response.status_code)
