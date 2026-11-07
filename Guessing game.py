import random

x=int(input("Enter a number between 1 to 100:"))

Number_1= random.randint(1,100)

print(Number_1)

if x>Number_1:
    print("Your number is too high")
elif x<Number_1:
    print("Your number is too low")
else:
    print("You guessed it right")


print("The number was:",Number_1)

print("Thanks for playing the game")