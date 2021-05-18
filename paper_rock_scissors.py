import random


def play():
    user_choice = input("Type in 'rock' ; 'paper' or 'scissors'")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user_choice == computer:
        return "It's a tie"

    if is_win(user_choice, computer):
        return 'You won!'

    return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') \
            or (player == 'paper' and opponent == 'rock'):
        return True


print(play())
print("press any key to exit")
input()
# Made by Omar Sarsar @Zeinot on github // Zeinotgaming@gmail.com
