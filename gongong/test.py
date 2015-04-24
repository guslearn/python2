#encoding=utf-8
import splinter
import login
import ct_ad

browser = splinter.Browser()
#login.CT108LoginPage(browser).login_in()
#print "sucessed"
ct_ad.Enter(browser).enter_ad()
print "ok"
browser.quit()

