#encoding=utf-8
import codecs

str1 = "abcde bcdea cdeab"
print "1. str1 split : " + str(str1.split(" "))
c = codecs.lookup("utf-8")
print "2. codecs lookup utf-8 : " + str(c)
print "3. a1 encode : " + str(c.encode(str1))
print "4. a1 decode : " + str(c.decode(str1))

r = c.streamreader("tmp.txt")
print "5. a1 streamreader : " + str(r)
#r.readlines()
print "???6. r type : " +  str(type(r))

w = c.streamwriter("tmp.txt")
#w.write("111")

print "-"*60

look1 = codecs.lookup("gb2312")
look2 = codecs.lookup("utf-8")
a = "我爱杭州"

print "len(a) : " + str(len(a))
print "a : " + a

b = look1.decode(a)
print b



