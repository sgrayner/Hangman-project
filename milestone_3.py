import string
import random

word_list = ['apple', 'banana', 'grapes', 'orange', 'strawberry']
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        return f'Good guess! \'{guess}\' is in the word.'
    else:
        return f'Sorry, \'{guess}\' is not in the word. Try again.'

def ask_for_input():
    while True:
        guess = input('Guess a letter')
        if len(guess) == 1 and guess in string.ascii_letters:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    print(check_guess(guess))


ask_for_input()

