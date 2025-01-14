def getAndDisplay(n):
    marks = input("Enter the marks for  students : ")
    split = marks.split()
    marklist = [float(i) for i in split]
    for mark in marklist:
        print(mark)

print(getAndDisplay(3))