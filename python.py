import random

number = random.randint(1, 100);
guess = 0;

while (guess != number):
    guess = int(input("Enter a Guess: "));
    if (guess < number):
        print("You Picked the lower number!");
    elif (guess > number):
        print("You Picked a higher number!");
    else:
        print("You Won!");
