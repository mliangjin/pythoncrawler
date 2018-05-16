import requests
from requests.exceptions import ReadTimeout

try:
    response = requests.get('https://www.zhihu.com', timeout=1)
    print (response.status_code)
except ReadTimeout:
    print('readTimeout')