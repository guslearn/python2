#encoding=utf-8
import urllib
import urllib2
import json
from xml.dom.minidom import parseString
from suds import WebFault
from suds.client import Client 

def TestLbs2():
    url_lbs = "http://lbsapi.uc108.org:1505/geo/getposition"
    values = "CtUserAuth AccessToken=ac8137c026be4b0b8e6614bba0a88eed &UserID=102988 &AppID=31"
    ##params = json.dumps(values)
    ##headers = {"Content-type":"application/json; charset=utf-8","Accept": "application/json"}

    #req = urllib2.Request(url_lbs,params,headers)
    req = urllib2.Request(url_lbs)
    req.add_header("Authorization","CtUserAuth AccessToken=dad0b4d4e10e4adb89fb6f4faf5ad13c &UserID=102988 &AppID=31")
    response = urllib2.urlopen(req)
    response_read = response.read()
    res = json.loads(response_read)
    print response_read
    print "response_read type : " + str(type(response_read))
    print res["StatusCode"]
    print res["Data"]["UserPoiInfo"]["UserID"]


def TestRest():
    url = "http://sdk.ct108.org:1910"
    data = {"RefFrom":31,"RegIP":"127.0.0.1","UserType":0,"Sex":0,"OSName":6,"MobileHardInfo":{"WifiID":"","SystemID"}}
    req = urllib2.Request(url)
    response = urllib2.urlopen(req,"post",30)
    respose_read = response.read()
    print response_read





if __name__ == "__main__":
    print "main`"
    TestRest()
