#encoding=utf-8
import Image
import ImageEnhance
import ImageFilter
import sys
sys.path.append("../pytesser")
import pytesser
#sys.path.append("..")
#import python2.pytesser

#二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

rep = {'O':'0','I':'1','L':'1','Z':'2','S':'8'};

def getverify1(name):
    #打开图片
    #im = Image.open(name)



    subname = name.split(".")
    print subname[0]
    sub = subname[0] + ".tiff"
    print sub   
    im = Image.open(name)
    im = im.convert('RGB')
    print im
    im.save(sub,format="tiff")
   # im = Image.open(name).convert('RGB')
  #  im.save(sub)
    print (im.save(sub))
    


    #转化到亮度
    imgry = im.convert('L')
#    imgry.save('g'+name)



    imgry.save('g'+sub)
    


    #二值化
    out = imgry.point(table,'1')


#    out.save('b'+name)


    out.save('b'+sub)



 #识别
    text = pytesser.image_to_string(out)
    #识别对吗
    text = text.strip()
    text = text.upper()

    for r in rep:
        text = text.replace(r,rep[r])

    print text
    return text

#picname = "v1.jpg"
#picname = "eurotext.tif"
picname = "phototest.tif"
getverify1(picname)


