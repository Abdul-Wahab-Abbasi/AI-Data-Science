import random
number  = random.randint(1000,2000)
print(number)

# Guess the number
userGuess = int(input("Enter your number b/w 1 to 10: "))
randNumber = random.randint(1,10)
print(f"""
Your guess: {userGuess}
Correct answer: {randNumber}
""")
