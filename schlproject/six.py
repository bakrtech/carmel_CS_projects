#Write a program that calculate the square and cubes using function
def square(a):
    return a*a
def cube(a):
    return a*a*a
#Main block
while True:
    a=input("ENTER THE NUMBER")
    if a.isnumeric():
        print(f"The squre is {square(a)} \nThe Cube is {cube(a)} ")
        break
    else:
        print("ENTER  NUMBERS ONLY!!!")
