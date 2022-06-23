print("Enter five numbers below")
num1 =float(input("First number"))
num2 =float(input("Second number"))
num3 =float(input("Third number"))
num4 =float(input("Fourth number"))
num5 =float(input("Fifth number"))
divisor = float(input("Enter the divisor"))
count = 0
print("multiples of",divisor," are:")
reminder = num1%divisor
if reminder == 0:
    print(num1)
    count+=1
reminder = num2%divisor
if reminder == 0:
    print(num2)
    count+=1
reminder = num3%divisor
if reminder == 0:
    print(num3)
    count+=1
reminder = num4%divisor
if reminder == 0:
    print(num4)
    count+=1
reminder = num5%divisor
if reminder == 0:
    print(num5)
    count+=1
print()
print(count,"multiples of", divisor,"found ")