example_string = "Hello World"
print(len(example_string))

print(example_string.capitalize())

print(example_string.count('l'))
print(example_string.count('l',4,10))
print(example_string.count('l',3    ))

sub = "ll"
example_string.find(sub)

print(example_string.isalnum())

print()
string2 = "1234"
print(string2.isalnum())
# space is not a digit

print()
string3 ='abcdefghijklmnopqrstuvwxyz'
print(example_string.isalpha())
print(string2.isalpha())
print(string3.isalpha())

print()
print(example_string.isdigit())
print(string2.isdigit())
print(string3.isdigit())

print()

print(example_string.islower())
print(string2.islower())
print(string3.islower())
print()
string4 = "ASDFGHJKL"
print(string4.isupper())
print(string3.isupper())
print()
string5= "    is loking good"
print(string5.lstrip())
print(string5.rstrip())
print(string5.strip())
print()
string6 = "CARMEL CONVENT SCHOOL "
print(string6.title())
print()
string7 = "bye everyone"
print(string7.replace("bye","hi"))