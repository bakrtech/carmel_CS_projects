for i in range(3):
    salary = int(input("Enter your salary here:"))
    DA =(125/100)*salary
    HRA =(10/100)*salary
    ALLOWNS = (15/100)*salary

    GROSS_INCOME = DA+HRA+ALLOWNS

    DEDCUTION = (12/100)*GROSS_INCOME

    NET_INCOME = GROSS_INCOME - DEDCUTION
    print("The value of  i is ",i)
    print("YOUR GROSS INCOME IS ",GROSS_INCOME,"AND NET INCOME IS ",NET_INCOME)
print("THANK YOU FOR USING THE SALARY CALCULATOR!")