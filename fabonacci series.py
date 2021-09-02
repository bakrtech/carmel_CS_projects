t =int(input("how many terms? (enter 2+ value only): "))
f =0
s = 1
print("/n fibonacci series is: ")
print(f,",",s,end=",")
for i in range(2,t):
    third = f +s
    f =s
    s = third
    print(s,end=" , ")

