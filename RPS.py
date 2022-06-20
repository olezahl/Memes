import random

def play():
    user = input("Choose your move wisely (roc pap sci spo liz): ")
    computer = random.choice(['roc'])

    if user == computer:
        return "Tie"
    if is_win(user, computer):
        return "You won!"
#    if is_loss(user, computer):
#        return "You lost!"
    return "You lost!"

def is_win(player, opponent):
    if ((       player == 'roc' or player == 'spo' and opponent == 'sci')
            or (player == 'liz' or player == 'sci' and opponent == 'pap')
            or (player == 'spo' or player == 'pap' and opponent == 'roc')
            or (player == 'roc' or player == 'sci' and opponent == 'liz')
            or (player == 'pap' or player == 'liz' and opponent == 'spo')):
        return True

#def is_loss(opponent, player):
#    if (opponent == 'roc' or 'spo' and player == 'sci') or (opponent == 'liz' or 'sci' and player == 'pap') or (opponent == 'spo' or 'pap' and player == 'roc') or (opponent == 'roc' or 'sci' and player == 'liz') or (opponent == 'pap' or 'liz' and player == 'spo'):
#       return True

print(play())