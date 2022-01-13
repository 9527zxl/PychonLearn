import json

import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }

    pose_url = 'https://fanyi.baidu.com/sug'
    kw = input('请输入翻译内容：')
    data = {
        'kw': kw
    }

    response = requests.post(url=pose_url, data=data,headers=headers)
    obj = response.json()

    name = kw+'.json'
    fp = open(name,'w',encoding='utf-8')
    json.dump(obj,fp=fp,ensure_ascii=False)

    print('翻译结束')