import os
print("hello from python script")

print(f"{os.environ['GITHUB_TOKEN']}")
print(f"{os.environ['GH_TOKEN']}")
print(f"{os.environ['ORGANIZATION']}")
print(f"{os.environ['REPOSITORY']}")

