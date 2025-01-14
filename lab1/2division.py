def findPercentage(n):
    if n>=80:
        print("distinction")
    elif n>=65:
        print("first division")
    elif n>=55:
        print("second division")
    elif n>=40:
        print("third divison")
    else:
        print("fail")


percentage = int(input("enter the persentage : "))
findPercentage(percentage)