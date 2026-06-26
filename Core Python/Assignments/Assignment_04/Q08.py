# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

srt=int(input("Enter starting no: "))
end=int(input("Enter ending no: "))

i=srt
while(i<=end):
    if i%7==0 and i%5==0:
        print(i)
    i+=1

