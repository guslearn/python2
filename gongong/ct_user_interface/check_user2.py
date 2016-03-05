import urllib2
import json
import cookielib
import data


url_check_user2 = data.url_check_user2
#cookie = cookielib.CookieJar()
#login1 = login.Login()
#login1.login_by_username()
#cookie = login1.login_by_username()
#cookie = login1._cookie

#handler = urllib2.HTTPCookieProcessor(cookie)
#opener = urllib2.build_opener(handler)


class CheckUser2:
    _username = ""
    def __init__(self,username):
        self._username = username
        #print self._username
        self.check_user2()

    def check_user2(self):
        value1 = {"username":self._username,"MobileHardInfo":data.Mobile_Hard_Info}
        data1 = json.dumps(value1)
        req1 = urllib2.Request(url_check_user2,data1, {'Content-Type': 'application/json'})
        response1 = urllib2.urlopen(req1)
        #response1 = opener.open(req1)
        response_read1 = response1.read()
        res1 = json.loads(response_read1)
        if res1["StatusCode"] == 0:
            print response_read1
        else:
            print response_read1
            print "Response failed!"


