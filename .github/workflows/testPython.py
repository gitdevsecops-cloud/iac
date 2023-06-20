from github import AccessToken
import github
import os
print("hello from python script")

print(f"{os.environ['GITHUB_TOKEN']}")
print(f"{os.environ['GH_TOKEN']}")
print(f"{os.environ['ORGANIZATION']}")
print(f"{os.environ['REPOSITORY']}")

from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("access_token")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)