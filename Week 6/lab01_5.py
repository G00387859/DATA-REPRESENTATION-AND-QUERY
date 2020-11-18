import requests
import json
from xlwt import *
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
filename = 'githubusers.json'
print(data)
for car in data:
    print(car)
#write the Json to a file.
#import json
if filename:
    with open(filename, 'w') as f:
        json.dump(data,f,indent=4)
w = Workbook()
ws = w.add_sheet('githubusers')
row = 0
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
ws.write(row,4,"gravatar_id")
ws.write(row,5,"url")
ws.write(row,6,"html_url")
ws.write(row,7,"followers_url")
ws.write(row,8,"gists_url")
ws.write(row,9,"starred_url")
ws.write(row,10,"subscriptions_url")
ws.write(row,11,"organizations_url")
ws.write(row,12,"repos_url")
ws.write(row,13,"events_url")
ws.write(row,14,"received_events_url")
ws.write(row,15,"type")
ws.write(row,16,"site_admin")
row +=1
for car in data:
    ws.write(row,0,car["login"])
    ws.write(row,1,car["id"])
    ws.write(row,2,car["node_id"])
    ws.write(row,3,car["avatar_url"])
    ws.write(row,4,car["gravatar_id"])
    ws.write(row,5,car["url"])
    ws.write(row,6,car["html_url"])
    ws.write(row,7,car["followers_url"])
    ws.write(row,8,car["gists_url"])
    ws.write(row,9,car["starred_url"])
    ws.write(row,10,car["subscriptions_url"])
    ws.write(row,11,car["organizations_url"])
    ws.write(row,12,car["repos_url"])
    ws.write(row,13,car["events_url"])
    ws.write(row,14,car["received_events_url"])
    ws.write(row,15,car["type"])
    ws.write(row,16,car["site_admin"])

    row +=1
w.save('githubusers.xls')

print(response.status_code)
print(response.text)