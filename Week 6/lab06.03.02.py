# to use this install package
# pip install PyGithub
from github import Github
import requests

# remove the minus sign from the key
# you can add this to your code just don't commit it
# or use an API key to your own repo
g = Github("7eb000919dc24cf384febc15e7220ad4eefa4d9-9")

#for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
repo = g.get_repo("G00387859/DATA-REPRESENTATION-AND-QUERYING")
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)
##response = requests.get(urlOfFile)
contentOfFile = requests.get(urlOfFile).text
#print (contentOfFile)
newContents = contentOfFile + " more stuff \n"
#print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)