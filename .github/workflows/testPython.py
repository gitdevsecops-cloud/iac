
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

def createIssue(alert_number, alert, owner, repo):
    # Create an issue
    print(f"creating alert for {alert_number, alert, owner, repo}")
    body = {
        "title": f"{alert_number} {alert.get('id')}",
        "body": f"issue issue"
    }

    issue = requests.post(
        url=f"https://api.github.com/repos/{owner}/{repo}/issues",
        data= body,
        headers=headers
    )
    print(f"Status code for issue is {issue.status_code}")
    return issue.status_code 

"""
print(f"header is {headers}")

print(f"Url is https://api.github.com/orgs/{os.environ['ORGANIZATION']}/code-scanning/alerts")

"""


alerts = requests.get(
    f"https://api.github.com/orgs/{os.environ['ORGANIZATION']}/code-scanning/alerts",
    headers=headers
)

for alert in alerts.json():
   # print(alert.get('number'))
   # print(alert.get('rule'))
   print(f"{type(alert.get('number'))}")

   if int(alert.get('number')) == 48:
        print("creating issue")
        createIssue("48", alert.get('rule'),os.environ['OWNER'],os.environ['REPOSITORY'] )

