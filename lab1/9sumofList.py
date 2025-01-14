def sumofList(vals):
    count = 0
    for val in vals:
        count+=val
    return count

vals = input("Enter n numbers: ")
vals= vals.split()
vals = [int(val) for val in vals]
print(sumofList(vals))