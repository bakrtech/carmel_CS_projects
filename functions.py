"""
Two types of functions:
1 user defined
2 in built functions
"""
def formula_add():  #function definition
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))
    c = a+b
    return c
sm =  formula_add()# function calling

print("The sum of  a and b is ",sm)

# multiple assignment of  a variable
d=e=f=12
# assigning multiple values to multiple variable
d,e,f =10,12,14
print(d," ",e," ",f)

d,e=e,d
print("d = ",d,' and of e is ',e)

d,e,f = d+1,e+1,f+1
print("d = ",d,' and of e is ',e," and of f =",f)

x =10
y,y =x+2,x+5
print(x,y)

x,x=20,30
y,y =x+10,x+30
print(x,y)

x =10
y = x/2
print(x,y)
print(type(x))
print(type(y))
print(type("class XI A"))

