#encoding=utf-8
import splinter
import selenium
import time
import data

class CT108LoginPage:
    def __init__(self,browser):
        self.browser = browser

    def __visit_url(self):
        self.browser.get(data.CT108_LOGIN_URL)

    def __fill_info(self):
        self.browser.find_element_by_id("username").send_keys(data.CT108_USERNAME)
        self.browser.find_element_by_id("pwd").send_keys(data.CT108_PASSWORD)
        self.browser.find_element_by_id("code").send_keys(data.CT108_YANZHENGMA)

    def login_in(self):
        self.__visit_url()
        self.__fill_info()
        self.browser.find_element_by_id("loginsubmit").click()
    
