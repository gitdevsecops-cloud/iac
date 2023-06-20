
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

print(f"header is {headers}")

print(f"Url is https://api.github.com/orgs/{os.environ['ORGANIZATION']}/code-scanning/alerts")

alerts = requests.get(
    f"https://api.github.com/orgs/{os.environ['ORGANIZATION']}/code-scanning/alerts",
    headers=headers
)

for alert in alerts.json():
    print(alert.get('number'))
    print(alert.get('rule'))