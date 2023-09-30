# In the farm we have 35 cows , 23 chickens,
#and 40 ducks.
# Create a program to calculate total number of 
# legs in the farm
#Requirements create a variable for 
# cows, chickens and ducks , and create variables
#for their number of legs. 
# print "We have 'result' legs in the farm"

num_of_cows,num_of_chickens,num_of_ducks = 35,23,40


legs_of_a_cow = 4
legs_of_a_chicken = legs_of_a_duck = 2

total_legs_of_chickens = legs_of_a_chicken * num_of_chickens
total_legs_of_cows = legs_of_a_cow * num_of_cows
total_legs_of_ducks = legs_of_a_duck * num_of_ducks


total_num_of_legs = total_legs_of_chickens + total_legs_of_ducks + total_legs_of_cows

print("We have", total_num_of_legs, "legs in this farm.")

#Note : Python is going to add space when comma is 
# used in print function.








