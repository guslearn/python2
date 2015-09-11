#encoding=utf-8
import data
import json
import httplib


class LBS:
    #def __init__(self,browser):
    #    self.browser = browser
    
    def try_shanghai(self):
#        self.browser.visit(data.AREAAPI_URL)
#        self.browser.fill("longitude",data.LONGITUDE)
#        self.browser.fill("latitude",data.LATITUDE) 
#        self.browser.find_by_xpath("id('Area_Area_GetAreaNumber_content')/x:form/x:div[2]/x:input").click()
#       self.browser.find_by_value("Try it out!").click()

        httpClient = None
        longtitude = 121.90
        latitude = 30.89    #到98
    #    longtitude1 = longtitude
        latitude1 = latitude        

        for i in range(1,10):
         longtitude1 = 121.90
         latitude1 = latitude1+0.01
         print "latitude1 : "
         print latitude1
         url = "/api/Area/GetAreaNumber?longitude=" + str(longtitude1) + "&latitude=" + str(latitude1) 

         try:

			 
            httpClient = httplib.HTTPConnection('areaapi.uc108.org',1505,timeout=30)
            #httpClient.request('GET','/api/Area/GetAreaNumber?longitude=116.36&latitude=39.94')
            httpClient.request('GET',url)

            response = httpClient.getresponse()
            #jsonResponse = response.read()

            #print "response.status : " + str(response.status)
            #print "response.reason : " + str(response.reason)
            #print "response.getheader() : " + str(response.getheader('StateCode'))
            #如何将response.read()转换为字典？
            ss =  json.loads(str(response.read()))["StateCode"]
            print(ss)
            #file_obj = open('testLog.txt','a+')
            #file_obj.writelines(url+"\n")

            #获取response code值
            da = response.status
            if (da == 400): 
                break

            file_obj = open('testLog.txt','a+')
            file_obj.writelines(url+"\n")
            

         except Exception, e:
            print e
         finally:
            if httpClient:
                httpClient.close()
                file_obj.close()
         
        else:
            print "the End!"


if __name__ == "__main__":
	'''
	url = urllib.urlopen("http://areaapi.uc108.org:1505//api/Area/GetAreaNumber?longitude=116.36&latitude=39.94")
	res = url.read()
	res_dict = json.loads(res)
	print(res_dict["StateCode"])
	'''
	LBS().try_shanghai()
