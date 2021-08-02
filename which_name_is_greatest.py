a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    if a > c:
        print(a," Is the greatest ")
if b > a:
    if b > c:
        print(b," is the greatest")
if c > a:
    if c > b:
        print(c," is the greatest")
if a == b == c:
    print("all are equal" )