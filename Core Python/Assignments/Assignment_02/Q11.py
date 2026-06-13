# # Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# a=int(input('enter amount: '))
# b=500
# c=200
# d=100
# e=50
# f=20
# g=10
# h=5
# i=2
# j=1

# b=a // 500
# a=a % 500

# c=a // 200
# a=a % 200

# d=a // 100
# a=a % 100

# e=a // 50
# a=a % 50

# f=a // 20
# a=a % 20

# g=a // 10
# a=a % 10

# h=a // 5
# a=a % 5

# i=a // 2
# a=a % 2

# j=a // 1
# a=a % 1

# print(f'500 notes: {b}  200 notes: {c}  100 notes: {d}  50 notes: {e}  20 notes: {f}  10 notes: {g}  5 notes: {h}  2 notes: {i}  1 notes: {j}' )

amount = int(input("Enter amount: "))

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

n5 = amount // 5
amount = amount % 5

n2 = amount // 2
amount = amount % 2

n1 = amount

print("500 Notes =", n500)
print("200 Notes =", n200)
print("100 Notes =", n100)
print("50 Notes =", n50)
print("20 Notes =", n20)
print("10 Notes =", n10)
print("5 Coin =", n5)
print("2 Coin =", n2)
print("1 Coin =", n1)