# WAP to print all numbers in a range divisible by a given number.
n=int(input("Enter no: "))
srt=int(input("Enter starting no: "))
end=int(input("Enter ending no: "))

for i in range(srt,end+1):
    if n%i==0:
        print(i)

# while(srt<=end):
#     if srt%n==0:
#         print(srt)
#     srt+=1