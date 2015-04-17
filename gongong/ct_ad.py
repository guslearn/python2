#encoding=utf-8
import splinter
import login
import data

class Enter:
    def __init__(self,browser):
        self.browser = browser
        login.CT108LoginPage(browser).login_in()

    def find_all_items(self):
       #allItems = self.browser.find_by_css(".m-nav .nav_second ul li")
       all_items = self.browser.find_by_css(data.CT108_ALLITEMS)
       return all_items
    
    def find_ad(self):
        items = self.find_all_items();
        items.mouse_over()
        print "items text : " + items.text
        t0 = self.browser.find_by_css(".m-nav .all_column .detail .wu")#所有内容
        t = t0.find_by_css(".m-nav .all_column .detail .il")
        tt = t.find_by_css(".m-nav .all_column .detail .tp")
        print "tt text : " + tt.text
        for ttt in tt:
            if ttt.text == u"广告":
                print "ttt text : " + ttt.text
                ttt.click()
        ads = self.browser.find_link_by_href("http://tcmm.admin.ct108.org:802/Default.aspx")
        ads.click()
       # gg = self.browser.find_by_css(".m-nav .all_column .detail .il a")
        gg = self.browser.find_by_css("v .nav_second ul liv .nav_second ul li")
        print "gg text : " + str(gg) 
        #return ads

    def enter_ad(self):
        #items = self.find_all_items();
        #items.mouse_over()
        #print "items text : " + items.text
        #ad = items.find_by_css(data.CT108_ADS)
        self.find_ad()
        #print "the length of ad is : " + str(len(ad))
        #print "ad text is : " + ad.text
        #print "ad-----" + str(ad)
        
        #ad.click()
        #gg = ad.find_by_css(".m-nav .all_column .detail .il a")
        #print "gg : " + str(gg)

        #for ad_text in (ads.text):
            #if ad_text == u"畅唐广告":
             #   ad_text.click()
              #  break
           # break
