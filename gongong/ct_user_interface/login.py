#encoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import register

url_login = data.url_login
cookie = cookielib.CookieJar()

reg1 = register.Register()
username,password = reg1.one_key()

#用户名密码登录
value1 = {"UserName":username,"Password":password,"AppId":66,"RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"DownloadGroup":6,"StatExtInfo":{"FromAppId":66},"CodeID":"A5E31C95EE4F409CB75D4C8262420454","VerifyCode":"7ab1","Version ":"20150821"}

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
#urllib2.install_opener(opener)
#opener.open("http://www.baidu.com")
#for item in cookie:
#    print 1
#    print item.name
#    print 2
#    print item.value


datas = json.dumps(value1)
req = urllib2.Request(url_login,datas, {'Content-Type': 'application/json'})
opener.open(req) #cookie中有AccessToken
for item in cookie:
    print 1
    print item.name
    print 2
    print item.value


response = urllib2.urlopen(req)
response_read = response.read()

#print response_read

#print type(response_read) #str

res = json.loads(response_read)
print res["StatusCode"]

print "second..."

url = "http://sdk.ct108.org:1910/User/CurrentUser"
value2 = {"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""}}
data1 = json.dumps(value2)
req1 = urllib2.Request(url,data1, {'Content-Type': 'application/json'},cookie)
response1 = urllib2.urlopen(req1)
response_read1 = response.read()
#res1 = json.loads(response_read1)
print response_read1

#if __name__ == "__main__":
#    print "main`"
#    #TestUrlOpen()
#    #TestSuds()

#    TestLbs2()
