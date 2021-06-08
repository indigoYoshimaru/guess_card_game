from model import game

with open('media\welcome.txt') as f:
    for line in f:
        print("\u001b[33m", line, end='')
    print()

game.play_game()
