
import os
import requests
print("hello from python script")

print(f"{os.environ['GITHUB_TOKEN']}")
#print(f"{os.environ['GH_TOKEN']}")
#print(f"{os.environ['ORGANIZATION']}")
#print(f"{os.environ['REPOSITORY']}")

headers = {
    'Authorization': f"Bearer {os.environ['GITHUB_TOKEN']}"
}

login = requests.get("https://api.github.com/user", headers=headers)
print(login.json())

alerts = requests.get(
    f"https://api.github.com/orgs/{os.environ['ORGANIZATION']}+code-scanning/alerts",
    headers=headers
)
print(alerts.json())