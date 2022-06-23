#making a snake water gun game using random module
import random
#taking the input from the user
print("Enter 'water','snake' or 'gun'")
user_input = input("Enter your choice: ")
#generating a random number
random_number = random.randint(1,3)
list_of_choices = ["match Tied ","You won the game","You lost the game"]
print(list_of_choices[random_number-1])
