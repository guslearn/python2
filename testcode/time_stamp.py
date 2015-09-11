import time
x = raw_input("Please input timeStamp...:")
y = time.localtime(float(x))
time = time.strftime('%Y-%m-%d %H:%M:%S',y)
print(time)

