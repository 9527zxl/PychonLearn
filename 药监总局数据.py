import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    id_list = []
    all_data_list = []

    pagination = int(input('请输入爬取的那一页数：'))

    param = {
        'on': 'true',
        'page': pagination,
        'pageSize': 15,
        'productName': '',
        'conditionType': 1,
        'applyname': '',
        'applysn': '',
    }

    page_data = requests.post(url=url, params=param, headers=headers).json()

    for id in page_data['list']:
        id_list.append(id['ID'])

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for p_id in id_list:
        data = {
            'id': p_id
        }
        data_json = requests.post(url=post_url,data=data,headers=headers).json()
        all_data_list.append(data_json)

    fp = open('./aa.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('爬取完成')