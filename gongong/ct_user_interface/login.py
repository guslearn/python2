#encoding=utf-8
import urllib
import urllib2
import json
import da

url_login = da.url_login

#用户名密码登录
value1 = {"UserName":"dating10","Password":"1q2w3e","AppId":66,"RecommenderID":11,"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""},"StatExtInfo":{"FromAppId":66},"CodeID":"A5E31C95EE4F409CB75D4C8262420454","VerifyCode":"aaaa","Version":"20150822","DownloadGroup":6}


data = json.dumps(value1)
req = urllib2.Request(url_login,data, {'Content-Type': 'application/json'})
response = urllib2.urlopen(req)
response_read = response.read()

print response_read

res = json.loads(response_read)
print res["StatusCode"]

#if __name__ == "__main__":
#    print "main`"
#    #TestUrlOpen()
#    #TestSuds()
#    TestLbs2()
                                        
