def add():
    s=0
    n=int(input("Enter the amount of numbers to be added:"))
    for i in range(n):
        num=int(input("Enter the number to be added:"))
        s=s+num
    print("The sum is:", s,"\n---------------------------")

def subt():
    s1=int(input("Enter the first number:"))
    s2=int(input("Enter the second number:"))
    print("The subtracted number is:", s1-s2,"\n---------------------------")

def mult():
    prod=1
    p=int(input("Enter the amount of numbers to be multiplied:"))
    for k in range(p):
        num2=int(input("Enter the number to be multiplied:"))
        prod=prod*num2
    print("The product is:", prod,"\n---------------------------")

def div():
    dividend=int(input("Enter the dividend:"))
    divisor=int(input("Enter the divisor:"))
    quo=dividend//divisor
    if dividend%divisor!=0:
        print("The quotient is", quo, "and the remainder is", dividend%divisor)
    else:
        print("The quotient is:", quo,"\n---------------------------")

def power():
    n1=int(input("Enter the number to be exponented:"))
    n2=int(input("Enter the exponent value:"))
    num3=pow(n1, n2)
    print("The result is:", num3,"\n---------------------------")
