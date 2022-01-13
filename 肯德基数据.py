import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }

    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    name = input('请输入查询关键字：')

    param = {
        'cname': '',
        'pid': '',
        'keyword': name,
        'pageIndex': '1',
        'pageSize': '10',
    }

    response = requests.post(url=url,params=param,headers=headers)
    list_data = response.json()

    nameString = name + '.json'
    fp = open(nameString,'w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    
    print('爬取完成')