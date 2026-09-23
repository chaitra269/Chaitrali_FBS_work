# 1. Create a class Emp (eid,ename,basic)

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(f"ID: {self.eid} | Name: {self.ename} | Basic Salary: {self.basic}")

