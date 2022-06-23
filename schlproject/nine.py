#Write a program in python to implement Insersion sor using a function named as Isort where the unsorted list is passed as parameter
def Isort(a):
    for i in range(1,len(a)):
        k=a[i]
        j=i-1
        while j>=0 and k < a[j]:
            a[j+1]=a[j]
            j=j-1
        else:
            a[j+1] =k
#Main Block
usr_lst=eval(input("Write your List"))
Isort(usr_lst)
print("The odered list is ", usr_lst)
