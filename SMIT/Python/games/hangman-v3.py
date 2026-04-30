import random

easy_words = ["plum", "date", "fig", "kiwi", "pear",]
medium_words = ["banana", "cherry", "lemon", "mango", "orange", "peach"]
hard_words = ["raspberry", "strawberry", "watermelon"]

isgame_running = True
while isgame_running:
    wrong_guesses = 0
    difficulty = input("Select difficulty: Easy, Medium, Hard: ").lower()
    randWord = ""
    hint = []
    chances = 0
    playerHints = 1
    if difficulty == "medium":
        randWord = random.choice(medium_words)
        hint = ["_"] * (len(randWord))
        hint[0],hint[1] = randWord[0], randWord[1]
        chances = 3
    elif difficulty == "hard":
        randWord = random.choice(hard_words)
        hint = ["_"] * (len(randWord))
        hint[0] = randWord[0]
        chances = 2
    else:
        randWord = random.choice(easy_words)
        hint = ["_"] * (len(randWord))
        hint[0],hint[1],hint[2] = randWord[0], randWord[1], randWord[2]
        chances = 5
    
    print("\n","=" * 50)
    print(f"Welcome to Hangman Fruit Edition!, Difficulty: {difficulty.upper()} 🎮".center(50))
    print("=" * 50)
    
    while True:
        if "".join(hint) == randWord:
            print("\n🎉 You won! 🎉")
            print("=" * 40)
            break
    
        if wrong_guesses == chances:
            print("\n💀 You lost!")
            print(f"The word was: {randWord}")
            print("=" * 40)
            break
    
        print("\n🧩 Word:", " ".join(hint))
        print(f"❌ Wrong guesses: {wrong_guesses}/{chances}")
        print(f"💡 Chances left: {chances - wrong_guesses}")
    
        userGuess = input("-> Enter your letter Or type 'hint' to use your hint: ").lower()
        if len(userGuess) != 1 and userGuess != "hint":
            print("⚠️ Please enter a single letter.")
            userGuess = input("-> Enter your letter Or type 'hint' to use your hint: ").lower()
    
        if userGuess == "hint":
            if playerHints > 0:
                print("💡 Hint: The word ends with", randWord[-1])
                playerHints -= 1
            else:
                print("⚠️ No hints left!")
            continue
        if userGuess in randWord:
            print("✅ Good guess!")
            for i in range(len(randWord)):
                if randWord[i] == userGuess:
                    if hint[i] != userGuess:
                        hint[i] = userGuess
                        break
        else:
            print("❌ Wrong guess!")
            wrong_guesses += 1
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        isgame_running = False
        print("Thanks for playing! Goodbye! 👋")