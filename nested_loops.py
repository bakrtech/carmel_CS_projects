"""
This is a little advaced for loops
TRY IT
"""
for i in range(12):
    print(" ")
    for j in range(5):
        print("{",i,",",j,"} ,",end=" ")

"""TRIANGLE MOUNTAIN OF ASTRICKS(*)"""
for i in range(5):
    for j in range(i+1):
        print('*',end="")
    print("")




times = int(input("enter the no. of lines required"))

for i in range(times):
    print("")
    for j in range(i+1):
        print('*',end="")



for i in range(5):
    for j in range(3):
        print(i,j,end="  ")
    print()