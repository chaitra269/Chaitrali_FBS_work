# Create a class book with members as bid,bname,price and author. add following methods:
# a. Constructor(Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    def __init__(self,bid=0,bname="Unknown",price=0.0,author="unknown"):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        print(f"Book '{self.bname}' object created.")

    def getBid(self):
        return self.bid
    def setBid(self,NewBid):
        self.bid=NewBid
    def getBname(self):
        return self.bname
    def setBname(self,NewBname):
        self.bname=NewBname
    def getPrice(self):
        return self.price
    def setPrice(self,NewPrice):
        self.price=NewPrice
    def getAuthor(self):
        return self.author
    def setAuthor(self,NewAuthor):
        self.author=NewAuthor

    def __del__(self):
        print(f"Book '{self.bname}' object destroyed.")

    def ShowBook(self):
        print("\n**********Book Details***********")
        print(f"Book ID: {self.bid}\tBook Name: {self.bname}\tPrice: {self.price}\tAuthor: {self.author}")

b1=Book(101,"Python Programming",45.99,"John Doe")
b1.ShowBook()
