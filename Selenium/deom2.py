from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(
    'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
bro = webdriver.Chrome(options=options)

with open('./js/stealth.min.js') as f:
    source_js = f.read()
bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": source_js
})

bro.get('http://cpquery.cnipa.gov.cn/')
