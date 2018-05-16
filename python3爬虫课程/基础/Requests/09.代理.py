import requests

proxies={'http':'http://127.0.0.1:9743',
'http':'https://127.0.0.1:9744',}

# 有密码的代理如何传入呢？添加user:password@
# 举个例子:'http':http://user:password@127.0.0.1:9743',

r=requests.get('https://www.taobao.com',proxies=proxies)
print(r.status_code)