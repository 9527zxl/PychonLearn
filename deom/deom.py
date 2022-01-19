from selenium import webdriver
from selenium.webdriver.common.by import By


class key:
    driver = webdriver.Chrome()

    def geturl(self, url):
        return self.driver.get(url)

    def account(self, account):
        return self.driver.find_element(By.XPATH, '//input[@id="username1"]').send_keys(account)

    def password(self, password):
        return self.driver.find_element(By.XPATH, '//input[@id="password1"]').send_keys(password)
