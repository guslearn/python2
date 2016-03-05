#ecoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import login


url_update_username_and_password = data.url_update_username_and_password
cookie = cookielib.CookieJar()
login1 = login.Login()
#login1.login_by_username()
cookie = login1._cookie
oldname = login1._username
userid = login1._userid

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

value1 = {"UserID":userid,"NewUserName":"utesdadfsa7","NewPassword":"qweasd","verifyData":{"HardInfo":data.Mobile_Hard_Info},"AppId":31}
data1 = json.dumps(value1)
req1 = urllib2.Request(url_update_username_and_password,data1, {'Content-Type': 'application/json'})
#response1 = urllib2.urlopen(req1)
response1 = opener.open(req1)
response_read1 = response1.read()
res1 = json.loads(response_read1)
if res1["StatusCode"] == 0:
    print response_read1
else:
    print "Response failed!"
    print res1["Message"]



