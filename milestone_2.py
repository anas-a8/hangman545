# Go to the first line of your file.
# Write import random on the line.
import random

# Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

# Assign this list to a variable called word_list.
word_list = favorite_fruits

# Print out the newly created list to the standard output (screen).

# Print out the newly created list to the standard output (screen).
print("Word List:", word_list)

# Create the random.choice method and pass the word_list variable into the choice method.
# Assign the randomly generated word to a variable called word.
word = random.choice(word_list)

# Print out word to the standard output.
print("Randomly chosen word:", word)

guess = input("Enter a single letter: ")

print("Your guess:", guess)

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # In the body of the if statement, print a message that says "Good guess!".
    print("Good guess!")
else:
    # Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
    print("Oops! That is not a valid input.")
