import string
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! \'{guess}\' is in the word.')
            for position in range(len(self.word)):
                if self.word[position] == guess:
                    self.word_guessed[position] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, \'{guess}\' is not in the word. You have {self.num_lives} lives left.')

        
    def ask_for_input(self):
        while True:
            guess = input('Guess a letter')
            if len(guess) != 1 or guess not in string.ascii_letters:
                print('Invalid character. Please, enter a single alphabetical letter.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                print(self.check_guess(guess))
                self.list_of_guesses.append(guess)
                
game = Hangman(['apple', 'banana', 'grapes', 'orange', 'strawberry'])
game.ask_for_input()
        
        