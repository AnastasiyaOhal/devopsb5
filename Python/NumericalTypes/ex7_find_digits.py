

#Create a program that will find each digit just using
# the variable name. 
# One fact is that number is always going to be 4 digit.

# Note! Every time finding a remainder with 10 gives us 
# last digit from the number. 
#Note! Every time a number is divided by 10 will 
# lose its last digit. 
# Find the remainder with 10 which will give last digit
# since the last digit is found then remove it by dividing
# 10
four_digit_num = 1000

last_digit = four_digit_num % 10
print(last_digit)
# I want to remove the last digit
three_digit_version = four_digit_num //10

third_digit = three_digit_version % 10 
print(third_digit)
two_digit_version = three_digit_version // 10

second_digit = two_digit_version % 10
print(second_digit)

first_digit = two_digit_version // 10
print(first_digit)











