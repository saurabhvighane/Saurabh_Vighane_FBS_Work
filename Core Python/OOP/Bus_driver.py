class Busdriver:
    Deponame = 'Shivajinagar Pune'

    @staticmethod
    def showdepo():
        print(f'Deponame:{Busdriver.Deponame}')

    def __init__(self,drivername,salary,id):
        self.__drivername = drivername
        self.__salary  = salary
        self.__id = id

    def getdrivername(self):
        return self.__drivername
    def setdrivername(self,drivername):
        self.__drivername = drivername

    def getsalary(self):
        return self.__salary
    def setsalary(self,salary):
        self.__salary = salary

    def getid(self):
        return self.__id
    def setsalary(self,id):
        self.__id = id

    def display(self):
        print(f'Drivername:{self.__drivername}\tsalary:{self.__salary}\tId:{self.__id}')

D1 = Busdriver("Adinath",50000,101)
D1.showdepo()
D1.display()

