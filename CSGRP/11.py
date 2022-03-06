x=tuple(input('Enter the tuple which has subtuples: '))
print(x)
y=[]
for i in range(len(x)):
	z=len(x[i])
	y.append(z)
l=tuple(y)
print('The required tuple is: ', l)	
