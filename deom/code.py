from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://passport.bilibili.com/login?from_spm_id=333.937.top_bar.login')
