#encoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import login


url_current_user = data.url_current_user
cookie = cookielib.CookieJar()
login1 = login.Login()
login1.login_by_username()
#cookie = login1.login_by_username()
cookie = login1._cookie

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

value1 = {"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""}}
data1 = json.dumps(value1)
req1 = urllib2.Request(url_current_user,data1, {'Content-Type': 'application/json'})
#response1 = urllib2.urlopen(req1)
response1 = opener.open(req1)
response_read1 = response1.read()
res1 = json.loads(response_read1)
if res1["StatusCode"] == 0:
    print response_read1
else:
    print "Response failed!"

print "22222222222222222222"
value2 = {"UserID":login1._userid,"OldUserName":login1._username,"NewUserName":"utesdadfsa4"}
data2 = json.dumps(value2)
req2 = urllib2.Request(data.url_update_username,data2, {'Content-Type': 'application/json'})
print 1
print type(req2)
#response1 = urllib2.urlopen(req1)
response2 = opener.open(req2)
print 2
print type(response2)
response_read2 = response2.read()
res2 = json.loads(response_read2)
if res1["StatusCode"] == 0:
    print response_read2
else:
    print "Response 2 failed!"


'''
testurl = "http://usersvc.ct108.org:1904/test/GetRegSmsCode.aspx?mobile=13112340204"
req3 = urllib2.Request(testurl)
response3 = urllib2.urlopen(req3)
print response3.read()
'''



