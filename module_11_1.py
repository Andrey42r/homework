import requests

r = requests.get('https://ru.m.wikipedia.org/wiki/Дикая_лошадь')
print(r.text)
r.encoding = 'UTF-16'
print(r.text)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('https://ru.m.wikipedia.org/wiki/Дикая_лошадь', data=payload)
print(r.text)


