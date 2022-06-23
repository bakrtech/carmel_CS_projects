user_input = str(input("Enter the string: "))
def count(word):
    upper,lower,numbers,special=0,0,0,0
    for i in range(len(word)):
        if word[i].islower():
            lower+=1
        elif word[i].isupper():
            upper +=1
        elif word[i].isdigit():
            numbers +=1
        else:
            special +=1
    print("Upper case letters: ",upper)
    print("lower Case letters: ",lower)
    print("Nubers ",numbers)
    print("Other special characters :" ,special)
count(user_input)
