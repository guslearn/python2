#ecoding=utf-8
import urllib
import urllib2
import json
import data

url_check_mobile_exist = data.url_check_mobile_exist
#file = open("file_of_mobile.txt")
#lines = file.readlines()
#    for line in lines:
#        #line = line.strip() #   去除每次到空行
#        if not line.startswith("#"):
#           print line

class MobileExist:
    _mobile = ""
    
    #lines = file.readlines()
    #for line in lines:
    #    #line = line.strip() #   去除每次到空行
    #    if not line.startswith("#"):
    #        print line

    def __init__(self,mobile):
        self._mobile = mobile
        self.is_exist()

    def is_exist(self):
        value1 = {"Mobile":self._mobile}
        data1 = json.dumps(value1)
        req1 = urllib2.Request(url_check_mobile_exist,data1, {'Content-Type': 'application/json'})
        response1 = urllib2.urlopen(req1)
        #response1 = opener.open(req1)
        response_read1 = response1.read()
        res1 = json.loads(response_read1)
        
        print "\n"
        print "Mobile : " + self._mobile

        if res1["StatusCode"] == 0:
            print response_read1
            #print type(res1["Data"])  #bool
            if (res1["Data"]):
                print "T"
            if not (res1["Data"]) == "false":
                print "F"

        else:
            print "Response failed!"
            #print res1["Message"]
            print response_read1


