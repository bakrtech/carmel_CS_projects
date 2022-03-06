x=eval(input('Enter a tuple/list: '))
y=eval(input('Enter the element to be searched: '))
print('Given element is: ',y)
if y in x:
    print('The given element is present in the list/tuple')
if y not in x:
    print('The given element is not present in the list/tuple')
