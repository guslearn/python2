#encoding=utf-8
import splinter

#初始化
browser = splinter.Browser()

#赋值
url = "http://user.uc108.com/register.html?gourl=http://hz.uc108.com/"
browser.visit(url)
username = "ttteeessstes1"
password = "1q2w3e"
idcard = "230722198510063374"
truename = u"葛唐朱"

browser.find_by_id("username").fill(username)
browser.find_by_id("pwd").fill(password)
browser.find_by_id("pwdRepeat").fill(password)
browser.find_by_name("IDCard").fill(idcard)
#browser.find_by_name("TrueName").fill(truename.decode('utf-8').encode('gbk'))
browser.find_by_name("TrueName").fill(truename)

#if (browser.find_by_id("code")):
inputcode = raw_input("请输入验证码： ")

browser.find_by_id("code").fill(inputcode)
browser.find_by_id("submit").click()



