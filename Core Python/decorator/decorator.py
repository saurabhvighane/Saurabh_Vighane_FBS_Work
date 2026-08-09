def decorator1(fun):
    print("I am in decorator")
    def wrapper():
        print("before function call")
        fun()
        print("After function call")
    return wrapper
@decorator1
def demo():
    print("I am from function")
# x=decorator(fun)    # outer funcyion call
# x()     # inner function call with closure
demo()
