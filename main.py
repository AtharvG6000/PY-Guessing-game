import random

def computer_choice(upper_limit):
    print(f"If the guess is correct enter C \n If its higher then , H \n If its lower then L")
    print(f"Lets go!")
    lower_limit = 1
    noOfGuesses = 0
    temp = 0
    C = True
    while(C):
        guess = random.randrange( lower_limit,upper_limit)
        print(f"Is it {guess} ?" )
        feedBack = input()
        noOfGuesses = noOfGuesses + 1
        if feedBack == 'C':
            C = False
            temp = guess
        elif feedBack == 'H':
            lower_limit = guess
        elif feedBack == 'L':
            upper_limit = guess
    if noOfGuesses <= 5:
        print("See , Computer are better than humans")
    elif noOfGuesses <= 10:
        print("Took some time but I got it")
    elif noOfGuesses > 10:
        print(f"{temp} is my unlucky number actually , thats why I avoided it")
        

computer_choice(100)
    