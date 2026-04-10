import random
secretNum = random.randint(1,10)
chances = 3
while chances > 0:
    userGuess = int(input("Enter your guess b/w 1 to 10: "))
    if userGuess == secretNum:
        print(f"Congratulations! You guessed the number {secretNum} correctly in {4 - chances} attempts.")
        break
    elif userGuess < secretNum:
        print("Your guess is too low. Your remain chances are: ", chances - 1)
    else:
        print("Your guess is too high. Your remain chances are: ", chances - 1)
    chances -= 1