import math
def prime():
    for i in range(2,100):
        if(i ==2 ):
            print(i,end=" ")
            continue
        flag = False
        for j in range(2,math.ceil(i/2)+1):
            if(i%j== 0):
                flag = True
                break
            
        if(not flag):
            print(i,end=" ")

prime()