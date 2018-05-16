import requests
from requests.auth import HTTPBasicAuth

# 用于打开网站时需要输入用户名密码的时候
response = requests.get('https://www.baodu.com', auth=HTTPBasicAuth('user','123'))