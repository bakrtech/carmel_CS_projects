#This a program that converts dollar to ruppes or ruppes to dollar 
menu="1  Dollar to ruppes ($ to ruppes) \n 2  ruppes to Dollar (ruppes to $)\n e  exit \n h  help"
print(menu)
def dollarToRuppes(a):
    return a*65
def ruppesToDollar(b):
    return b/65
while True:
    usr_inpt=str(input("What is your input: "))
    if usr_inpt =='1':
        while True:
            dlr = input("Enter the amount in dollar $")
            if dlr.isnumeric():
                print("The amount in ruppes ",dollarToRuppes(int(dlr)))
                break
            else:
                print("ENTER NUMBERS ONLY !")
    elif usr_inpt =='2':
        while True:
            dlr = input("Enter the amount in INR ruppes ",)
            if dlr.isnumeric():
                print("The amount in dollar ",ruppesToDollar(int(dlr)))
                break
            else:
                print("ENTER NUMBERS ONLY !")
    elif usr_inpt=='e':
        break
    elif usr_inpt =="h":
        print(menu)
    else:
        print("WRONG INPUT!!")
    print(menu)
