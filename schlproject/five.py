#Write a program that gives information about a box including Volume TSA LSA
def Volume(lenght,width,height):
    return lenght*width*height 
def TSA(lenght,width,height):
    return 2*((lenght*width)+(width*height)+(height*lenght))
def LSA(lenght,width,height):
    return 2*height*(lenght+width)
#Main block
while True:
    height = input("ENTER THE HEIGHT OF BOX: ")
    width = input("ENTER THE WIDTH OF BOX: ")
    lenght  = input("ENTER THE LENGHT OF BOX: ")
    if height.isnumeric() and width.isnumeric() and lenght.isnumeric():
        height=int(height)
        lenght=int(lenght)
        width=int(width)
        break
    else:
        print("ENTER NUMBERS ONLY")
print(f"The Volume of the box is {Volume(height,width,lenght)}\nThe TSA of the box is {TSA(lenght,width,height)} \nThe LSA of the box is {LSA(lenght,width,height)}")
