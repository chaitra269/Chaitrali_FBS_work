# Create a class product with members as pid,pname,price and quantity . Add following methods:
# a. Constructor(Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Product:
    def __init__(self,pid=0,pname="Unknown",price=0.0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        print(f"Product '{self.pname}' object created.")

    def getPid(self):
        return self.pid
    def setPid(self,Newpid):
        self.bid=Newpid
    def getPname(self):
        return self.pname
    def setPname(self,NewPname):
        self.pname=NewPname
    def getPrice(self):
        return self.price
    def setPrice(self,NewPrice):
        self.price=NewPrice
    def getQuantity(self):
        return self.quantity
    def setQuantity(self,NewQuantity):
        self.quantity=NewQuantity

    def __del__(self):
        print(f"Product '{self.bname}' object destroyed.")

    def ShowBook(self):
        print("\n**********Product Details***********")
        print(f"Product ID: {self.pid}\tProduct Name: {self.pname}\tPrice: {self.price}\tQuantity: {self.quantity}")

p1=Product(10,"Electronics",100000,40)
p1.ShowBook()