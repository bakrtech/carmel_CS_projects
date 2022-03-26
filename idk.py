import random
times=0
itemss={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
range_times=int(input("How much times=> "))
for i in range(range_times):
    a=random.randint(0,10)

    for i  in  itemss:
        if i == a:
            itemss[i]+=1

        
for i in itemss:
    print(i,"==>",itemss[i])
print("The END")
