#encoding=utf-8
import splinter
import login
import data
from selenium import webdriver
import time

class Enter:
    def __init__(self,browser):
        self.browser = browser
        login.CT108LoginPage(browser).login_in()

    def enterReimburse(self):
        #self.browser.find_element_by_css_selector[css=a:contains("我要借款")].click()
        self.browser.find_element_by_link_text("我要借款").click()
        time.sleep(5)
