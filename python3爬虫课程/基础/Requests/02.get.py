import requests

# 带参数的get请求
# response = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(response.text)
# 解析 json
# print(response.json())

# 获取二进制数据
# response = requests.get('https://github.com/favicon.ico')
# print(type(response.text))      # str
# print(type(response.content))   # bytes
# 写入到本地
# with open('favicon.ico', 'wb') as f:
#     f.write(response.content)
#     f.close

# 添加headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
response = requests.get('https://www.zhihu.com', headers = headers)
print(response.status_code)
print(response.content)
