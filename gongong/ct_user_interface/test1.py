#encoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import register

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

url = "http://sdk.ct108.org:1910/User/CurrentUser"
value2 = {"MobileHardInfo":{"WifiID":"745c39fa0900","SystemID":"34b4206771049e7","ImeiID":"162517026242370","ImsiID":"","SimSerialNO":""}}
data1 = json.dumps(value2)
req1 = urllib2.Request(url,data1, {'Content-Type': 'application/json'})
#response1 = urllib2.urlopen(req1)
response1 = opener.open(req1)
response_read1 = response1.read()
#res1 = json.loads(response_read1)
print response_read1


