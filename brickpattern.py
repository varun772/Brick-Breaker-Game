from random import randint
from numpy import add, diff
from brick import *
#from random import randinit

def Brickpattern(display,array,level,ans1,array1,array2,final1,addition,array3,array4,array5):
    if(level[0]==0):
        var = 0
        for i in range(5,25,5):
            k = (25 - 5)/5
            v = (25 - i)/5
            k = int(k)
            v = int(v)
            dif = k-v
            for n in range(var,dif+1,1):
                if (array[n] <= n):
                    if(n==3):
                        if(array[n]==3):
                            kim1 = 1
                        if(array[n]==2):
                            kim1 = 2
                        if(array[n]==1):
                            kim1 = 3
                        if(array[n]==0):
                            kim1 = 4
                    if(n==2):
                        if(array[n]==0):
                            kim1 = 3
                        if(array[n]==1):
                            kim1 =2
                        if(array[n]==2):
                            kim1= 1
                    if(n==1):
                        if(array[n]==0):
                            kim1 = 2
                        if(array[n]==1):
                            kim1 =1
                    if(n==0):
                        if(array[n]==0):
                            kim1=1
                    for j in range(5,10,3):
                        if((i+addition) >= 27):
                            print("GAME OVER")
                            return 10 
                        b1 = Brick(i+addition,j)
                        b1.printbrick(display,kim1)
            var =var +1
        if(7+addition >=27):
            print("GAME OVER")
            return 10
        b2 = Brick(7+addition,27)
        b4 = Brick(7+addition,50)
        kim5 = 5
        if (ans1 == 0):
            kim6 = randint(1,4)
        else:
            kim6 = array[11]
        #print(kim6) 
        b2.printbrick(display,kim5)
        b4.printbrick(display,kim6)
        for i in range(16,20,4):
                for j in range(30,120,12):
                    if(array[7]==0):
                        if(i+addition >= 27):
                            print("GAME OVER")
                            return 10
                        b3 = Brick(i+addition,j)
                        kim1 =3
                        b3.printbrick(display,kim1)
        return kim6
    if(level[0]==1):
        for i in range(20,24,4):
            for j in range(22,154,11):
                    if(array1[j]>0):
                        if((i+addition)>=27):
                            print("GAME OVER")
                            return 10
                        b3 = Brick(i+addition,j)
                        if(array1[j]==2):
                            kim1 = 2
                        else:
                            kim1 =1
                        b3.printbrick(display,kim1)
        for i in range(16,20,4):
            for j in range(22,154,11):
                if(array2[j]>0):
                    if((i+addition)>=27):
                        print("GAME OVER")
                        return 10
                    b3 = Brick(i+addition,j)
                    if(array2[j]==3):
                        kim1 = 3
                    elif(array2[j]==2):
                        kim1 = 2
                    else:
                        kim1 = 1
                    b3.printbrick(display,kim1)
        if(7+addition >= 27):
            print("GAME OVER")
            return 10
        b4 = Brick(7+addition,50)
        if(final1 == 0):
            kim1 = randint(1,4)
        else:
            kim1 = array2[11]
        b4.printbrick(display,kim1)
        return kim1
    if(level[0] == 2):
        kim1 = 0
        for i in range(20,24,4):
            for j in range(22,154,11):
                if(array3[j]>0):
                    if((i+addition)>=27):
                        print("GAME OVER")
                        return 10
                    b3 = Brick(i+addition,j)
                    if(array3[j]==2):
                        kim1 = 2
                    else:
                        kim1 =1
                    b3.printbrick(display,kim1)
        for i in range(16,20,4):
            for j in range(22,154,11):
                if(array4[j]>0):
                    if((i+addition)>=27):
                        print("GAME OVER")
                        return 10
                    b3 = Brick(i+addition,j)
                    if(array4[j]==3):
                        kim1 = 3
                    elif(array4[j]==2):
                        kim1 = 2
                    else:
                        kim1 = 1
                    b3.printbrick(display,kim1)
        for i in range(12,16,4):
            for j in range(22,154,11):
                if(array5[j]>0):
                    if((i+addition)>=27):
                        print("GAME OVER")
                        return 10
                    b3 = Brick(i+addition,j)
                    if(array5[j]==4):
                        kim1 =4
                    elif(array5[j]==3):
                        kim1 = 3
                    elif(array5[j] == 2):
                        kim1 =2
                    else:
                        kim1 = 1
                    b3.printbrick(display,kim1)
        for i in range(8,12,4):
            for j in range(44,99,11):
                if((i+addition)>=27):
                    print("GAME OVER")
                    return 10
                b3 = Brick(i+addition,j)
                kim = 1
                b3.printbrick(display,kim)
        return kim1
             #print(k) 