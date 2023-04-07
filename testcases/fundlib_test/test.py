import requests
import json

url = "https://www.qcc.com/api/investOrg/getInvestMembers"

payload = json.dumps({"id":"b2eeb7362ef83deff5c7813a67e14f0a","pageIndex":1,"pageSize":10000,"type":1})
headers = {
  '3259e0ef3e0e2d0213f5': 'bc4345c61e551ba93fb39049a30cf266db798819edd1793090d663bb6ff5069f341d014c7504f9ef43d552d40d746c37a2345d76fbdad4725f65c654977cff97',
  'Content-Type': 'application/json',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
  'cookie': 'qcc_did=73a707ef-f1ce-44e6-8622-1f0b31d67449; UM_distinctid=181b22bb81056c-016e0939fd3125-4f617f5b-1fa400-181b22bb811d9; QCCSESSID=436c0e63b644e5bc2b555d66e5; acw_tc=7ae4011416663312964968515e2164c01a2509da87126491159682d9ca; CNZZDATA1254842228=977225361-1656549313-%7C1666330736'
}

response = requests.request("POST", url, headers=headers, data=payload)
datalist = response.json()['Result']
dattttt = []
for i in range(len(datalist)):
  print([datalist[i]['ExecutiveName'], datalist[i]['Position'], datalist[i]['PersonalProfile']])
  # print(datalist)
# print(response.json()['Result'])
# print(dattttt)


