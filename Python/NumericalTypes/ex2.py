# We are asked to create a program to calculate 
# average score for a student with the exam scores following:
# 1 -> 70
# 2 -> 95
# 3 -> 50 
# 4 -> 45
# Calculate the average score for the student 
# and print the average in following format. 
# Average score for given student grades is `avgScore`. 

exam1, exam2, exam3, exam4 = 70, 95, 50, 45


sum_exam_scores = exam1 + exam2 + exam3 + exam4 
avg = sum_exam_scores / 4
print("Average score for given student grades is", avg)

#What is the type of variable avg? 
#float
# type() function
#When we put the variable name in a type function it will 
# show the type of a variable. 
print(type(avg))









