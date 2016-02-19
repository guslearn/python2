#ecoding=utf-8
import urllib
import urllib2
import json
import cookielib
import data
#import login




url_send_code = "http://usersvc.ct108.org:1904/test/GetRegSmsCode.aspx?mobile=" + "13112340204"

print "**************"
req2 = urllib2.Request(url_send_code)
response2 = urllib2.urlopen(req2)
response_read2 = response2.read()
res2 = json.loads(response_read2)
#self._smscode = res2
print type(res2)

