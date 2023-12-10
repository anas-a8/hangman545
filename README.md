# Hangman Game in Python


## Table of Contents
1. [Project Description](#project-description)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [File Structure](#file-structure)
5. [License Information](#license-information)


## 1. Project Description
### a. What the project does
Hangman is game coded in Python. The game randomly selects a word from a provided list in which a player thinks of a word and the player tries to guess that word. The player has a limited number of attempts, and the game continues until the player either guesses the entire word or runs out of attempts(lives).

### b. The aim of the project
The aim is to provide a simple and functional implementation of the Hangman game, as a practical project  for understanding basic programming concepts, including classes, user input handling, and random selection in Python

### c. What I Learned
- Object-oriented programming in Python.
- Working with lists in Python
- Random selection of elements from a list.
- Handling user input and implementing input validation
- Writing basic conditional statements


## 2. Installation Instructions
To run the Hangman game on your local machine, follow these detailed installation instructions:


1. install [Python](https://www.python.org/).
2. Clone the repository from github to your local machine:
git clone https://github.com/anas-a8/hangman545.git
3. Run the Game.


## 3. Usage Instructions
To play the Hangman game, follow these steps:

1. Run the game 

2. You will be prompted to guess a letter.

3. Enter a single alphabetical character as your guess. The game will validate your input:

    - If the input is not a single alphabetical character, you will receive an error message, and you will be prompted to enter a valid guess.
    - If you have already guessed the letter, you will be notified, and you can enter a different guess.


4. After each guess, the game will provide feedback:

    - If your guess is correct, the program will inform you, and the display will update to reveal the correctly guessed letters.
    - If your guess is incorrect, the program will deduct a life, and you will be informed of the remaining lives.

5. Continue guessing until you either correctly guess the entire word or run out of lives.

6. The game will end with one of the following outcomes:

    - If you correctly guess the word, the program will congratulate you, and you win the game.
    - If you run out of lives, the program will inform you that you lost.


## 4. File Structure
hangman545/
│
├── milestone_2.py
├── milestone_3.py
├── milestone_4.py
├── milestone_5.py
└── README.md

- `hangman.py`: The main Python script containing the Hangman class and the game logic.
- `README.md`: Documentation file providing information about the project.


## 5. License Information
This Hangman game is released under the MIT License. You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

For more details, please refer to the: https://opensource.org/license/mit/