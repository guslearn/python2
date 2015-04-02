#encoding=utf-8
import splinter
import login
import ct_ad

browser = splinter.Browser()
#login.CT108LoginPage(browser).login_in()
#print "sucessed"
ct_ad.Enter(browser).enterAd()
print "ok"
#allItems = browser.find_by_css(".m-nav .nav_second ul li")
#print allItems

