#== equal to, != not equal, < less than, > greater than, <= less than or equal to, >= greater than or equal to.
number = 10
is_greater_than_five = number > 5
is_equal_to_ten = number == 10
is_odd = number % 2 != 0 #True(checks if the remainder after division by 2 is not 0, indicating an odd number)

# Type casting
age_in_string = "25" #This is a string, not a number
age_in_numbers = int(age_in_string) # Now age_in_numbers is 25 (integer)

#input
name = input("what is your name? ")
print("Hello,", name) #Personalized greeting using input

#calculations
num1 = int(input("Enter the first number: ")) #convert input to integer
num2 = int(input("Enter the second number: "))
#perform the addition and store the result
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

#Loop
#Loop through a list of exam scores and print grades based on a specific grading scale,
grades = [85,92,78,99,65]
for score in grades:
    if score >= 90:
        print(score, "is an A.")
    elif score >= 80:
        print(score, "is a B.")
