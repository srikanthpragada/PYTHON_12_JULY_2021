import requests

username = 'srikanthpragada'
resp = requests.get(f"https://api.github.com/users/{username}")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(0)

details = resp.json()

for k, v in details.items():
    print(f"{k:20}  {v}")
