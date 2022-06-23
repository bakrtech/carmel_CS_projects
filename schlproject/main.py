import twelve
#getting the input from the user
print("Enter 'kg','tonne','pound'")
user_input = input("Enter your choice: ")
#checking if the user input is correct
if user_input == "kg":
    print("Enter the weight in kg: ")
    weight = float(input())
    print("The weight in tonne is: ", twelve.kgtotonne(weight))
    print("The weight in pound is: ", twelve.kgtopound(weight))
elif user_input == "tonne":
    print("Enter the weight in tonne: ")
    weight = float(input())
    print("The weight in kg is: ", twelve.tonnekg(weight))
    print("The weight in pound is: ", twelve.kgtopound(weight))
elif user_input == "pound":
    print("Enter the weight in pound: ")
    weight = float(input())
    print("The weight in kg is: ", twelve.poundtokg(weight))
    print("The weight in tonne is: ", twelve.kgtotonne(weight))
