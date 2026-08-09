def outer():
    print("I am outer function")
    name = 'FirstBit'
    def inner():
        # print("I am inner function")
        print(name)
    return inner
    # i = inner
    # print(i)
o = outer() #()()
print(o)
print('+++++++++++')
o()
# print(type(o))