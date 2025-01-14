string = input("Enter a string: ")
newString = ""
for i in string:
    if i.isupper():
        newString += i.lower()
    else:
        newString += i.upper()
print(newString)
