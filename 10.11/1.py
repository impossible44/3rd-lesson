import requests

#response=requests.get('https://jsonplaceholder.typicode.com/posts/18')
#print(f"status code: {response.status_code}")
#print(f"Text answ: {response.text}")

#data=response.json()
#print(f"Заголовок поста: {data['title']}")

#payload={'user': 'ivan', 'age': 25}
#response=requests.get('https://httplein.org/get', params=payload)
#print(response.url)
#print(response.text)

url='https://httpbin.org/post'
payload_json={'title': 'foo', 'body': 'bar', 'userId':18}
response=requests.post(url, json=payload_json)
print(f"responce text: {response.text}")

payload_form={'username': 'admin', 'password': 'secret'}
response2=requests.post(url, data=payload_form)
print(f"responce text: {response2.text}")