test_tup = (10, 4, 5, 6, 8)
print("The original tuple : " + str(test_tup))
N = int(input("value to be checked:")) 
res = False 
for ele in test_tup : 
    if N == ele : 
        res = True
        break 
    print("Does it contain the required value ? : " + str(res))
