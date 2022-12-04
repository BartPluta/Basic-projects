game_chat = ""
instruction = '''start - to start the car
stop - to stop the car
quit - to exit'''
start = 'Car started...Ready to go!'
start_already = 'Car already started!!'
started = False
stop = 'Car stopped.'
stop_already = 'Car already stopped!!'
idu = "I don't understand that..."
while True:
    game_chat = input('>').lower()
    if game_chat == 'help':
        print(instruction)
    elif game_chat == 'start':
        if started:
            print(start_already)
        else:
            started = True
            print(start)
    elif game_chat == 'stop':
        if not started:
            print(stop_already)
        else:
            started = False
            print(stop)
    elif game_chat == 'quit':
        break
    else:
        print(idu)
