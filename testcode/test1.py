class Test(object):
  def __init__(self,num):
    self.num=num

  def __eq__(self,other):
    if self.num == other.num:
        return True
    else:
        return False

  def __ne__(self,other):
    if self.num != other.num:
        return True
    else:
        return False

  def __gte__(self,other):
    print self.num
    print other.num
    if self.num >= other.num:
        return True
    else:
        return False

def main():
  a=Test(5)
  b=Test(5)
  c=Test(7)
  #print (a==b)
  #print (a==c)
  #print (a!=b)
  #print (a!=c)
  print (a>b)
  #print (a>=c)
  #print (c>=a)

if __name__ == "__main__":
    main()
