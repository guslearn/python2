#encoding=utf-8
from selenium import webdriver
#import xpath_test1.html

driver = webdriver.Firefox()
file_path = "file:///" + os.path.abspath('xpath_test1.html')
driver.get(file_path)


