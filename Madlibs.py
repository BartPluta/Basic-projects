instruction = '''Hi, this is mad lib "Vacation", you have help list and instruction below. Have fun :)
Start to start the game
Quit to exit the game

Verb is an action 
Noun is a person/place/thing
Adjective describes a person/place/thing
Type Start to begin'''

while True:
    start = input(f'If you need help type help, if you want play type start. ').lower()
    if start == 'help':
        print(instruction)
    elif start == 'start':
        adjective1 = input('Adjective: ')
        adjective2 = input('Adjective: ')
        noun1 = input('Noun: ')
        noun2 = input('Noun: ')
        plural_noun1 = input('Plural noun: ')
        game1 = input('Game: ')
        plural_noun2 = input('Plural noun: ')
        verb_ending_ing1 = input('Verb ending in "ING": ')
        verb_ending_ing2 = input('Verb ending in "ING": ')
        plural_noun3 = input('Plural noun: ')
        verb_ending_ing3 = input('Verb ending in "ING": ')
        noun3 = input('Noun: ')
        plant = input('Plant: ')
        body_part = input('Part of the body: ')
        place = input('A place: ')
        verb_ending_ing4 = input('Verb ending in "ING": ')
        adjective3 = input('Adjective: ')
        number = input('Number: ')
        plural_noun4 = input('Plural noun: ')
        mad_libs = (f'''A vacation is when you take a trip to some {adjective1} place 
with your {adjective2} family. Usually you go to some place that is near a/an {noun1} or up on a/an {noun2}.
 A good vacation place is one where you can ride {plural_noun1} or play {game1} or go hunting for {plural_noun2}.
I like to spend my time {verb_ending_ing1} or {verb_ending_ing2}. When parents go on a vacation, they spend
their time eating three {plural_noun3} a day,  and fathers play golf, and mothers sit around {verb_ending_ing3}.
Last summer, my little brother fell in a/an {noun3} and got poison {plant} all over his {body_part}.
My family is going to go to (the) {place}, and I will practice {verb_ending_ing4}. Parents need vacations more
than kids because parents are always very {adjective3} and because they have to work {number} hours every day
all year making enough {plural_noun4}  to pay for the vacation. ''')
        print(mad_libs)
    elif start == "quit":
        quit()
    else:
        print("I don't understand. Type help or start.")
