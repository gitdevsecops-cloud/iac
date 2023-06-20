
import os
import requests
print("hello from python script")

print(f"{os.environ['GITHUB_TOKEN']}")
#print(f"{os.environ['GH_TOKEN']}")
#print(f"{os.environ['ORGANIZATION']}")
#print(f"{os.environ['REPOSITORY']}")

headers = {
    'Authorization': 'Bearer '+os.environ['GITHUB_TOKEN'] 
}

login = requests.get("https://api.github.com/user", headers=headers)
print(login.json())