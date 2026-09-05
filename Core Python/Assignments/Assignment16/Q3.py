# Create a class shirt with members as sid,sname, type(Formal etc),price and size(small,large) . Add following methods:
# a. Constructor(Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. for each size of shirt price should change by 10%
# (eg. If 1000 is price then small price=1000,medium=1100,large=1200 and xlarge=1300)use static concept

class Shirt:
    SIZE_MULTIPLIERS={
        "small":1.0,
        "medium": 1.1,
        "large": 1.2,
        "xlarge": 1.3,
    }
    def __init__(self,sid=0,sname="Generic",type="Formal",price=1000.0,size="small"):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.base_price=price
        self.size=size.lower()
        self.price = self.calculate_price()

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
        print(f"Shirt '{self.sname}' removed.")
    def calculate_price(self):
        multiplier=Shirt.SIZE_MULTIPLIERS.get(self.size,1.0)
        return self.base_price*multiplier

    def ShowBook(self):
        print("\n**********Shirt Details***********")
        print(f"Shirt ID: {self.sid}\tShirt Name: {self.sname}\tType: {self.type}\tSize: {self.size}\tFinal Price:{self.price}")

s1=Shirt(301,"Arrow","Formal",1000,"Small")
s2=Shirt(302,"Arrow","Formal",1000,"Medium")
s3=Shirt(303,"Arrow","Formal",1000,"large")
s4=Shirt(304,"Arrow","Formal",1000,"xlarge")
s1.ShowBook()
s2.ShowBook()
s3.ShowBook()
s4.ShowBook()