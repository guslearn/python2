#encoding=utf-8
import urllib
import urllib2
import json
import da

#def TestLbs2():
url_register = da.url_register

#一键注册，要以整个json格式请求
value1 = {"UserType":da.UserType["normal"],"RegFrom":31,"OSName":6,"RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}

#手机号注册
value2 = {"UserType":da.UserType["normal"],"RegFrom":31,"OSName":6,"mobile":"13112340150","SmsVerifyCode":"716197","Password":"qweasd","RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}

#用户名密码注册
value3 = {"UserType":da.UserType["normal"],"RegFrom":31,"OSName":6,"RecommenderID":11,"UserName":"testaaa001","Password":"qweasd","MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"sex":0,"RegIP":"192.168.0.1","DownloadGroup":6}
data = json.dumps(value2)
req = urllib2.Request(url_register,data, {'Content-Type': 'application/json'})
response = urllib2.urlopen(req)
response_read = response.read()

print response_read
#print type(response_read) #str

res = json.loads(response_read)
print res["StatusCode"]

#if __name__ == "__main__":
#    print "main`"
#    #TestUrlOpen()
#    #TestSuds()
#    TestLbs2()
