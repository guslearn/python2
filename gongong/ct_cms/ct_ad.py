#encoding=utf-8
import splinter
import login
import data

class Enter:
    def __init__(self,browser):
        self.browser = browser
        login.CT108LoginPage(browser).login_in()

    def enterReimburse(self):
#        reimburse = self.browser.find_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[2]/ul/li[1]/a/span[@class='mm-text']")

        #reimburse = self.browser.find_by_xpath("/html/body/div[1]/div[2]/div/div[1]/ul/li[2]/a[@class='mm-text mmc-dropdown-delay animated fadeIn']")
        self.browser.find_by_xpath("/html/body/div[1]/div[2]/div/div[1]/ul[@class='navigation']/li[2]/a/span").click()
        #re1 = reimburse.find_by_class("navigation")
        #self.browser.find_by_xpath("/html/body/div[1]/div[2]/div/div[1]/ul/li[2]/a").first.click()
        print reimburse
