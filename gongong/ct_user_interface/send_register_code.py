#ecoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import login


mobile = "13112340211"

class Regcode:
    _mobile = ""
    _smscode = 0

    def __init__(self):
        self.send_code()
    
    def send_code(self):
        

        url_send_register_code = data.url_send_register_code
        self._mobile = mobile
        value1 = {"Mobile":self._mobile,"regFrom":66}
        data1 = json.dumps(value1)
        req1 = urllib2.Request(url_send_register_code,data1, {'Content-Type': 'application/json'})
        response1 = urllib2.urlopen(req1)
        #response1 = opener.open(req1)
        response_read1 = response1.read()
        res1 = json.loads(response_read1)
       
        url_send_code = "http://usersvc.ct108.org:1904/test/GetRegSmsCode.aspx?mobile=" + self._mobile

        if res1["StatusCode"] == 0:
            print response_read1
            print "**************"
            req2 = urllib2.Request(url_send_code)
            response2 = urllib2.urlopen(req2)
            response_read2 = response2.read()
            res2 = json.loads(response_read2)
            self._smscode = res2
            print type(res2)
            print "The code is : " + str(res2)
        else:
            print "Response failed!"
            print res1["Message"]


