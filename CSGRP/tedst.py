Ntuple = int(input("How many tuple do you want to enter? "))
Mt = []
for i in range(Ntuple):
    a=tuple(input("Enter a tuple: "))
    Mt.append(a)
l=0
dic= []
for i in range(len(Mt)):
    d=len(Mt[i])
    dic.append(Mt[i])
dic.sort()
print(dic)