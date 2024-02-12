## Hangman-project

# Description
The purpose of this project is to practise using python programming techniques, using the command line and github. The task is to create a hangman game. The computer chooses a word from a file and asks the user to imput letters to guess the word.
I think that 12 lives is a suitable number of lives for the player to start with, as some words can take a lot of guesses to work out. I allow the computer to choose a random word from a hidden word list, rather than forcing the user to input a list of words for the computer to choose from because I think it adds extra challenge and enjoyment to the game.

# Installation instructions
The program runs on python, the modules imported are the string and random modules. A file 'nounlist.csv' is also required for the program to open.

# Usage instructions
The program asks the user to input a letter. Type in a letter and press enter. After each input, the computer tells the user whether or not the letter is in the word. The user starts with 12 lives. If the letter is not in the word, the user will lose a life and the computer will tell the user how many lives they have remaining. If the letter is in the word, the computer will show how many missing spaces are left in the word and where the locations of the correctly guessed letters are.  

<img width="254" alt="Correct_letter" src="https://github.com/sgrayner/Hangman-project/assets/29332415/81cdb7f9-1e53-4ff7-9656-6665e740bc9f">
<br>
<br>
<img width="291" alt="Incorrect_letter" src="https://github.com/sgrayner/Hangman-project/assets/29332415/ebba97c2-6b0e-42b8-889e-ff41bb1baab0">
<br>
<br>
<img width="167" alt="already_tried_letter" src="https://github.com/sgrayner/Hangman-project/assets/29332415/e764f014-3c4d-4bc8-a200-84865bf9dcbe">  


# Licencing information
MIT licence
