import requests

payloads = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data = payloads)

print r.text