#encoding=utf-8
import splinter
#import register
import time
import json
import urllib2
import check_mobile_exist
import check_user2

if __name__ == "__main__":
    #exefile("lvs_search_near.py")
    #register.Register().one_key()
    #mobile_exist = check_mobile_exist.MobileExist()

    #手机号校验
    #file = open("eg_file_of_mobile.txt")
    
    #用户名校验
    file = open("eg_file_of_username.txt")
    lines = file.readlines()
    for line in lines:
        line = line.strip() #   去除每次的空行,用户名校验需要
        if not line.startswith(("#")):
            print line
            #mobile_exist = check_mobile_exist.MobileExist(line)
            checkuser2 = check_user2.CheckUser2(line)


