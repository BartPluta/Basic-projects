import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback.lower() != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
            print('Your guess is too high. Try lower')
        elif feedback == 'l':
            low = guess + 1
            print('Your guess is too low. Try higher number.')
    print(f'Wow well done computer. You guess {guess} secret number correctly')


computer_guess(1000)
