#pseudocode
#Get input from user
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))

#Compare number values with if else statements
if number_1 >= number_2 and number_1 >= number_3:
    largest = number_1
elif number_2 >= number_1 and number_2 >= number_3:
    largest = number_2
else:
    largest = number_3

#Print result