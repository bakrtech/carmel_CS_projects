myTuple1 = (2, 7)
myTuple2 = (5, 9)
print("Elements of tuple 1 are " + str(myTuple1))
print("Elements of tuple 2 are " + str(myTuple2))
pairList = [(a, b) for a in myTuple1 for b in myTuple2]
pairList = pairList + [(b, a) for a in myTuple1 for b in myTuple2]
print("All pair combination list is " + str(pairList))
