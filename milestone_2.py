import random

favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

word_list = favorite_fruits

print("Word List:", word_list)

word = random.choice(word_list)

print("Randomly chosen word:", word)

guess = input("Enter a single letter: ")

print("Your guess:", guess)

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
