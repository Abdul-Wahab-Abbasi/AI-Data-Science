import random
print("\n","=" * 50)
print("Welcome to Hangman! 🎮".center(50))
print("=" * 50)
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

fruit_word_list = ["fig", "kiwi", "plum", "banana", "orange", "papaya", "guava", "cherry", "watermelon", "pomegranate", "strawberry"]
animal_word_list = ["cat", "dog", "cow", "lion", "rabbit", "donkey", "buffalo", "zebra", "tiger", "elephant", "crocodile"]
country_word_list = ["Iran", "Iraq", "Oman", "Turkey", "Canada", "France", "Germany", "Mexico", "Saudi Arabia", "United States", "Afghanistan", "Bangladesh"]

words = []
randWord = ""
isgame_running = True

category = input("Select Word Category: \n 1. Fruit name [type: fruit]\n 2. Animal name [type: animal]\n 1. Country name [type: country]\n ->")
if category == 'animal':
    print(f"\n Selected {category}")
    category = animal_word_list
elif category == 'country':
    print(f"\n Selected {category}")
    category = country_word_list
else:
    if category != 'fruit':
        print(f"\n Selected default category 'Fruit'")
    else:
        print(f"\n Selected {category}")
    category = fruit_word_list

difficulty = input("\nSelect difficulty:\n 1. Easy: 3-4 letters word [type: easy]\n 2. Medium: 6-8 letters word [type: medium]\n 3. Hard: 10-12 letters word [type: hard] \n ->")
if difficulty == 'medium':
    for word in category:
        if len(word) > 4 and len(word) <= 8:
            words.append(word)
    print(f"\n Selected {difficulty}")
elif difficulty == 'hard':
    for word in category:
        if len(word) > 8 and len(word) <= 12:
            words.append(word)
    print(f"\n Selected {difficulty}")
else:
    for word in category:
        if len(word) <= 4:
            words.append(word)
    if difficulty != 'easy':
        print(f"\n Selected default difficulty 'easy'")
    else:
        print(f"\n Selected {difficulty}")

wrong_guesses = 0
randWord = random.choice(words).lower()
wordHint = []
hints = 2
for letter in randWord:
    if letter == " ":
        wordHint.append(" ")
    else:
        wordHint.append("_")

while isgame_running:
    print("Hangman Status:")
    for line in hangman_art[wrong_guesses]:
        print(line)
    if wrong_guesses == 6:
        print("\n💀 You lost!")
        print(f"The word was: {randWord}")
        print("=" * 40)
        break

    if "".join(wordHint) == randWord:
        print("\n🎉 You won! 🎉")
        print("=" * 40)
        break

    print("\n🧩 Word:", " ".join(wordHint))
    print(f"❌ Wrong guesses: {wrong_guesses}/6")
    print(f"💡 Hints left: {hints}")

    userGuess = input("-> Enter your letter or type 0 for hint: ").lower()
    if userGuess == '0':
        if hints > 0:
            if hints == 2:
                print(f"\n💡 Hint: The word starts with '{randWord[0]}'")
            else:
                 print(f"\n💡 Hint: The word ends with '{randWord[-1]}'")
            hints -= 1
        else:
            print("\n❌ No hints left!")
        userGuess = input("-> Enter your letter: ").lower()
        
    if userGuess in randWord:
        print("✅ Good guess!")
        for i in range(len(randWord)):
            if randWord[i] == userGuess:
                if wordHint[i] != userGuess:
                    wordHint[i] = userGuess
                    break
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1