import random
import json
import string

hanger = ['''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''',
          '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''',
          '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''',
          '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''',
          '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''',
          ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''',
          '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \   _|_''',
          '''
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    

                    \O/      
          ~WINNER~   |   ~WINNER~        
                     |    
                    / \ 

       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']


filename = 'words.txt'
with open(filename, 'r') as f:
    word_list = json.load(f)


words = [word.lower() for word in word_list]


def get_random_word(words):
    '''secret_word is the set word with letters
    guess_word is the blanks last and is modified
    guess is user input '''
    random_word_index = random.randint(0, len(words) - 1)
    secret_word = words[random_word_index]
    guess_word = list('_' * len(secret_word))
    return guess_word, secret_word


# def input_errors(guess, correct_letters, missed_letters):
#     if guess not in string.ascii_lowercase:  # the alphabet 'abc...'
#         print('Please enter a LETTER')
#     elif len(guess) != 1:
#         print('Please enter only one letter')
#     elif guess in correct_letters or guess in missed_letters:
#         print('Please enter a different letter')


def user_guess(secret_word, guess_word, missed_letters, correct_letters, lives, h):
    print('Your word is')
    print(guess_word)
    guess = input('\nPlease guess one letter: ')

    # input_errors function. Cannot call function
    if guess not in string.ascii_lowercase:  # the alphabet 'abc...'
        print('Please enter a LETTER')
    elif len(guess) != 1:
        print('Please enter only one letter')
    elif guess in correct_letters or guess in missed_letters:
        print('Please enter a different letter')
    else:

        if guess not in secret_word:
            missed_letters.append(guess)

            print('Missed letters:')
            print(missed_letters)

            for missed_letter in missed_letters:
                lives -= 1
                h += 1
            print(hanger[h])
            print('\nYou have ' + str(lives) + ' chances left\n')

        elif guess in secret_word:
            x = secret_word.index(guess)
            for x in range(len(secret_word)):
                if secret_word[x] == guess:
                    guess_word[x] = guess

            print(guess_word)
            correct_letters.append(guess)
            print('\nCorrect letters:')
            print(correct_letters)

    win(guess_word, secret_word, lives)


def win(guess_word, secret_word, lives):
    if ''.join(guess_word) == secret_word:
        print(hanger[7])


    elif lives == 0:
        print('You lose')


    if ''.join(guess_word) == secret_word or lives == 0:
        print('Your word was: ' + secret_word)
        play = input('Play again? y/n')
        if play == 'y':
            init_hangman()
        elif play == 'n':
            pass



def init_hangman():
    missed_letters = []
    correct_letters = []

    guess_word, secret_word = get_random_word(words)
    # print(secret_word)

    lives = 6
    h = 0

    print('Welcome to Hangman!')
    print(hanger[h])


    while True:
            user_guess(secret_word, guess_word, missed_letters, correct_letters, lives, h)



init_hangman()
