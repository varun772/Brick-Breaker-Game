#direct imports
#from brickpattern import brickpattern
import numpy as np
import os
import time
from colorama import init,Fore,Back,Style
from time import sleep

#imports from files
from paddle import Paddle
from input import *
from ball import Ball
#from brick import *
from brickpattern import Brickpattern
from powerup import powerup
#from screen import screen
#from playsound import playsound



#code
#print(os.name)
rows = os.get_terminal_size().lines
columns = os.get_terminal_size().columns

#os.system('date')
display = np.full((30,200),Back.BLACK+" ")
#print(rows)
#print(columns)
lives = 3
new_paddle = Paddle()
new_ball = Ball()
 
x = round(27)
y= round(5)

x1 = round(26)
y1 = round(9.5)

timestart = time.time()
released = 0
ans = 0
final =0 
final1 = 0
array = [0] * 25
array1 = [2] *180
array2 = [3] * 180
array3 = [2] * 180
array4 = [3] * 180
array5 = [4] * 180
level = [0] * 3
randarray = [0]*10000
addition = 0
Brickpattern(display,array,level,final,array1,array2,final1,addition,array3,array4,array5)
arrayl =[[0]*2]*1000
arrayr =[[0]*2]*1000
arrayufo = [0] * 10000000
reverse = 1
reverse1 = 1
scorec = 0
sorec1 = 0
sum1 = 0
powerups = 0
play = "s1.wav"
play1 = "s2.wav"
play3 = "s3.wav"
count = 0
releasetime = 0
arrayufo[1] = 10
arrayufo[2] = 5
arrayufo[3] = 10
arraycount = [1]*10
while True:
        sum = 0
        inputkey = user_input()
        if inputkey == "q":
            break
        if inputkey == "a":
            y = Paddle.movel(y)
            if released == 0:
                y1 = Ball.moveball(y)
        if inputkey == "d":
            y = Paddle.mover(y)
            if released == 0:
                y1 = Ball.moveball(y)
        if inputkey == " ":
            released = 1
            releasetime = time.time()
        if inputkey == "n":
            y = round(5)
            x1 = round(26)
            y1 = round(9.5)
            released = 0
            if(level[0]== 2):
                print("GAME OVER")
                break
            level[0] = 2
        if inputkey == "p":
            powerups = 1
            powerupsstart = time.time()
        if inputkey == "l":
            array3 = [0] * 180
            array4 = [0] * 180
            array5 = [0] * 180  
        #x1 = x1 - 2
        #y1 = y1 + 2
        if(time.time()-releasetime>=5 and time.time()-releasetime<=15):
            if(released !=0):
                if(x1==x-1 and (y1>=y and y1<=y+10)):
                    count = count + 1
        if(time.time()-releasetime>5):
            if(released != 0):
                addition = 2 * count
        if (released == 1):
            #playsound('myfile.mp3')
            #os.system("myfile.mp3")
            if(x1<=1):
                os.system("aplay s2.wav -q &")
                reverse = 1
            if(x1>=26 and (y1>=y and y1<=y+10)):
                    reverse = -1
                    if(y1<y+5):
                        os.system("aplay s2.wav -q &")
                        reverse1 = -1
                    if(y1>y+5):
                        os.system("aplay s2.wav -q &")
                        reverse1 = 1
                    if(y1==y+5):
                        os.system("aplay s2.wav -q &")
                        reverse1 = 0 
            if(y1<=1):
                os.system("aplay s2.wav -q &")
                reverse1 = 1
            if(y1>=150):
                os.system("aplay s2.wav -q &")
                reverse1 = -1
            if(x1>=28 and lives == 0):
                os.system("aplay s3.wav -q &")
                break
            var =0
            #level[0] = 1
            if (level[0] == 0):
                for i in range(5,25,5):
                    if((y1>=5 and y1<=18)):
                        k = (25 - 5)/5
                        v = (25 - i)/5
                        k = int(k)
                        v = int(v)
                        dif = k-v
                        for n in range(var,dif+1,1):  
                            if(array[n] <= n):
                                if(x1-(i+addition)==1):
                                    os.system("aplay s1.wav -q &")
                                    reverse = 1
                                    array[n] = array[n]+1
                                if(x1-(i+addition)==-1):
                                    os.system("aplay s1.wav -q &")
                                    reverse = -1
                                    array[n] = array[n]+1
                                var = var + 1
                for i in range(16,20,4):
                    for j in range(30,120,12):
                        if(y1>=j and y1<=j+10):
                            if(x1-(i+addition)==1):
                                if (array[7]==0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = 1
                                array[7]=15
                            if(x1-(i+addition)==-1):
                                if (array[7]==0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = -1
                                array[7]=15
                if(y1>=27 and y1<=40):
                    if(x1-(7+addition) == 1):
                        os.system("aplay s1.wav -q &")
                        reverse = 1
                    if(x1-(7+addition)==-1):
                        os.system("aplay s1.wav -q &")
                        reverse = -1
                if(y1>=50 and y1<=60):
                    if(x1-(7+addition) == 1):
                        final = 1
                        if(array[11]>0):
                            os.system("aplay s1.wav -q &")
                            reverse= 1
                        array[11] = array[11] - 1
                    if(x1-(7+addition)==-1):
                        final = 1
                        if(array[11]>0):
                            os.system("aplay s1.wav -q &")
                            reverse = -1
                        array[11] = array[11] - 1
            if(level[0]==1):
                print("fun")
                for i in range(20,24,4):
                    for j in range(22,154,11):
                        if(y1>=j and y1<=j+10):
                            if(x1-(i+addition)==1):
                                if(array1[j]>0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = 1
                                    array1[j]=array1[j]-1
                            if(x1-(i+addition)==-1):
                                    if(array1[j]>0):
                                        os.system("aplay s1.wav -q &")
                                        reverse = -1
                                        array1[j] = array1[j]-1
                for i in range(16,20,4):
                    for j in range(22,154,11):
                        if(y1>=j and y1<=j+10):
                            if(x1-(i+addition)==1):
                                if(array2[j]>0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = 1
                                    array2[j] = array2[j] - 1
                            if(x1-(i+addition)==-1):
                                if(array2[j]>0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = -1
                                    array2[j] = array2[j] - 1
                    if(y1>=50 and y1<=60):
                        if(x1-(7+addition)==1):
                            final1 = 1
                            if(array2[11]>0):
                                os.system("aplay s1.wav -q &")
                                reverse= 1
                                array2[11] = array2[11] - 1
                        if(x1-(7+addition)==-1):
                            final1 = 1
                            if(array2[11]>0):
                                os.system("aplay s1.wav -q &")
                                reverse = -1
                                array2[11] = array2[11] - 1
            if(level[0] == 2):
                for i in range(20,24,4):
                    for j in range(22,154,11):
                        if(y1>=j and y1<=j+10):
                            if(x1-(i+addition)== 1):
                                if(array3[j]>0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = 1
                                    array3[j]=array3[j]-1
                            if(x1-(i+addition)== -1):
                                    if(array3[j]>0):
                                        os.system("aplay s1.wav -q &")
                                        reverse = -1
                                        array3[j] = array3[j]-1
                for i in range(16,20,4):
                    for j in range(22,154,11):
                        if(y1>=j and y1<=j+10):
                            if(x1-(i+addition)==1):
                                if(array4[j]>0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = 1
                                    array4[j] = array4[j] - 1
                            if(x1-(i+addition)==-1):
                                if(array4[j]>0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = -1
                                    array4[j] = array4[j] - 1
                for i in range(12,16,4):
                    for j in range(22,154,11):
                        if(y1>=j and y1<=j+10):
                            if(x1-(i+addition)==1):
                                if(array5[j]>0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = 1
                                    array5[j] = array5[j] - 1
                            if(x1-(i+addition)==-1):
                                if(array5[j]>0):
                                    os.system("aplay s1.wav -q &")
                                    reverse = -1
                                    array5[j] = array5[j] - 1
                for i in range(8,12,4):
                    for j in range(44,99,11):
                        if(y1>=j and y1 <= j+10):
                            if(x1 - (i+addition)==1):
                                reverse = 1
                            if(x1 - (i+addition) == -1):
                                reverse = -1
                if((arrayufo[0]-y1)>=-8 and (arrayufo[0]-y1<=0)):
                    if(arrayufo[3] > 0):
                        if(x1-6 == 1):
                            reverse = 1
                            arrayufo[3] = arrayufo[3]-1
                        if(x1-6 == -1):
                            reverse = -1
                            arrayufo[3] = arrayufo[3]-1
                        if(arrayufo[3] <=8):
                            if(arraycount[1] > 0 ):
                                if(x1-7 == -1):
                                    reverse = -1
                                    arraycount[1] = arraycount[1] - 1
                                if(x1-7 == 1):
                                    reverse = 1
                                    arraycount[1] = arraycount[1] - 1
                            if(arraycount[1]>0):
                                if(x1-5 == -1):
                                    reverse = -1
                                    arraycount[0] = arraycount[0] - 1
                                if(x1-5 == 1):
                                    reverse = 1
                                    arraycount[0] = arraycount[0] - 1
                            if(arraycount[2]>0):
                                if((arrayufo[0]-y1>= -7) and (arrayufo[0]-y1 <= -4)):
                                    if(x1-7==1):
                                        reverse1 = -1
                                        arraycount[2] = arraycount[2] - 2
                            if(arraycount[3]>0):
                                if((arrayufo[0]-y1>= -4) and (arrayufo[0]-y1 <= 0)):
                                    if(x1-7==-1):
                                        reverse1 = 1
                                        arraycount[3] = arraycount[3] -1
                        
            x1 = x1 + reverse
            y1 = y1 + reverse1
            if (x1>=28 and lives>0):
                lives = lives -1
                y = round(5)
                x1 = round(26)
                y1 = round(9.5)
                released = 0
            #if ((time.time()-timestart >= 16 and time.time()-timestart <=16.4) or (time.time()-timestart >= 46 and time.time()-timestart <=46.4)):
        for i in range(10):
            sum = sum + array[i]
        for i in range(22,154,11):
            sum = sum + (3 - array1[i])
            sum = sum + (3 - array2[i])
        #print(released)
        #if(time.time()-timestart >= 16):
        if((sum >= 15 and sum<=15.4 and level[0]==0) or (sum == 27 and level[0]==0)): 
            level[0]=1
            count = 0
            released = 0
            y = round(5)
            x1 = round(26)
            y1 = round(9.5)
        if((((sum >=20 and sum<=20.4) and level[0]==1)) or ((sum >=30 and sum<=30.4) and level[0]==1)):
            level[0]=2
            released = 0
            count = 0
            y = round(5)
            x1 = round(26)
            y1 = round(9.5)
        if(lives == 0):
            break
        os.system("clear")
        #print(array)
        display[x:x+1,y:y+10]=new_paddle.getshape()
        Paddle.powerups(display,x,y,powerups,arrayl,arrayr)
        display[x1:x1+1,y1:y1+1]=new_ball.getballshape()
        if(level[0]==2):
            arrayufo[0] = Paddle.ufo(display,arrayufo,x,y,arraycount)
        for row in display:
           print("".join(row))
        display = np.full((30,200),Back.BLACK+" ")
        ans = Brickpattern(display,array,level,final,array1,array2,final1,addition,array3,array4,array5)
        if ans == 10 :
            break
        if (final == 0):
            array[11] = ans
            scorec = ans
        if(final1 ==0):
            array2[11] = ans
            sorec1 = ans
        #print(array[11])
        #print(scorec)
        #print(level[0])
        #print(sum)
        #print((time.time()-timestart))
        print(Fore.GREEN+'time {0:.3f}'.format(time.time()-timestart),end="   ")
        print(Fore.GREEN+'score = ',sum,end="  ") 
        #print(released)
        print(Fore.GREEN+'No of lives remaining',lives,end="  ")
        print(Fore.GREEN+'LEVLE ',level[0],end="  ")
        if(level[0]==2):
            print(Fore.GREEN+'Score of UFO',arrayufo[3],end=" ")
        #powerup(display,x,y,powerups,arrayl,arrayr)
        #print(level[0])
        #print(array1)
        #print(array2)
        #print(ans)
        #print(released)
        #print(sum1)
        #print(level[0])
        #print(released)
        #print(count)
        #print(addition)
        #print(arrayufo[3])
        #print(y1)
        #print(arrayufo[0])
        #print("\n")
        #print(y1)
        #print(arrayufo[0]-y1)
        #print(x1)
        #print(array3)
        #print(array4)
        #print(array5)
        #print(arraycount)
        #print("\n")
        #print(y1)
        #print(x1-(7+addition))
        print("\n")
