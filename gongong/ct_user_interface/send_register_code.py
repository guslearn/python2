#ecoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
import login


url_send_register_code = data.url_send_register_code
mobile = "13112340204"

value1 = {"Mobile":mobile,"regFrom":66}
data1 = json.dumps(value1)
req1 = urllib2.Request(url_send_register_code,data1, {'Content-Type': 'application/json'})
response1 = urllib2.urlopen(req1)
#response1 = opener.open(req1)
response_read1 = response1.read()
res1 = json.loads(response_read1)
if res1["StatusCode"] == 0:
    print response_read1
else:
    print "Response failed!"
    print res1["Message"]


