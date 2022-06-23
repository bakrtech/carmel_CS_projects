#Write a program in python to implent buble sort using function named BSORT wher the unsorted list
def Bsort(tlist):
    n=len(tlist)
    for i in range(n):
        for j in range(0,n-1):
            if tlist[j] > tlist[j+1]:
                tlist[j],tlist[j+1]=tlist[j+1],tlist[j]
#Main Block
usr_list = eval(input("Enter the unsorted list:"))
Bsort(usr_list)
print(usr_list)
