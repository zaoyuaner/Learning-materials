import requests
#from requests.auth import HTTPBasicAuth
auth= ("admin","123456")
response = requests.get("https://api.github.com/user",auth=auth)
print(response.text)