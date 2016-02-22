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
#reg1.one_key()
reg1.mobile()
username,password,userid = reg1._uname,reg1._pwd,reg1._userid
mobilehard = data.Mobile_Hard_Info
#print username

class Login:
    _username = username
    _userid = userid
    _userpwd = password
    _cookie = ""
    _hardinfo = mobilehard
    _mobile = ""
    #默认为同设备用户名密码登录
    def __init__(self):
        self.login_by_username_same_hard()


    #同设备用户名密码登录
    def login_by_username_same_hard(self):
        __cookie = cookielib.CookieJar()
        value1 = {"UserName":self._username,"Password":password,"AppId":66,"RecommenderID":11,"MobileHardInfo":self._hardinfo,"DownloadGroup":6,"StatExtInfo":{"FromAppId":66},"CodeID":"A5E31C95EE4F409CB75D4C8262420454","VerifyCode":"7ab1","Version ":"20150821"}

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
            print self._username
            print self._userpwd
        else:
            print "Not Sucessed!"

    #不同设备上用户名密码登录
    def login_by_username(self):
        __cookie = cookielib.CookieJar()
        value1 = {"UserName":self._username,"Password":password,"AppId":66,"RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0901","SystemID":"34b4206771049e8","ImeiID":"162517026242371","ImsiID":"","SimSerialNO":""},"DownloadGroup":6,"StatExtInfo":{"FromAppId":66},"CodeID":"A5E31C95EE4F409CB75D4C8262420454","VerifyCode":"7ab1","Version ":"20150821"}

        handler = urllib2.HTTPCookieProcessor(__cookie)
        opener = urllib2.build_opener(handler)
        datas = json.dumps(value1)
        req = urllib2.Request(url_login,datas, {'Content-Type': 'application/json'})

        response = opener.open(req)
        response_read = response.read()
        res = json.loads(response_read)
        if res["StatusCode"] == 0:
            #return __cookie
            self._cookie = __cookie
        else:
            print "Not Sucessed!"


    def login_by_mobile_and_pwd(self):
        __cookie = cookielib.CookieJar()
        self._mobile = reg1._mobile
        value1 = {"Mobile":self._username,"Password":password,"AppId":66}

        handler = urllib2.HTTPCookieProcessor(__cookie)
        opener = urllib2.build_opener(handler)
        #urllib2.install_opener(opener)

        datas = json.dumps(value1)
        req = urllib2.Request(url_login,datas, {'Content-Type': 'application/json'})

        response = opener.open(req)
        #response = urllib2.urlopen(req)
        response_read = response.read()

        res = json.loads(response_read)
        #print res["StatusCode"]
        #print cookie
        if res["StatusCode"] == 0:
            #return __cookie
            self._cookie = __cookie
            print self._username
            print self._userpwd
        else:
            print "Not Sucessed!"
