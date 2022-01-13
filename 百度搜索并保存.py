import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55'
    }

    url = 'https://www.baidu.com/s'
    kw = input('输入搜索内容:')
    param = {
        'wd': kw
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text

    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName, '保存成功')
