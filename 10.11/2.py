import requests

headerz={
    'User-Agent': 'MyAwesomeUserAgent/1.0', 'Authorization': 'Bearer Token'
}

response = requests.get('https://api.github.com/user', headers=headerz)

print(f"{response.status_code}")
print(f"{response.text}")