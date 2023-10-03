# Create a program that will add up the value of a number of quarters, dimes, nickels, and pennies. 
# The number of each type of coin is input by the user. The total value is printed in dollars.
# TASK-1
# Example: 
# Quarters: 5 
# Dimes: 4 
# Nickels: 3 
# Pennies: 2
# The total in dollars is $1.82

quarters = 25
dimes = 10
nickels = 5
pennies = 1

num_of_quarters = int(input("Please enter the number of quarters: "))
num_of_dimes = int(input("Please enter the number of dimes: "))
num_of_nickels = int(input("Please enter the number of nickels: "))
num_of_pennies = int(input("Please enter the number of pennies: "))

total_of_quarters = float(num_of_quarters * quarters / 100)
print (total_of_quarters)
total_of_dimes = float(num_of_dimes * dimes / 100)
print (total_of_dimes)
total_of_nickels = float(num_of_nickels * nickels / 100)
print (total_of_nickels)
total_of_pennies = float(num_of_pennies * pennies / 100)
print (total_of_pennies)
total = total_of_quarters + total_of_dimes + total_of_nickels + total_of_pennies

print ("Your total is $",total)