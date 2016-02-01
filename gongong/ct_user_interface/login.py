#ecoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import register


url_login = data.url_login
#cookie = cookielib.CookieJar()

reg1 = register.Register()
reg1.one_key()
username,password,userid = reg1._uname,reg1._pwd,reg1._userid
#print username

class Login:
    _username = username
    _userid = userid
    _cookie = ""
    #默认为用户名密码登录
    def __init__(self):
        self.login_by_username()

    def login_by_username(self):
        __cookie = cookielib.CookieJar()
        value1 = {"UserName":self._username,"Password":password,"AppId":66,"RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"DownloadGroup":6,"StatExtInfo":{"FromAppId":66},"CodeID":"A5E31C95EE4F409CB75D4C8262420454","VerifyCode":"7ab1","Version ":"20150821"}

        handler = urllib2.HTTPCookieProcessor(__cookie)
        opener = urllib2.build_opener(handler)
        #urllib2.install_opener(opener)

        datas = json.dumps(value1)
        req = urllib2.Request(url_login,datas, {'Content-Type': 'application/json'})

        response = opener.open(req)
        #response = urllib2.urlopen(req)
        response_read = response.read()

        #print response_read
        #for item in cookie:
            #print 1
            #print item.name
            #print 2
            #print item.value
            #print 3
            #print item.path
            #print 4
            #print item.domain
            #print 5
            #print item.version

        res = json.loads(response_read)
        #print res["StatusCode"]
        #print cookie
        if res["StatusCode"] == 0:
            #return __cookie
            self._cookie = __cookie
        else:
            print "Not Sucessed!"



