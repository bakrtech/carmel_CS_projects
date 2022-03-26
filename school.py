#function
def Partern_1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j," ",end="")
        print("\n",end="")
def Partern_2(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i," ",end="")
        print("\n")
def fabonaci(n):
    a=1
    b=2
    print(a,b,end=" ")
    if n>2:
        for i in range(2,n+1):
            c=a*b
            a=b
            b=c 
            print(b,end=" ")
#main block
a = int(input("HOW MUCH TIMES?  "))
print("partern 1 \n")
Partern_1(a)
print("partern 2 \n")
Partern_2(a)
print("fabonaci")
fabonaci(a)
