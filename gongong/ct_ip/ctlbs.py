#encoding=utf-8
import data
import json
import httplib


class LBS:
    #def __init__(self,browser):
    #    self.browser = browser
    
    def try_shanghai(self):
        httpClient = None
        longtitude = 73.45 #(73.04,54.27) (73.04,18.00) (137.50,53.40) (137.50,21.23)  新疆（73.45,39.42）（78.97,34.31）（87.78,49.40）（96.45,42.84）
        latitude = 39.42   
        #x = 6447
        x = 2300
        x1 = 65
        #y = 3627
        y = 298
        y1 = 47
       
        #longtitude1 = longtitude
        #latitude1 = latitude        

        #x循环
        for i in range(0,x):
         #longtitude1 = 73.04 + i*0.01
         longtitude1 = 73.45 + i*0.01
         for j in range(0,y):
              #latitude1 = 18.00 + j*0.01
              latitude1 = 39.42 + j*0.01
              print "pongtitude : " + str(longtitude1)
              print "latitude1 : " + str(latitude1)
              url = "/api/Area/GetAreaNumber?longitude=" + str(longtitude1) + "&latitude=" + str(latitude1) 
              
              print "url is : "
              print (url)
              
              file_obj = open('testLog.txt','a+')
              
              try:
                print j
                httpClient = httplib.HTTPConnection('areaapi.uc108.org',1505,timeout=30)
                #httpClient.request('GET','/api/Area/GetAreaNumber?longitude=116.36&latitude=39.94')
                httpClient.request('GET',url)

                response = httpClient.getresponse()
                
                print "response : " + str(response.read())
                #如何将response.read()转换为字典？
                ss =  json.loads(str(response.read()))["Data"]
                tt =  json.loads(str(response.read()))["StateCode"]
                print "Data is : "
                print(ss)
                print ("\n")

                #获取response code值
                #da = response.status
                #if (da == 400): 
                #   break
            
                #file_obj = open('testLog.txt','a+')

                if (ss == "000000" and tt == "200"):
                    file_obj.writelines("longtitude : " + longtitude + "latitude : " +  latitude1 + "\n")
                    file_obj.writelines(url+"\n")
            

              except Exception, e:
                print e
              finally:
                if httpClient:
                    httpClient.close()
                    file_obj.close()
         

#if __name__ == "__main__":
#	'''
#	url = urllib.urlopen("http://areaapi.uc108.org:1505//api/Area/GetAreaNumber?longitude=116.36&latitude=39.94")
#	res = url.read()
#	res_dict = json.loads(res)
#	print(res_dict["StateCode"])
#	'''
#	LBS().try_shanghai()
