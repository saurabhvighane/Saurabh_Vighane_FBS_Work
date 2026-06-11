### Arithmatic Operator
# Addition
q=22
p=99
e='str'
print(q+p)
# print(q+e)  #int and str can't be added

#Subtraction
a=p-q
print(a)

#Multiplication
a=p*q
print(a)

#Division
D=p/q
print(D)

#Floor Division
F=q//p
print(F)

#Modulus
M=q%p
print(M)

#Exponential
E=q**p
print(E)


###  Assignment operators
# Equal to =
s='sau'
print(s)

# +=
s+="rabh"
print(s)

# -=
p+=22
print(p)

# *=
q-=2
print(q)

# /=
q/=p
print(q)

# //=
p//=4
print(p)

# **=
q**=p
print(q)


#  Relational Operator
# ==(Exact equals to also data type)
z=11
m=11
c=(z==m)
print(c)

# !=
c=(z!=m)
print(c)

#  >
c=(z>m)
print(c)

# >=
c=(m>=z)
print(c)

# <
c=(m<=z)
print(c)

# <=
c=(z<=m)
print(c)

#  logical operator

#  Membership operator
# 1 in

li=[3,8,2,0]
print(3 in li)
print('s' in 'Saurabh')

# 2 not in 
print(2 not in li)
print(5 not in li)
print('f' not in 'First comes First serve')
l={2,3,1}
print(2 not in l)

#  Identity operator

x=10
y=10
z=30
li1=[10,20,30]
li2=[10,20,30]

# 1 is

print(x is y)
print(id(x))
print(id(y))
print(li1 is li2)
print(id(li1))
print(id(li2))

# 2 is not

print(li1 is not li2)
print(x is not y)