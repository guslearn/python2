class InventoryItem(object):
    def __init__(self,title,description,price,store_id):
        self.title=title
        self.description=description
        self.price=price
        self.store_id=store_id

    def __str__(self):
        return self.title
    
    def __eq__(self,other):
        if self.store_id == other.title:
            return True
        else:
            return False

    def change_description(self,description=""):
        if not description:
            description = raw_input("Please give me a description: ")
        self.description = description

    def change_price(self,price=-1):
        while price < 0:
            price = raw_input("Please give me the new price [X.XX]: ")
            try:
                price = float(price)
                break
            except:
                print "I'm sorry, but {} isn't valid.".format(price)
        self.price = price

    def change_title(self,title=""):
        if not title:
            title = raw_input("Please give me a new title: ")
        self.title=title

class Book(InventoryItem):
    def __init__(self,title,description,price,format,author,store_id):
        super(Book,self).__init__(title=title,description=description,price=price,store_id=store_id)
        self.format = format
        self.author = author
    
    def __str__(self):
        book_line = "{title} by {author}".format(title=self.title,author=self.author)
        return book_line

    def __eq__(self,other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False

    def change_format(self,format):
        if not format:
            format = raw_input("Please give me the new format: ")
        self.format = format
    
    def change_author(self,author):
        if not author:
            author = raw_input("Please give me the new author: ")
        self.author = author


def main():
   # book=InventoryItem(title="AAA",description="BBB",price=333,store_id="123123")
   # print book

    hamlet = Book(title="Hamlet",description="A Dane has a bad time.",price=5.99,format="paperback",store_id="29382918",author="William Shakespeare")
    hamlet_hardback = Book(title="Hamlet",description="A Dane has a bad time.",price=10.99,format="hardback",store_id="3894083920",author="William Shakespeare")
    macbeth = Book(title="Macbeth",description="Don't listen to strange ladies on the side of the road.",price=4.99,format="paperback",store_id="3928932",author="William Shakespeare")

    print(hamlet == hamlet_hardback)
    print(hamlet == macbeth)
    print hamlet
    hamlet.change_description()
    print hamlet.description
    macbeth.change_format(format="audiobook")
    print (macbeth.format)

if __name__ == "__main__":
    main()









