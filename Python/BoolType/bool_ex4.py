#We should create a program to calculate if there is still a ticket 
# for the game tonight. We are given two variables: Capacity of the stadium 
#and the amount of tickets sold. 
# Print True if I can still buy a ticket, False otherwise.
# NOTE! USER will enter the capacity and amount of tickets sold.

stadium_capacity =int(input("Please enter the stadium capacity:"))
print(type(stadium_capacity))
s = input()
sold_tickets = int(input("Please enter the amount of tickets sold:"))

#How can I check if there is still a space? 

is_there_space = stadium_capacity > sold_tickets

print("There is space for the game tonigh:", is_there_space)











