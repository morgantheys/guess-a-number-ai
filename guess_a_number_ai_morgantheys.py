# Guess A Number AI
#
# Morgan Theys
# 9/9/2016

import random

def splash_screen():
    print(" _____ _      _                 _   _                 _               ")
    print("|  __ (_)    | |        /\     | \ | |               | |              ")        
    print("| |__) |  ___| | __    /  \    |  \| |_   _ _ __ ___ | |__   ___ _ __ ")
    print("|  ___/ |/ __| |/ /   / /\ \   | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|")
    print("| |   | | (__|   <   / ____ \  | |\  | |_| | | | | | | |_) |  __/ |   ")  
    print("|_|   |_|\___|_|\_\ /_/    \_\ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   ")
    print()

def show_credits():
    print("Created by Morgan Theys 9/13/2016")
    
def play():
    global Name
    
    print("Type in your Name")
    Name = input()
    print("Hello, " + Name + ", think of a number from 1 to 100 and I will try to guess it.")
    input("Press ENTER to play.")
    
    low = 1
    high = 100
    got_it = False

    got_it = False
    limit = 7
    tries = 0
    
    num = random.randint(1, 100)

    lower_responses = ["lower", "low", "l", "loower", "Lower", "Low", "L", "LoWeR"]
    higher_responses = ["high", "higher", "h", "High", "Higher", "H", "HiGhEr"]
    yes_responses = ["correct", "Correct", "Yes", "yes", "y", "Y", "yee yee", "YeS"]

    while got_it == False:
        #calculate guess
        guess = (high + low) // 2

        #computer asks
        answer = input("Is it " + str(guess) +", " + Name + "?")

        #adjust range
        if answer in higher_responses:
            low = guess + 1
        elif answer in lower_responses:
            high = guess - 1
        elif answer in yes_responses:
            got_it = True

    print("Woohoo, " + Name + ", I Got It!!!")


def play_again():
    while True:
        answer = input("Would you like to play again, " + Name + "?")

        if answer == 'no' or answer == 'n' or answer == 'No' or answer == 'N' or answer == 'nO':
            return False
        elif answer == 'yes' or answer == 'y' or answer == 'YeS' or answer == 'yee yee' or answer == 'Yes' or answer == 'Y':
            return True

        print("What?!!!" + Name +", just say yes or no.")


# start here
splash_screen()

again = True

while again:
    play()
    again = play_again()

show_credits()
