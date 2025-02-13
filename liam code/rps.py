def player():
    global a
    global b
    a = input("Rock, Paper, Scisors?\n> ").lower()
    if a == "r":
        a = "rock"
    elif a == "p":
        a = "paper"
    elif a == "s":
        a = "scisors"
    else:
        print("That's not RPS!\n\n")
        if input("\nTry again? (Y/N)\n> ").lower() == "y":
            print("\n")
            a = ""
            player()
        else:
            quit()

def computer():
    global b
    from random import randint
    b = randint(1, 3)
    if b == 1:
        b = "rock"
    elif b == 2:
        b = "paper"
    elif b == 3:
        b = "scisors"

def check_winner(a, b):
    print(f"\nYou chose: {a.capitalize()}\nComputer chose: {b.capitalize()}\n")
    if a != b:
        if a == "rock" and b == "scisors":
            return "You win!"
        elif a == "paper" and b == "rock":
            return "You win!"
        elif a == "scisors" and b == "paper":
            return "You win!"
        else:
            print("You lose!")
    elif a == b:
        return "It's a tie"

if player() == "rock" or "paper" or "scisors":
    if computer() == 1 or 2 or 3:
        print(check_winner(a, b))
