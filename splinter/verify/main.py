# -*- coding: utf-8 -*-
''' 采用PIL 和pytesser进行简单的验证码识别
程序包中已经包含了pytesser，但是需要自己安装PIL

使用样例
getverify1('v1.jpg') 返回值为识别出的字符

author：nwpulei@gmail.com
2013-1-1
'''
import Image
import ImageEnhance
import ImageFilter
import sys
from pytesser import *

# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#由于都是数字
#对于识别成字母的 采用该表进行修正
rep={'O':'0',
    'I':'1','L':'1',
    'Z':'2',
    'S':'8'
    };


def  getverify1(name):
    
    #打开图片
    im = Image.open(name)
    #转化到亮度
    imgry = im.convert('L')
    imgry.save('g'+name)
    #二值化
    out = imgry.point(table,'1')
    out.save('b'+name)
    #识别
    text = image_to_string(out)
    #识别对吗
    text = text.strip()
    text = text.upper();

    for r in rep:
        text = text.replace(r,rep[r])

    print text
    return text
getverify1('v1.jpg')
getverify1('v2.jpg')
getverify1('v3.jpg')
getverify1('v4.jpg')
    
