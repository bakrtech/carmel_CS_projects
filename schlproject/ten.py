#random number gusser game
import random
#taking the input from the user
number = int(input("Enter a number between 1 and 100: "))
#generating a random number
random_number = random.randint(1,100)
#checking if the number is correct
if number == random_number:
    print("You guessed the correct number!")
#checking if the number is too high
elif number > random_number:
    print("Your guess is too high!")
#checking if the number is too low
elif number < random_number:
    print("Your guess is too low!")
#checking if the number is not in the range
else:
    print("Your guess is not in the range!")
#printing the random number
print("The random number was:", random_number)
