esum =0
a = int(input("enter the starting limit of even number: "))
b = int(input("enter the end limit of even number: "))

for even in range(a,b):
    if even%2 ==0:
        esum = esum + even
print("The sum of even of num between ",a," and ",b," is"
                        ,esum)