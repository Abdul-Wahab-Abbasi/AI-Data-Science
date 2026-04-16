import random

print("=" * 50)
print("MULTIPLAYER NUMBER GUESSING GAME 🎮".center(50))
print("=" * 50)

playerId1 = 1
player1Name = input("\nEnter name for player 1: ").capitalize()

playerId2 = 2
player2Name = input("Enter name for player 2: ").capitalize()


difficulty = input("Enter difficulty [Easy, Medium, Hard]: ").lower()
if difficulty == "medium":
    secretNo = random.randint(1,20)
    player1Chances = 4
    player2Chances = 4
    player1hints = 2
    player2hints = 2
    _range = "1-20"
elif difficulty == "hard":
    secretNo = random.randint(1,50)
    player1Chances = 5
    player2Chances = 5
    player1hints = 2
    player2hints = 2
    _range = "1-50"
else:
    if difficulty != 'easy':
        print("Invalid difficulty level. Defaulting to Easy.")
    secretNo = random.randint(1,10)
    player1Chances = 3
    player2Chances = 3
    player1hints = 2
    player2hints = 2
    _range = "1-10"

print("\n" + "=" * 50)
print("Game Started!".center(50))
print("=" * 50 + "\n")

gameOver = False
winningPlayer = 0
turn = random.randint(1,2)
secretNo = random.randint(1,10)

while True:
    if gameOver:
        print("\n" + "=" * 50)
        if winningPlayer == 1:
            print(f"🎉 Player {player1Name} WON THE GAME! 🎉".center(50))
        elif winningPlayer == 2:
            print(f"🎉 Player {player2Name} WON THE GAME! 🎉".center(50))
        else:
            print("❌ Both players failed to guess the secret number ❌".center(50))
        print("=" * 50)
        break
    elif (player1Chances + player2Chances) == 0:
        gameOver = True
    elif turn == 1:
        print(f"\n👤 {player1Name}'s Turn | Chances Left: {player1Chances}")
        if player1Chances > 0:
            userGuess = int(input(f"-> Enter your guess ({_range}) Or type 0 for hint: "))
            if userGuess == 0:
                if player1hints == 2:
                    if secretNo % 2 == 0:
                        print(f"💡 The secret number is even")
                    else:
                        print(f"💡 The secret number is odd")
                elif player1hints == 1:
                    if secretNo <= 5:
                         print("💡 The secret number is less than 6")
                    else:
                        print("💡 The secret number is greater than 5")
                else:
                    print("⚠️ You don't have any hint left")
                if player1hints > 0:
                   player1hints -= 1
            elif userGuess == secretNo:
                winningPlayer = playerId1
                gameOver = True
                print(f"✅ Congrats! You guessed the correct secret number {secretNo}!")
            else:
                print(f"❌ Wrong! The secret number is not {userGuess}")
                turn = 2
                player1Chances -= 1
        else:
            print(f"⚠️  {player1Name}, you don't have any chances left!")
            turn = 2
    elif turn == 2:
        print(f"\n👤 {player2Name}'s Turn | Chances Left: {player2Chances}")
        if player2Chances > 0:
            userGuess = int(input(f"-> Enter your guess ({_range}) Or type 0 for hint: "))
            if userGuess == 0:
                if player2hints == 2:
                    if secretNo % 2 == 0:
                        print(f"💡 The secret number is even")
                    else:
                        print(f"💡 The secret number is odd")
                elif player2hints == 1:
                    if secretNo <= 5:
                         print("💡 The secret number is less than 6")
                    else:
                        print("💡 The secret number is greater than 5")
                else:
                    print("⚠️ You don't have any hint left")
                if player2hints > 0:
                   player2hints -= 1
            elif userGuess == secretNo:
                winningPlayer = playerId2
                gameOver = True
                print(f"✅ Congrats! You guessed the correct number {secretNo}!!")
            else:
                print(f"❌ Wrong! The secret number is not {userGuess}")
                turn = 1
                player2Chances -= 1
        else:
            print(f"⚠️  {player2Name}, you don't have any chances left!")
            turn = 1