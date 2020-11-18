import requests
import json
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
filename = 'githubusers.json'
with open(filename, 'w')as f:
    json.dump(data, f,indent=4)
print(response.status_code)
print(response.text)