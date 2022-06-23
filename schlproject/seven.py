#Program that genrates a number with n digits with each digit random not starting with 0
import random
def randomNumberGenrator(a):
    output=""
    firstdigit=random.randint(1,9)
    output = output +str(firstdigit)
    for i in range(1,a):
        d =random.randint(0,9)
        output=output+str(d)
    print(output)
#Main Block
usr_inpt=int(input("ENTER THE NUMBER OF DIGITS: "))
randomNumberGenrator(usr_inpt)
