#encoding=utf-8
import splinter
from selenium import webdriver
import login
import ct_ad

browser = webdriver.Firefox()
#login.CT108LoginPage(browser).login_in()
#print "sucessed"
ct_ad.Enter(browser).enterReimburse()
print "ok"
browser.quit()

