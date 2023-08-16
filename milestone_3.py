import string

while True:
    guess = input('Guess a letter')
    if len(guess) == 1 and guess in string.ascii_letters:
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')