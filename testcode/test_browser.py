#encoding=utf-8
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

url = "http://www.baidu.com"

browser = webdriver.Firefox()

#1.基础操作
#browser.get(url)
#time.sleep(2)
#print "浏览器最大化"
#browser.maximize_window()
#time.sleep(2)
#print "设置浏览器宽480,高800显示"
#browser.set_window_size(480,800)
#time.sleep(5)
#assert u"百度" in browser.title
#一般的send_keys()方法在/usr/local/lib/python2.7/dist-packages/selenium/webdriver/support下
#browser.find_element_by_id("kw").send_keys("selenium")
#browser.find_element_by_id("su").click()
#time.sleep(3)
#print browser.title

#browser.get("http://selenium-python.readthedocs.org")
#elem = browser.find_element_by_name("q")
#elem.send_keys("pycon")
#elem.send_keys(keys.RETURN)
#assert "No results found." not in browser.page_source
#browser.close()
#browser.quit()



#2.checkbox定位
"""
file_path = "file:///" + os.path.abspath('checkbox.html')
browser.get(file_path)
#方法一
#选择页面上所有到input，然后从中过滤出所有到checkbox，并勾选
inputs = browser.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        print("1")
        input.click()
time.sleep(2)

#方法二
checkboxes = browser.find_elements_by_css_selector("input[type=checkbox]")
#for checkbox in checkboxes:
#    checkbox.click()
checkboxes.submit()
time.sleep(2)
#打印checkbox数量
print len(checkboxes)

browser.quit()
"""

#3.xpath定位

file_path3 = "file:///" + os.path.abspath('xpath_test1.html')
browser.get(file_path3)
xpaths1 = browser.find_elements_by_xpath("//catalog/cd/price")
print "xpaths1's len is : " + str(len(xpaths1))

xpaths2 = browser.find_elements_by_xpath("//cd")
print "xpaths2's len is : " + str(len(xpaths2))

xpaths3 = browser.find_elements_by_xpath("//catalog/cd/*")
#xpaths3x = browser.find_element_by_xpath("/catalog/cd/*")
print "xpaths3's len is : " + str(len(xpaths3))
#print "xpaths3x's len is : " + str(len(xpaths3x))

xpaths4 = browser.find_elements_by_xpath("//catalog/*/price")
print "xpaths4's len is : " + str(len(xpaths4))

xpaths5 = browser.find_elements_by_xpath("//*/*/price")
print "xpaths5's len is : " + str(len(xpaths5))

xpaths6 = browser.find_elements_by_xpath("//*")
print "xpaths6's len is : " + str(len(xpaths6))

#从catalog的子元素中取出第一个叫做cd的元素
xpaths7 = browser.find_elements_by_xpath("//catalog/cd[1]")
print "xpaths7's len is : " + str(len(xpaths7))

#选择catalog中的最后一个cd元素
xpaths8 = browser.find_elements_by_xpath("//catalog/cd[last()]")
print "xpaths8's len is : " + str(len(xpaths8))

#选出含有price子元素的所有/catalog/cd元素
xpaths9 = browser.find_elements_by_xpath("//catalog/cd[price]")
#xpaths9 = browser.find_elements_by_xpath("//catalog/cd/price/*")--不可取，因为/catalog/cd/下不一定以price子元素第一个开头
for xpath9 in xpaths9:
    print xpath9.text
print "xpaths9's len is : " + str(len(xpaths9))

#选出price元素的值等于10.90的所有/catalog/cd元素
xpaths10 = browser.find_elements_by_xpath("//catalog/cd[price=10.90]")
print "xpaths10's len is : " + str(len(xpaths10))

#选出price元素的值等于10.90的所有/catalog/cd元素的price元素
xpaths11 = browser.find_elements_by_xpath("//catalog/cd[price=10.90]/price")
print "xpaths11's len is : " + str(len(xpaths11))

xpaths12 = browser.find_elements_by_xpath("//catalog/cd/title | //catalog/cd/artist")
for xpath12 in xpaths12:
    print xpath12.text
print "xpaths12's len is : " + str(len(xpaths12))

#选择所有title以及artist元素
xpaths13 = browser.find_elements_by_xpath("//title | //artist")
for xpath13 in xpaths13:
    print xpath13.text
print "xpaths13's len is : " + str(len(xpaths13))

#选择文件中所有叫做country的属性???有问题啊！！！！！！
xpaths14 = browser.find_elements_by_xpath("//@country")
print "xpaths14's len is : " + str(len(xpaths14))

#选择所有含有country这个属性的cd元素
xpaths15 = browser.find_elements_by_xpath("//cd[@country]")
print "xpaths15's len is : " + str(len(xpaths15))





browser.quit()





