def demo(fun):
    def wrapper():
        print("Before your main function")
        fun()
        print("After calling  main function")
    return wrapper

@demo
def x():
    a=10
    b=10
    print(a+b)

@demo
def y():
    a=10
    b=10
    print(a-b)
x()
print("______________")
y()
