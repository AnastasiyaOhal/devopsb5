#  Leap Year
# A year is leap if it is divisible by 4 but not by 100 
# unless it is also divisible by 400. 
# Write a program that takes a year as input 
# and prints True if it's a leap year, False otherwise.

year = int(input("enter the year that you want to learn if it is a leap year:"))

# What conditions should this year give me so that I know it is a leap year/ 
# I am looking a for a year number that is divisible by 4 but not 100. 
# Or it could be divisible by only 400 and and it is a leap year. 
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print( "Is the given year leap? ", is_leap)
#Note if the number x is divisible by number z it means 
# x % z == 0 evaluates to True. 
# if x % z == 0 is True it means x is divisible by z. 










