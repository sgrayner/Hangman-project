import string
import random

class Hangman:
    '''This class is used to set up a game of hangman.
    Attributes:
        word_list (list): A list of words input by the user.
        word (str): A word randomly selected from the word list input by the user.
        word_guessed (list): A list of strings, containing underscores for each letter in the word. Each underscore is replaced when the user guesses a missing letter.
        num_letters (int): The number of letters in the word.
        num_lives (int): The number of lives the user has remaining. The user looses a life each time they guess an incorrect letter.
        '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        
        self.list_of_guesses = []

    def _check_guess(self, guess):
        '''This function is used to let the user know if their guess is correct or incorrect 
            and either add a correct letter to word_guessed, or to deduct a life for an incorrect letter.
            
            Arguments: guess'''
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

        
    def _ask_for_input(self):
        '''This function asks the user to input a letter. It checks if the user input is valid and passes a 
            valid input to the check_guess function.'''
        while True:
            guess = input('Guess a letter')
            if len(guess) != 1 or guess not in string.ascii_letters:
                print('Invalid character. Please, enter a single alphabetical letter.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                print(self._check_guess(guess))
                self.list_of_guesses.append(guess)
                
game = Hangman(['apple', 'banana', 'grapes', 'orange', 'strawberry'])
game._ask_for_input()
        
        