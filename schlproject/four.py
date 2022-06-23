#Write a functions that convert meter to cm and vice versa
def cmtom(a):
    return a* 100

def mtocm(b):
    return b/100

def metertofeet(c):
    return c* 3.2

def feettometer(d):
    return d/3.2
#Main Block
#ask user to enter the choice
print("1. Convert cm to m \n2. Convert m to cm \n 3. Convert meter to feet \n 4. Convert feet to meter")
choice=int(input("Enter your choice: "))
#ask user to enter the value
value=float(input("Enter the value: "))
#call the function
if choice==1:
    print(cmtom(value),"m")
elif choice==2:
    print(mtocm(value),"cm")
elif choice==3:
    print(metertofeet(value),"feet")
elif choice==4:
    print(feettometer(value),"meter")
else:
    print("Invalid choice")
print("Thank you for using the program")

