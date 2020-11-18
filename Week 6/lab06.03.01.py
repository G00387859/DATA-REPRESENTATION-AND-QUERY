# to use this install package
# pip install PyGithub
from github import Github
import requests

# remove the minus sign from the key
# you can add this to your code just don't commit it
# or use an API key to your own repo
g = Github("783a944b1517ffa7e494820254ce83d83552999-b")

#for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
repo = g.get_repo("G00387859/DATA-REPRESENTATION-AND-QUERYING")
#https://github.com/G00387859/DATA-REPRESENTATION-AND-QUERYING.git
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)
newContents = contentOfFile + " more stuff \n"
#print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)

