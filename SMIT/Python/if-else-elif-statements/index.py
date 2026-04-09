# if statement
# if statement works by checking whether the given condition is true or false. 
# If the condition istrue, the code block inside the if statement will be executed. 
# If the condition is false, the code block will be skipped.
number = 10
if number > 5:
    print("Number is greater than 5")

number = 5
if number >= 5:
    print("Number is greater than or equal to 5")

number = 3
if number == 3:
    print("Number is equal to 3")

# else statement
# else statement is used to execute a block of code when the condition in the if statement is false.
number = 2
if number > 5:
    print("Number is greater than 5")
else:
    print("Number is not greater than 5")


# elif statement
# elif statement is used to check multiple conditions. It stands for "else if".
number = 0
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# Practice 1
# Check if student has paid the last month's fee if not
# then check if they have scholarship if they have scholarship
# then they don't need to pay the fee otherwise they need to pay the fee.
lastMonthFee = 'unpaid'
hasScholarship = True

if lastMonthFee == 'paid':
    print("Student has paid the fee.")
elif hasScholarship:
    print("Student have scholarship, no need to pay the fee.")
else:
    print("Please pay your last month's fee.")

# Practice 2
# Create a grading system that assigns letter grades based on a student's score.
score = float(input("Enter your score b/w (0 - 100): "))
if score > 100:
    print("Please enter the score b/w (0 - 100)")
elif score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")