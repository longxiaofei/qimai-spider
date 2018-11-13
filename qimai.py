from urllib.parse import quote, urlencode
import requests
import base64
import json
import time

cookies = ""


cookies = {name_value.split('=')[0]: name_value.split('=')[1]
           for name_value in cookies.replace(' ', '').split(';')}
headers = {
    'Referer': 'https://www.qimai.cn/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}

def http_get(url):
    cookie = [{'name': key, 'value': value}
                for key, value in cookies.items()]
    response = requests.get(url, headers=headers, cookies=cookies)
    assert response.status_code == 200
    return response

def object_lh(a):
    e = 'a12c0fa6ab9119bc90e4ac7700796a53'
    t = len(e)
    n = len(a)
    a = list(a)
    for s in range(n):
        a[s] = chr(ord(a[s]) ^ ord(e[s%t]))
    return ''.join(a)

def get_analysis(args):
    o = []
    # diff_time = int(time.time()*1000 - float(cookies['synct'])*1000)
    # print(diff_time)
    t = int(time.time()*1000-1515125653845)
    for value in args.values():
        o.append(value)
    o = ''.join(sorted(o))
    o = quote(o)
    o = base64.b64encode(o.encode()).decode()
    o += "@#" + "/rank/index" + "@#" + str(t) + "@#1"
    o = base64.b64encode(object_lh(o).encode()).decode()
    return o

def get_datas(brand, country, date, device):
    args = {
        "brand": brand,
        "country": country,
        "date": date,
        "device": device,
        "genre": "36"
    }
    cookies['synct'] = format(time.time(), '.3f')
    for page in range(30, 31):
        final_args = args.copy()
        final_args['page'] = str(page)
        analysis = get_analysis(final_args)
        final_args['analysis'] = analysis
        url = 'https://api.qimai.cn/rank/index?' + urlencode(final_args)
        response = http_get(url)
        datas = json.loads(response.text)
        for data in datas['rankInfo']:
            yield data


if __name__ == "__main__":
    """
        :brand; str, free,免费榜  paid,付费榜  grossing,畅销榜
        :country; str, cn,中国; us,美国; tr,土耳其;  ...
        :device; str, ipad or iphone
        :date; str, example, 2018-11-13
    """
    demo = get_datas(brand='free', country='cn', date='2018-11-13', device='iphone')
    for data in demo:
        print(data)

