from http.cookies import SimpleCookie
from multiprocessing import parent_process
import random


roc = rock
liz = lizard
spo = spock
pap = paper
sco = scissors

def play():
    user = input("Choose your move wisely (roc pap sci spo liz): ")
    computer = random.choice(['roc, pap, sci, liz, spo'])

    if user == computer:
        return "Tie"
    if is_win(user, computer):
        return "You won!"
    return "You lost!"

def is_win(player, opponent):
    if (       (player == 'roc' or player == 'spo' and opponent == 'sci')
            or (player == 'liz' or player == 'sci' and opponent == 'pap')
            or (player == 'spo' or player == 'pap' and opponent == 'roc')
            or (player == 'roc' or player == 'sci' and opponent == 'liz')
            or (player == 'pap' or player == 'liz' and opponent == 'spo')
        ):
        return True

print(play())