import random

hangman_art = [
    [
        "   ",
        "   ",
        "   ",
    ],
    [
        " o ",
        "   ",
        "   ",
    ],
    [
        " o ",
        " | ",
        "   ",
    ],
    [
        " o ",
        "/| ",
        "   ",
    ],
    [
        " o ",
        "/|\\",
        "   ",
    ],
    [
        " o ",
        "/|\\",
        "/  ",
    ],
    [
        " o ",
        "/|\\",
        "/ \\",
    ],
]

fruit_word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange", "peach", "pear", "plum", "raspberry", "strawberry", "watermelon"]

isgame_running = True
wrong_guesses = 0
randWord = random.choice(fruit_word_list)
hint = ["_"] * (len(randWord))

print("\n","=" * 50)
print("Welcome to Hangman Friut Edition! 🎮".center(50))
print("=" * 50)

while isgame_running:
    print("Hangman Status:")
    for line in hangman_art[wrong_guesses]:
        print(line)
    if wrong_guesses == 6:
        print("\n💀 You lost!")
        print(f"The word was: {randWord}")
        print("=" * 40)
        break

    if "".join(hint) == randWord:
        print("\n🎉 You won! 🎉")
        print("=" * 40)
        break

    print("\n🧩 Word:", " ".join(hint))
    print(f"❌ Wrong guesses: {wrong_guesses}/6")

    userGuess = input("-> Enter your letter: ").lower()

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