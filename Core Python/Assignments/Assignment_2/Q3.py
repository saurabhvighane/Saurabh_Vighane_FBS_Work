# Convert distant given in feet and inches into meter and centimeter.

# Take input
feet=float(input("Enter the distance in feet:"))
inches=float(input("Enter distance in inches"))

# perform operation
t_inches= (feet*12) + inches
cm=t_inches * 2.54

meter=int(cm // 100)
cm=cm % 100

# display output
print(f"distance in meter is {meter} and cm is {cm}")