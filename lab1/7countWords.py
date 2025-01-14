def findwords(sent):
    words= sent.split()
    return len(words)
sent = input("Enter a sentence : ")
print("The numbers of words is : ",findwords(sent))