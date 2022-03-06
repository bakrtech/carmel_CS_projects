myDict = {'c#': 2, 'Javascript': 1, 'Python': 8, 'C++': 1, 'Java': 4}
updateDict = {"Scala"  : 10, "Python" : 17}
print("Dictionary = ", end = " ")
print(myDict)
print('Another dictionary through which I have to update the given dictionary is: ',updateDict)
for sub in myDict:
    if sub in updateDict:
        myDict[sub]  = updateDict[sub]
print("Updated dictionary = ", end = " ")
print(myDict)
