from CalculaterModule import *
print("WELCOME TO THE CALCULATOR")
menu="1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponential  \n6. Exit\n----------------------------------\nTerminal based program for doing basic algebra. \n Slect the respective options for calculation \n"
print(menu)
while True:
    while True:
        sel=int(input("Enter your choice:"))
        if sel>6 or sel<1:
            print("Enter a number between 1 to 6")
        else:
            break
    if sel==1:
        add()
    elif sel==2:
        subt()
    elif sel==3:
        mult()
    elif sel==4:
        div()
    elif sel==5:
        power()
    elif sel==6:
        print("Thank you for using the program. \nHave a nice day.")
        break
    print(menu)
