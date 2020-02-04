#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      milo
#
# Created:     16/01/2020
# Copyright:   (c) milo 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import random
    list = ["rock", "paper", "scissors"]
    c_guess = random.choice(list)
    p_guess = input("type rock, paper or scissors\n")
    if p_guess in ("rock","paper","scissors"):
        print(c_guess)
        if p_guess == c_guess:
            print("draw")
        elif (p_guess == "rock" and c_guess == "scissors") or (p_guess == "paper" and c_guess == "rock") or (p_guess == "scissors" and c_guess == "paper"):
            print("%s beats %s you win!"%(p_guess, c_guess))
        else:
            print("%s beats %s you lost!"%(c_guess, p_guess))
    else:
        print("Wrong input")



if __name__ == '__main__':
    main()
