#encoding=utf-8
import time
import splinter

#进入新浪新闻
browser = splinter.Browser()
#url = "http://www.sina.com.cn/"
#browser.visit(url)
#browser.click_link_by_href("http://news.sina.com.cn/")

browser.visit("http://user.uc108.com/register.html")
#最头行
a = browser.document.getElementById("username")
print "a text is : "+ a.text
#if (a.len()>0)
#    print "yes"
#else
#    print "no"
browser.quit()
