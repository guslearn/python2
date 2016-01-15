#encoding=utf-8
import urllib
import urllib2
import json
import da

url_register = da.url_register
url_register_sendsms = da.url_register_sendsms

class Register:
#    url_register = da.url_register
    url_register_sendsms = da.url_register_sendsms

    #一键注册，要以整个json格式请求
    def register_one(self):
        value1 = {"UserType":da.UserType["normal"],"RegFrom":31,"OSName":6,"RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}

        data = json.dumps(value1)
        req = urllib2.Request(url_register,data, {'Content-Type': 'application/json'})
        response = urllib2.urlopen(req)
        response_read = response.read()
      
        print response_read
        #print type(response_read) #str 
        #res = json.loads(response_read)
        #print res["StatusCode"]

    #手机号注册
    def register_by_mobile():
        value2 = {"UserType":da.UserType["normal"],"RegFrom":31,"OSName":6,"mobile":"13112340150","SmsVerifyCode":"716197","Password":"qweasd","RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}

        sendsms = {"mobile":"13112340155","regFrom":"66"}

    #用户名密码注册
    def register_by_username():
        value3 = {"UserType":da.UserType["normal"],"RegFrom":31,"OSName":6,"RecommenderID":11,"UserName":"testaaa002","Password":"qweasd","MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}


        data = json.dumps(sendsms)
        req = urllib2.Request(url_register_sendsms,data, {'Content-Type': 'application/json'})
        response = urllib2.urlopen(req)
        response_read = response.read()

        print response_read
        #print type(response_read) #str

        res = json.loads(response_read)
        print res["StatusCode"]

