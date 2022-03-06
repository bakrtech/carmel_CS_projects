Friend=[]
NFrined = int(input("How many friends do you have? "))
for i in range(0,NFrined):
    Name = str(input("What is your friend's name? "))
    Friend.append(Name)
# Friend = eval(input('Enter the names in the form of list:'))
First_letter ={}
for i in range(0,len(Friend)):
    d=Friend[i][0]
    if len(First_letter) != 0:
        for j in First_letter:
            if d ==j:
                First_letter[j] +=1
                a=1
            else:
                a=0
        if a ==0:
            First_letter[d]=1
    else:
        First_letter[d]=1
print(First_letter)
