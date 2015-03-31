'''
f = open("users.txt")
lines = f.readlines()
f.close()

f = open("users.txt","w")
lines[0] = ("Jacob\n")
f.write("try")
f.writelines(lines)
f.close()
f = open("users.txt")
alines = f.readlines()
for line in alines:
    print line

f.close()
'''

'''
f = open("tmp.txt","w+")
f.write("this is a new file")
f.close()
f = open("tmp.txt")
print (f.readlines())
f.close()
'''

import os

'''
current_dir = os.getcwd()
listeddir = os.listdir(current_dir)
print listeddir
'''

stats = os.stat("users.txt")
print stats.st_size


