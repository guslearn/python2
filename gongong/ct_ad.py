#encoding=utf-8
import splinter
import login
import data

class Enter:
    def __init__(self,browser):
        self.browser = browser
        login.CT108LoginPage(browser).login_in()

    def findAllItems(self):
       allItems = self.browser.find_by_css(".m-nav .nav_second ul li")
       return allItems

    def enterAd(self):
        items = self.findAllItems();
        ads = items.find_by_css(".m-nav .all_column .detail .il a")
        ad = ads.find_by_css(data.CT108_ADS)
        print len(ad)
        #for ad_text in (ads.text):
            #if ad_text == u"畅唐广告":
             #   ad_text.click()
              #  break
           # break
