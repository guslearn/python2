#encoding=utf-8
import time
import splinter

#进入新浪新闻
browser = splinter.Browser()
#url = "http://www.sina.com.cn/"
#browser.visit(url)
#browser.click_link_by_href("http://news.sina.com.cn/")

browser.visit("http://news.sina.com.cn/")
#最头行
a = browser.find_by_id("blk_cheadTopbar_01")
atr = a.text.encode('utf-8')
print "the astr type : " +  str(type(atr))
print atr.split(" ")
browser.quit()
