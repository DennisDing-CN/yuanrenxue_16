import requests
import execjs

with open('16.js', 'r', encoding='utf-8') as f:
    line = f.read()

key = execjs.compile(line).call('get_m')

cookies = {
    'sessionid': 'mts009d0m3p7jlwlablq9w7ysukj5p22',
}
headers = {
    'user-agent': 'yuanrenxue.project',
}
sum = 0
for i in range(1, 6):
    params = {
        'page': str(i),
        'm': key['m'],
        't': key['t'],
    }

    response = requests.get('https://match.yuanrenxue.com/api/match/16', params=params, cookies=cookies, headers=headers).json()
    print(response)
    for i in response['data']:
        sum += int(i['value'])
print(sum)
