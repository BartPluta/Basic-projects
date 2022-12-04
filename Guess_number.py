import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} '))
        print(guess)
        if guess < random_number:
            print('Your guess is incorrect. Try higher number.')
        elif guess > random_number:
            print ('Ayy, your guess number is too high. Try lower number.')

    print(f'YEAH!! You guess correct number {random_number}')


guess(1000)
