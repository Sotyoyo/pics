import time
import execjs
import requests

url = 'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'

with open('./tao_day1.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
# mcode = execjs.compile(jscode).call('getResCode') + '111'
mcode = execjs.compile(jscode).call('getResCode')
print(mcode)

headers = {
    'Cookie':
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1655284381; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1655286218',
    'Host': 'webapi.cninfo.com.cn',
    'mcode': mcode,
    'Origin': 'http://webapi.cninfo.com.cn',
    'Referer': 'http://webapi.cninfo.com.cn/',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

data = {'tdate': '2022-06-14', 'market': 'SZE'}

res = requests.post(url=url, headers=headers, data=data).text
print(res)
