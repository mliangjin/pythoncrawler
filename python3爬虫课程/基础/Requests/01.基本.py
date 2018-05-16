import requests

response = requests.get('https://www.baidu.com')
print (type(response))
print (response)

# 请求状态码
print ('--------------------------------------')
print (response.status_code)

# 请求返回的html文本 str类型
print ('--------------------------------------')
print (type(response.text))
print (response.text) 

# cookies
print ('--------------------------------------')
print (requests.cookies)
