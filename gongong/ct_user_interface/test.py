#encoding=utf-8
import splinter
import register
import time
import json
import urllib2
import login

#browser = splinter.Browser()
#ct_lbs.LBS().try_shanghai()
#time.sleep(3)
#print "ok"
#browser.quit()
if __name__ == "__main__":
    #exefile("lvs_search_near.py")
    #register.Register().one_key()
    login.Login().login_by_username()
