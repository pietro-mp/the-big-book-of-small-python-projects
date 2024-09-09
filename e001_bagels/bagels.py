import random

SECRET_SIZE = 3
MAX_CLUES = 10


def main():
    """the main game"""
    print(f'''
I am thinking of a {SECRET_SIZE}-digit-number. Try to guess what is it.
Here are some clues:
When I say:    That means:
    Pico       One digit is correct but in the wrong position.
    Fermi      One digit is correct and in the right position.
    Bagels     No digit is correct.
''')

    while True:
        # o loop principal do jogo
        print('I have thought up a number.')
        print(f'You have {MAX_CLUES} guesses to get it.')
        secret_num = get_random()
        num_guesses = 1
        while num_guesses <= MAX_CLUES:
            guess = ''

            while len(guess) != SECRET_SIZE or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('> ')
            guess_clues = get_clues(guess, secret_num)
            print(guess_clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_CLUES:
                print('You ran out of guesses!')
                print(f'The answer was {secret_num}')
        print('Do you want to play again? (y/n)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
# bagels, a deductive logic game
def get_random():
    """returns the secret number (in string) with size set in SECRET_SIZE."""
    nums = list('0123456789')

    random.shuffle(nums)
    secret_num = ''
    for i in range(SECRET_SIZE):
        secret_num += nums[i]
    return secret_num


def get_clues(guess, secret_num):
    """returns the clues as a str (each one separated by a space)"""
    if guess == secret_num:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        # one number is correct and in the right pos
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        # one number is correct but in the wrong pos
        elif guess[i] in secret_num:
            clues.append('Pico')
    # nothing is correct
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()
