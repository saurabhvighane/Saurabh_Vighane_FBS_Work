# Addition if two no

#take input

N1=int(input("Enter no 1: "))
N2 =int(input("Enter no 2: "))

# perform operation

sum=N1+N2

# display result

print(sum)
print("Addition:",sum)  #print automatically add space between addition and sum
print("Addition:"+str(sum)) #it does not add space
print("Addition of "+str(N1)+" & "+str(N2)+" is "+str(sum)+".")
print(f"Addition of {N1} & {N2} is {sum}.")