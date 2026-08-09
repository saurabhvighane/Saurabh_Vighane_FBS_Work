def generator(n):
    for i in range(1,n+1):
        yield(i)
g =generator(5)
print(next(g))
print("Ruk")
print(next(g))
print("Kya hai")
print(next(g))
print("Kya hai")
print(next(g))
print("Kya hai")
print(next(g))
print("Kya hai")



