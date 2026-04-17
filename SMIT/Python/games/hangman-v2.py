import random

fruit_words = ["fig", "kiwi", "plum", "banana", "orange", "papaya", "guava", "cherry", "watermelon", "pomegranate", "strawberry"]
animal_words = ["cat", "dog", "cow", "lion", "rabbit", "donkey", "buffalo", "zebra", "tiger", "elephant", "crocodile"]
country_words = ["iran", "iraq", "oman", "turkey", "canada", "france", "germany", "mexico", "saudi arabia", "united states", "afghanistan", "bangladesh"]

hangman_art = [
    ["   ", 
     "   ", 
     "   "],
    [" o ", 
     "   ", 
     "   "],
    [" o ", 
     " | ", 
     "   "],
    [" o ", 
     "/| ", 
     "   "],
    [" o ", 
     "/|\\", 
     "   "],
    [" o ", 
     "/|\\", 
     "/ "],
    [" o ", 
     "/|\\", 
     "/ \\"],
]

print("=" * 40)
print("     Welcome to Hangman! 🎮")
print("=" * 40)

print("\nChoose a category:")
print("  1. Fruit   (type: fruit)")
print("  2. Animal  (type: animal)")
print("  3. Country (type: country)")
category = input("-> ").lower()

if category == "animal":
    word_list = animal_words
elif category == "country":
    word_list = country_words
else:
    category = "fruit"
    word_list = fruit_words

print(f"Category: {category}")

print("\nChoose a difficulty:")
print("  1. Easy   — short words       (type: easy)")
print("  2. Medium — medium words      (type: medium)")
print("  3. Hard   — long words        (type: hard)")
difficulty = input("-> ").lower()

filtered_words = []

for word in word_list:
    if difficulty == "medium" and 5 <= len(word) <= 8:
        filtered_words.append(word)
    elif difficulty == "hard" and len(word) > 8:
        filtered_words.append(word)
    elif difficulty == "easy" and len(word) <= 4:
        filtered_words.append(word)

if len(filtered_words) == 0:
    difficulty = "easy"
    for word in word_list:
        if len(word) <= 4:
            filtered_words.append(word)

print(f"Difficulty: {difficulty}")

secret_word = random.choice(filtered_words)
hints = 2
wrong_guesses = 0
guessed_letters = []

display = []
for letter in secret_word:
    if letter == " ":
        display.append(" ")
    else:
        display.append("_")

while True:

    print("\n" + "=" * 40)
    print("  Head :", hangman_art[wrong_guesses][0])
    print("  Body :", hangman_art[wrong_guesses][1])
    print("  Legs :", hangman_art[wrong_guesses][2])
    print("=" * 40)

    if wrong_guesses == 6:
        print("💀 You lost! The word was:", secret_word)
        break

    if "_" not in display:
        print("🎉 You won!")
        break

    print("Word   :", " ".join(display))
    print("Wrong  :", wrong_guesses, "/ 6")
    print("Hints  :", hints)
    print("Guessed:", ", ".join(guessed_letters) if len(guessed_letters) > 0 else "none")

    guess = input("\nGuess a letter (or 0 for hint): ").lower()
    if guess == "0":
        if hints == 0:
            print("❌ No hints left!")
        elif hints == 2:
            print("💡 Hint: The word starts with:", secret_word[0])
            hints -= 1
        else:
            print("💡 Hint: The word ends with:", secret_word[-1])
            hints -= 1
        continue

    if len(guess) != 1:
        print("⚠️  Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️  You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

print("\nThanks for playing! 👋")