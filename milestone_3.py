import random

favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

word_list = favorite_fruits

print("Word List:", word_list)

word = random.choice(word_list)

print("Randomly chosen word:", word)

def check_guess(guess):
    guess = guess.lower()
    
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        print("Your guess:", guess)

        check_guess(guess)

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Oops! That is not a valid input.")

ask_for_input()
