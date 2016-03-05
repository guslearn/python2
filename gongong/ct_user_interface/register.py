#encoding=utf-8
import urllib
import urllib2
import json
import data
import send_register_code

url_register = data.url_register
#regcode1 = send_register_code.Regcode()
#mobile = regcode1._mobile
#smscode = regcode1._smscode

class Register:
    _userid = 0;
    _uname = ""
    _pwd = ""
    _hardinfo = data.Mobile_Hard_Info
    _mobile = ""

    def __init__(self):
        self.one_key()

    #一键注册，要以整个json格式请求
    def one_key(self):
        value = {"UserType":data.UserType["normal"],"RegFrom":31,"OSName":6,"RecommenderID":11,"MobileHardInfo":self._hardinfo,"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}
        datas = json.dumps(value)
        req = urllib2.Request(url_register,datas, {'Content-Type': 'application/json'})
        response = urllib2.urlopen(req)
        response_read = response.read()
        res = json.loads(response_read)
        self._uname = res["Data"]["UserName"]
        self._pwd = res["Data"]["Password"]
        self._userid = res["Data"]["UserID"]
        #return _uname,_pwd,_userid

'''    
    #手机号注册
    def mobile(self):
        regcode1 = send_register_code.Regcode()
        mobile = regcode1._mobile
        smscode = regcode1._smscode
        self._mobile = mobile        

        value = {"UserType":data.UserType["normal"],"RegFrom":31,"OSName":6,"mobile":self._mobile,"SmsVerifyCode":smscode,"Password":"qweasd","RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}
        datas = json.dumps(value)
        req = urllib2.Request(url_register,datas, {'Content-Type': 'application/json'})
        response = urllib2.urlopen(req)
        response_read = response.read()
        #response_read = response.read()
        res = json.loads(response_read)
        self._uname = res["Data"]["UserName"]
        self._pwd = res["Data"]["Password"]
        self._userid = res["Data"]["UserID"]
'''

'''
    #用户名密码注册
    def uname(self):
        value = {"UserType":data.UserType["normal"],"RegFrom":31,"OSName":6,"RecommenderID":11,"UserName":"testaaa007","Password":"qweasd","MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}
        datas = json.dumps(value)

        req = urllib2.Request(url_register,datas, {'Content-Type': 'application/json'})
        response = urllib2.urlopen(req)
        response_read = response.read()
        #response_read = response.read()
        res = json.loads(response_read)
        self._uname = res["Data"]["UserName"]
        self._pwd = res["Data"]["Password"]
        self._userid = res["Data"]["UserID"]

    #datas_one = self.one_key().datas
    #datas_mobie = self.mobile().datas
    #datas_uname = self.uname().datas
    #req_ = urllib2.Request(url_register,datas, {'Content-Type': 'application/json'})
    #response = urllib2.urlopen(req)
    #response_read = response.read()
    #res = json.loads(response_read)
    #username = res["Data"]["UserName"]
    #password = res["Data"]["Password"]

    #username_one,password_one = self.one_key()
'''
