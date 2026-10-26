
import random

words = ["python", "computer", "program", "student", "keyboard"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect attempts left:", attempts)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

else:
    print("\nGame over! The correct word was:", word)
