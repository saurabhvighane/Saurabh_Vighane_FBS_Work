# Program to Find the Roots of a Quadratic Equation

# Take input from user
A=int(input("Entrt A: "))
B=int(input("Entrt B: "))
C=int(input("Entrt C: "))

# Perform operation
D= B**2 - 4 * A * C
print(D)
R1=-B + (D**0.5)/2*A 
R2=-B - (D**0.5)/2*A 

#Display result
print(f'Root 1 is: {R1} \n Root 2 is {R2}')