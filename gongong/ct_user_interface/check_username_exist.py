#ecoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import login


url_check_username_exist = data.url_check_username_exist
username = "dating1efegfege"

value1 = {"UserName":username}
data1 = json.dumps(value1)
req1 = urllib2.Request(url_check_username_exist,data1, {'Content-Type': 'application/json'})
response1 = urllib2.urlopen(req1)
#response1 = opener.open(req1)
response_read1 = response1.read()
res1 = json.loads(response_read1)
if res1["StatusCode"] == 0:
    print response_read1
else:
    print "Response failed!"
    print res1["Message"]


