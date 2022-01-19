from time import sleep

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

bro = Chrome(options=options)
bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

bro.get('http://cpquery.cnipa.gov.cn/')
sleep(5)
bro.implicitly_wait(10)

bro.find_element(By.XPATH, '//input[@id="username1"]').send_keys('15755188511')
bro.find_element(By.XPATH, '//input[@id="password1"]').send_keys('Zhixin888*')

code = bro.find_element(By.XPATH, '//span[@id="selectyzm_text"]')
# 鼠标悬停
ActionChains(bro).move_to_element(code).perform()
sleep(3)

bro.quit()