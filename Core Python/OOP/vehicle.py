class Vehicle:
    def __init__(self,brand,color,speed,price):
        self.brand = brand
        self.color = color
        self.speed = speed 
        self.price = price
    
    def getbrand(self):
        return self.brand
    def setbrand(self,brand):
        self.brand = brand

    def getcolor(self):
        return self.color
    def setcolor(self,color):
        self.color = color

    def getspeed(self):
        return self.speed
    def setspeed(self,speed):
        self.speed = speed
    
    def getprice(self):
        return self.price
    def setprice(self,price):
        self.price = price

    def display(self):
        print(f'Brand:{self.brand}\tColor:{self.color}\tSpeed:{self.speed}\tprice:{self.price}')


v1 = Vehicle('BMW','White',150,2000000)
# v1.display()
v1.setprice(500000000)
v1.display()
v2 = Vehicle('Defender','Black',160,2000000)
v2.display()
print(v2.getbrand())


v2 = ()
