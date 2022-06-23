#Write a functions that convert meter to cm and vice versa
def cmtom(cm):
    """CONVERTS CENTIMETERS TO METERS"""
    return cm* 100
def mtocm(m):
    """CONVERTS METERS TO CENTIMETERS"""
    return m/100
def metertofeet(m):
    """CONVERTS METERS TO FEET"""
    return m* 3.2
def feettometer(feet):
    """CONVERTS FEET TO METERS"""
    return feet/3.2
print("1. Convert cm to m \n2. Convert m to cm \n 3. Convert meter to feet \n 4. Convert feet to meter")
choice=int(input("Enter your choice: "))
value=float(input("Enter the value: "))
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

