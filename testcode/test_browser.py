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
file_path = "file:///" + os.path.abspath('checkbox.html')
browser.get(file_path)
#选择页面上所有到input，然后从中过滤出所有到checkbox，并勾选
inputs = browser.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute('ttype') == 'checkbox':
        input.click()
time.sleep(2)

browser.quit()



