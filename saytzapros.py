import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.headers, 'headers')
print(response.status_code, 'status_code')
print(response.request, 'request')