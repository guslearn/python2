#ecoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import login


url_update_username = data.url_update_username
cookie = cookielib.CookieJar()
login1 = login.Login()
cookie = login1._cookie
oldname = login1._username
userid = login1._userid

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

value1 = {"UserID":userid,"OldUserName":oldname,"NewUserName":"utesdadfsa1"}
data1 = json.dumps(value1)
req1 = urllib2.Request(url_update_username,data1, {'Content-Type': 'application/json'})
print 1
print type(req1)
#response1 = urllib2.urlopen(req1)
response1 = opener.open(req1)
print 2
print type(response1)
response_read1 = response1.read()
res1 = json.loads(response_read1)
if res1["StatusCode"] == 0:
    print response_read1
else:
    print "Response failed!"

'''
testurl = "http://usersvc.ct108.org:1904/test/GetRegSmsCode.aspx?mobile=13112340204"
req3 = urllib2.Request(testurl)
response3 = urllib2.urlopen(req3)
print response3.read()
'''



