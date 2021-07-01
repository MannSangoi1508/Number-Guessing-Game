import random
chances = 5
number = random.randint(1,9)
while chances > 0:
    guess = int(input("Enter Your Guess Number: "))
    
    if guess == number:
        print("You Won!")
        break

    if guess > number:
        print("Your Number Is High")
        
    if guess < number:
        print("Your Number Is Low")


    chances = chances -1

if chances == 0:
    print("You Lost")