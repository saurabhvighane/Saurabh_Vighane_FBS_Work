# 1. Create a class Emp (eid,ename,basic)


class Emp:
    def __init__(self,eid,ename,basic):
        self.eid=eid
        self.ename=ename
        self.basic=basic

    def __str__(self):
        return f'Id:{self.eid}\tName:{self.ename}\tBasic:{self.basic}'
