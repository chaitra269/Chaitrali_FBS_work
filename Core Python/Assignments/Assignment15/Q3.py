# Create a class shirt with members as sid,sname, type(Formal etc),price and size(small,large) . Add following methods:
# a. Constructor(Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Shirt:
    def __init__(self,sid=0,sname="Unknown",price=0.0,type="Unknown",size="none"):
        self.sid=sid
        self.sname=sname
        self.price=price
        self.type=type
        self.size=size
        print(f"Shirt '{self.sname}' object created.")

    def getsid(self):
        return self.sid
    def setsid(self,Newsid):
        self.sid=Newsid
    def getSname(self):
        return self.sname
    def setSname(self,NewSname):
        self.Sname=NewSname
    def getPrice(self):
        return self.price
    def setPrice(self,NewPrice):
        self.price=NewPrice
    def getType(self):
        return self.type
    def setType(self,NewType):
        self.type=NewType
    def getSize(self):
        return self.size
    def setSize(self,NewSize):
        self.size=NewSize

    def __del__(self):
        print(f"Shirt '{self.sname}' object destroyed.")

    def ShowBook(self):
        print("\n**********Shirt Details***********")
        print(f"Shirt ID: {self.sid}\tShirt Name: {self.sname}\tPrice: {self.price}\tType: {self.type}\tSize: {self.size}")

s1=Shirt(234,"Zara",5000,"Formal","Small")
s1.ShowBook()