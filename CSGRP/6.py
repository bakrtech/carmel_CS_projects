users = {'ram' : 'Admin' , 'shaam' : 'Staff' , 'aam' : 'Manager'}
print('The dictionary is: ',users)
key = input("Enter the key to be searched: ")
if key in users.keys(): 
    print("value : ", users[key])
else :
    print("Please enter valid key \nList of keys : ")
    for val in users.keys():
        print(val, end = " ")
