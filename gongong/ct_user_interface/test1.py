#encoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import register

'''
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
'''

class TestClass:
  val1 = 100
   
  def __init__(self):
    self.val2 = 200
   
  def fcn(self,val = 400):
    val3 = 300
    self.val4 = val
    self.val5 = 500
if __name__ == '__main__':
  inst = TestClass()
  inst1 = TestClass()
  inst2 = TestClass()
 
  print TestClass.val1 # 100
  print inst1.val1   # 100
 
  inst1.val1 = 1000 
  print inst1.val1   # 1000
  print TestClass.val1 # 100
 
  TestClass.val1 =2000
  print inst1.val1   # 1000
  print TestClass.val1 # 2000
 
  print inst2.val1   # 2000   
 
  inst3 = TestClass() 
  print inst3.val1   # 2000 
'''
  print TestClass.val1
  print inst.val1
  print inst.val2
 # print inst.val3
  print inst.val4  
  print inst.val5
'''
