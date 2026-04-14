import random
level = 1
levelPassed = 0
gameOver = False
while True:
    if gameOver:
        if levelPassed == 0:
            print("\nYour title: Absolute Potato 🥔")
        elif levelPassed == 1:
            print("\nYour title: Accidental Guesser 🐵")
        elif levelPassed == 2:
            print("\nYour title: Competent 🥈")
        else:
            print("\nYour title: Legend 🧠✨🥇")
        playAgain = input("\nDo you want to play again? Yes/No: ").lower()
        if playAgain == 'no':
            break
        else:
            level = 1
            levelPassed = 0
            gameOver = False
    elif level == 1:
        secretNum = random.randint(1,10)
        hints = 3
        chances = 3
        print(f"""
              Level 1: Toddler Mode:
              The secret number is between 1-10.
              You have {hints} hints and {chances} chances.
              """)
        while chances > 0:
            userGuess = int(input("Enter your guess b/w 1-10 or type 0 for hint: "))
            if userGuess == 0:
                if hints == 0:
                    print("No hint left for this level :=(")
                elif hints == 3:
                    if secretNum % 2 == 0:
                        print("The secret number is even :-)")
                    else:
                        print("The secret number is Odd :-)")
                elif hints == 2:
                    if secretNum <= 5:
                        print("The secret number is less than 6")
                    else:
                        print("The secret number is greater than 5")
                else:
                    print(f"The secret number is {secretNum}")
                if hints > 0:
                    hints -= 1
            else:
                chances -=1
                if userGuess == secretNum:
                    print(f"Congratulations! You guessed the number {secretNum} correctly. Now qualifying for next level")
                    level = 2
                    levelPassed +=1
                    break
                else:
                    print(f"You guessed the wrong number. your remaining chances are {chances}")
        if chances == 0:
            gameOver = True
    elif level == 2:
        secretNum = random.randint(1,20)
        hints = 2
        chances = 4
        print(f"""
              Level 2: Getting Serious:
              The secret number is between 1-20.
              You have {hints} hints and {chances} chances.
              """)
        while chances > 0:
            userGuess = int(input("Enter your guess b/w 1-20 or type 0 for hint: "))
            if userGuess == 0:
                if hints == 0:
                    print("No hint left for this level :=(")
                elif hints == 2:
                    if secretNum % 2 == 0:
                        print("The secret number is even :-)")
                    else:
                        print("The secret number is Odd :-)")
                else:
                    if secretNum <= 10:
                        print("The secret number is less than 11")
                    else:
                        print("The secret number is greater than 10")
                if hints > 0:
                    hints -= 1
            else:
                chances -=1
                if userGuess == secretNum:
                    print(f"Congratulations! You guessed the number {secretNum} correctly. Now qualifying for next level")
                    level = 3
                    levelPassed +=1
                    break
                else:
                    print(f"You guessed the wrong number. your remaining chances are {chances}")
        if chances == 0:
            gameOver = True
    elif level == 3:
        secretNum = random.randint(1,50)
        hints = 2
        chances = 4
        print(f"""
              Level 3: Sweating Now:
              The secret number is between 1-50.
              You have {hints} hints and {chances} chances.
              """)
        while chances > 0:
            userGuess = int(input("Enter your guess b/w 1-50 or type 0 for hint: "))
            if userGuess == 0:
                if hints == 0:
                    print("No hint left for this level :=(")
                elif hints == 2:
                    if secretNum % 2 == 0:
                        print("The secret number is even :-)")
                    else:
                        print("The secret number is Odd :-)")
                else:
                    if secretNum <= 25:
                        print("The secret number is less than 26")
                    else:
                        print("The secret number is greater than 25")
                if hints > 0:
                    hints -= 1
            else:
                chances -=1
                if userGuess == secretNum:
                    print(f"Congratulations! You guessed the number {secretNum} correctly.")
                    levelPassed +=1
                    gameOver = True
                    break
                else:
                    print(f"You guessed the wrong number. your remaining chances are {chances}")
        if chances == 0:
            gameOver = True

print("\nThanks for playing the game")