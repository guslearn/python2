#encoding=utf-8
import splinter
#import register
import time
import json
import urllib2
import check_mobile_exist

#browser = splinter.Browser()
#ct_lbs.LBS().try_shanghai()
#time.sleep(3)
#print "ok"
#browser.quit()
if __name__ == "__main__":
    #exefile("lvs_search_near.py")
    #register.Register().one_key()
    #mobile_exist = check_mobile_exist.MobileExist()

    file = open("file_of_mobile.txt")
    lines = file.readlines()
    for line in lines:
        #line = line.strip() #   去除每次到空行
        if not line.startswith(("#")):
            mobile_exist = check_mobile_exist.MobileExist(line)
            #mobile_exist._mobile = line
            #print mobile_exist._mobile


