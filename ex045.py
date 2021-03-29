#: Crie um programa que faça o computador
# jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Stone', 'Paper', 'Scissors')
computer = randint(0, 2)
print('''Your options:
[0] Stone
[1] Paper
[2] Scissors''')
player = int(input('What is your play? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 12)
print(f'Computer played {itens[computer]}')
print(f'Player played {itens[player]}')
print('-=' * 12)
if computer == 0: #STONE
    if player == 0:
        print('DRAW')
    elif player == 1:
        print('WON')
    elif player == 2:
        print('LOSE')
    else:
        print('PLAY NOT VALID!')
elif computer == 1: # PAPER
    if player == 0:
        print('LOSE')
    elif player == 1:
        print('DRAW')
    elif player == 2:
        print('WON')
    else:
        print('Play not valid')
elif computer == 2: # SCISSORS
    if player == 0:
        print('WON')
    elif player == 1:
        print('LOSE')
    elif player == 2:
        print('DRAW')
    else:
        print('Play not valid')


