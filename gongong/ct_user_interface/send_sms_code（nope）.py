#ecoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import login


url_send_sms_code = data.url_send_sms_code
cookie = cookielib.CookieJar()
login1 = login.Login()
#login1.login_by_username()
cookie = login1._cookie
userid = login1._userid
hardinfo = login1._hardinfo

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

value1 = {"verifyData":{"userID":userid,"userIP":"192.168.1.1","HardInfo":hardinfo},"newPassword":"qweasd","appid":31}
data1 = json.dumps(value1)
req1 = urllib2.Request(url_update_password,data1, {'Content-Type': 'application/json'})
#response1 = urllib2.urlopen(req1)
response1 = opener.open(req1)
response_read1 = response1.read()
res1 = json.loads(response_read1)
if res1["StatusCode"] == 0:
    print response_read1
    print login1._username
    print login1._userpwd
else:
    print "Response failed!"
    print res1["Message"]

'''
testurl = "http://usersvc.ct108.org:1904/test/GetRegSmsCode.aspx?mobile=13112340204"
req3 = urllib2.Request(testurl)
response3 = urllib2.urlopen(req3)
print response3.read()
'''



