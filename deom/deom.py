from selenium import webdriver


def driver_object(type_):
    if type_ == 'Chrome':
        driver = webdriver.Chrome()
    elif type_ == 'Firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver


class Key:
    # driver = webdriver.Chrome()

    def url(self, url):
        return self.driver.get(url)

    def __init__(self, type_):
        self.driver = driver_object(type_)
