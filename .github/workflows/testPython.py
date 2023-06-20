from github import Auth
import github
import os
print("hello from python script")

print(f"{os.environ['GITHUB_TOKEN']}")
print(f"{os.environ['GH_TOKEN']}")
print(f"{os.environ['ORGANIZATION']}")
print(f"{os.environ['REPOSITORY']}")

auth = Auth.Token(os.environ['GITHUB_TOKEN'])
g = github(auth= auth)
print(g.get_user().login)