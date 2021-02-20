

import requests
outcome=requests.get('http://www.baidu.com')
print(outcome)
outcome.encoding = 'utf-8'
content = outcome.text
print(content)

while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)



    dcity = req.json()
    print(dcity)

    dcityd=dcity.get('data')
    if dcityd:
     cityfore = dcityd['forecast'][1]
     print(cityfore.get('date'))
     print(cityfore.get('high'))
     print(cityfore.get('low'))
     print(cityfore.get('type'))
     print(cityfore.get('fengxiang'))
     print(cityfore.get('fengli'))
    else:
      print('NONE')