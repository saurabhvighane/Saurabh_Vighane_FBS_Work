# Write a program to convert days into years, weeks and days.

# Take input from user
Days=int(input("ENter days to calculate Years weeks and days : "))

# Perform operation
years= Days // 365
Days= Days % 365    #remaining days after a year
weeks= Days // 7    #convert them into weeks
Days= Days % 7

#Display result
print(f'Years: {years} Weeks: {weeks} Days: {Days}')