import requests
url = 'http://127.0.0.1:5000/cars'
data = {'reg':'12D345','make':'maysley','model': 'minor','price':12234}
    
response = requests.post(url,json=data)
print(response.status_code)
print(response.json())