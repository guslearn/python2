#encoding=utf-8
import urllib
import urllib2
import json

#def TestLbs2():
url_lbs = "http://lbsapi.uc108.org:1505/geo/getposition"
auth_value = "CtUserAuth AccessToken=508c578720644ca495df81f7f514b9c5 &UserID=102988 &AppID=31"
req = urllib2.Request(url_lbs)
req.add_header("Authorization",auth_value)
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
print "abc"
#print response_read
#print "response_read type : " + str(type(response_read))
#print res["StatusCode"]
#print res["Data"]["UserPoiInfo"]["UserID"]

'''def TestLbs3():
    url_lbs = "http://lbsapi.uc108.org:1505/geo/updateposition"
    req = urllib2.Request(url_lbs)
    re1.add_header("Authorization","CtUserAuth AccessToken=dad0b4d4e10e4adb89fb6f4faf5ad13c &UserID=102988 &AppID=31")
    data = {"Longitude":" 118.888242","Latitude":"28.931042"}
'''   


#if __name__ == "__main__":
#    print "main`"
#    #TestUrlOpen()
#    #TestSuds()
#    TestLbs2()
