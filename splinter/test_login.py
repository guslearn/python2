#coding=utf-8
import sys
import splinter

browser = splinter.Browser()

def testLogin(description,username,password,result):
    output(description)
    browser.fill("username",username)
    browser.fill("pwd",password)
    browser.find_by_id("loginsubmit").click()
    checkResult(result)

def output(x):
    print x

def resultMsg(res):
    if res == True:
        print "pass!"
    else:
        print "Not pass!"

def checkResult(x):
    resultMsg(browser.is_text_present(x))

testUrl = "http://user.uc108.com/login.html"
browser.visit(testUrl)
output(browser.title)
#testLogin("123","111","222","333")

#browser.fill("username","abc")
browser.find_link_by_href("/mobile_modify.html").first.click()


