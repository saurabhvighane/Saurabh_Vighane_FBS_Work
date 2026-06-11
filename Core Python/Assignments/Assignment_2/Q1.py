# Convert the time entered in hh,min and sec into seconds.

# Take input from user
H=int(input("Enter time in Hours: "))
M=int(input("Enter time in Minutes: "))
S=int(input("Enter time in seconds: "))

# Perform operation
Seconds= H*3600 + M*60 + S

#Display result
print("Total Seconds: ",Seconds)