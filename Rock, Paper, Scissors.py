import random

def play():
    user = input("Choose one:\n Ro = Rock \n Pa = Paper \n Sc = Scissors \n").lower()
    computer = random.choice(["ro", "pa", "sc"])

    if user == computer:
        return "¡Draw!"

    if win(user, computer):
        return "¡You won!"

    return "¡You lost!"


def win(player, opponent):
    if ((player == "ro" and opponent == "sc")
        or (player == "sc" and opponent == "pa")
        or (player == "pa" and opponent == "ro")):
        return True
    else:
        return False


print(play())
