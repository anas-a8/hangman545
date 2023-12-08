import random

# Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

# Assign this list to a variable called word_list.
word_list = favorite_fruits

# Print out the newly created list to the standard output (screen).
print("Word List:", word_list)

# Create the random.choice method and pass the word_list variable into the choice method.
# Assign the randomly generated word to a variable called word.
word = random.choice(word_list)

# Print out word to the standard output.
print("Randomly chosen word:", word)

def check_guess(guess):
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()
    
    # Step 3: Check if the guess is in the word
    if guess in word:
        # Step 4: Print a message for a correct guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        # Step 5: Print a message for an incorrect guess
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        # Step 2: Move the code that checks if the input is a valid guess into this function block.
        guess = input("Enter a single letter: ")
        print("Your guess:", guess)

        # Step 3: Call the check_guess function to check if the guess is in the word.
        check_guess(guess)

        # Step 4: Break out of the loop if the guess is valid.
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Oops! That is not a valid input.")

# Step 5: Call the ask_for_input function to test your code.
ask_for_input()
