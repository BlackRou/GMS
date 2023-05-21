import random

def rps():
    valid_choices = ['r', 'p', 's']

    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors!\n")
        if user in valid_choices:
            break
        else:
            print("Invalid choice! Please enter 'r', 'p', or 's'.")

    computer = random.choice(valid_choices)

    if user == computer:
        return f"It's a tie, computer picked {computer}!"

    if is_win(user, computer):
        return f"You lost! The computer picked {computer}!"
    else:
        return f"You won! The computer picked {computer}!"

def is_win(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r
    return (player == 's' and opponent == 'r') or \
           (player == 'p' and opponent == 's') or \
           (player == 'r' and opponent == 'p')

print(rps())
