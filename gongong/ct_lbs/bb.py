#encoding=utf-8
import urllib
import urllib2
import json
from xml.dom.minidom import parseString
from suds import WebFault
from suds.client import Client 

def TestUrlOpen():
  page = urllib.urlopen("http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=58367")
  lines = page.readlines()
  page.close()
  document = ""
  for line in lines :
    document = document + line

  from xml.dom.minidom import parseString
  dom =parseString(document)
  strings = dom.getElementsByTagName("string")
  print (strings[6].childNodes[0].data + " " + strings[7].childNodes[0].data)

def TestSuds():
  #url = 'http://webservice.webxml.com.cn/WebServices/WeatherWS.asmx?WSDL'
  url = 'http://webservice.webxml.com.cn/WebServices/WeatherWS.asmx?WSDL'
  client = Client(url)
  print (client)
  #print (client.service.getWeather('58367'))

def TestLbs():
    urltest = "http://lbsapi.uc108.org:1505/geo/getposition"
    req = urllib2.Request(urltest)
    response = urllib2.urlopen(req)
    print (response.geturl())
    print "response info : "
    print response.info()
    

def TestLbs2():
    url_lbs = "http://lbsapi.uc108.org:1505/geo/getposition"
    values = "CtUserAuth AccessToken=ac8137c026be4b0b8e6614bba0a88eed &UserID=102988 &AppID=31"
    ##params = json.dumps(values)
    ##headers = {"Content-type":"application/json; charset=utf-8","Accept": "application/json"}

    #req = urllib2.Request(url_lbs,params,headers)
    req = urllib2.Request(url_lbs)
    req.add_header("Authorization","CtUserAuth AccessToken=dad0b4d4e10e4adb89fb6f4faf5ad13c &UserID=102988 &AppID=31")
    response = urllib2.urlopen(req)
    #response_read = response.read()
    #print "Response_read type : "
    #print type(response_read)
    
    #res = json.loads(response_read)
    #print "res type : "
    #print type(res)
    #print response_read
    
    response_read = response.read()
    res = json.loads(response_read)
    print response_read
    print "response_read type : " + str(type(response_read))
    print res["StatusCode"]
    print res["Data"]["UserPoiInfo"]["UserID"]

def TestLbs3():
    url_lbs = "http://lbsapi.uc108.org:1505/geo/updateposition"
    req = urllib2.Request(url_lbs)
    re1.add_header("Authorization","CtUserAuth AccessToken=dad0b4d4e10e4adb89fb6f4faf5ad13c &UserID=102988 &AppID=31")
    data = {"Longitude":" 118.888242","Latitude":"28.931042"}
   


if __name__ == "__main__":
    print "main`"
    #TestUrlOpen()
    #TestSuds()
    TestLbs2()
