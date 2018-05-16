import requests

# requests.get('http://httpbin.org/cookies/set/number/123456')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)

# 保持会话
s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456')
response = s.get('http://httpbin.org/cookies')
print(response.text)