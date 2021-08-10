for i in range(6):
    print()
    for j in range(6):
        print()
        print(j, end='' )

print("")
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print("")

for i in range(1,6):
    c =65
    for j in range(i):
        print(chr(c),end=" ")
        c +=1
    print("")
c =65
for i in range(1,6):
    for j in range(i):
        print(chr(c),end=" ")
    c +=1

    print("")
