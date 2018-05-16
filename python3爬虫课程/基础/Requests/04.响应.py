import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

response = requests.get('http://www.jianshu.com', headers=headers)
print (type(response.status_code), response.status_code)
print ('----------------------------------------------')
print (type(response.headers), response.headers)
print ('----------------------------------------------')
print (type(response.cookies), response.cookies)
print ('----------------------------------------------')
print (type(response.url), response.url)
print ('----------------------------------------------')
print (type(response.history), response.history)
print ('----------------------------------------------')