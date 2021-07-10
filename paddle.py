import os
import numpy as np
import sys
import termios
import tty
import signal
from colorama import Fore, init,Back, Style


class Paddle():
    def __init__(self):
        self._basicshape =  np.array(
            [
                [Back.RED+'-']
            ]
        )
    def getshape(self):
        return self._basicshape
    
    def mover(var):
        if(var+10 <=200):
            return var+3
        else:
            return var-3

    def movel(var):
        if(var>2):
            return var-3
        elif (var ==2):
            return var
        else:
            return 2
    def powerups(display,x,y,powerups,arrayl,arrayr):
        if(powerups  == 1):
         display[x-1][y] = '|'
         display[x-1][y+9] = '|'

    def ufo(display,array,x,y,arraycount):
            if(y-array[0]>0):
                display[6][array[0]+1] ="  /___   ___\ ____________________"
                y1 = array[0] + 1
            elif(y-array[0]<0):
                display[6][array[0]-1] = "  /___   ___\ ____________________"
                y1= array[0] -1 
            else:
                display[6][array[0]] = "  /___   ___\ ____________________"
                y1 = array[0]     
            if(array[3]<=8):
                if(arraycount[1]<=0):
                    display[5][y1] = "______" 
                if(arraycount[0]<=0):
                    display[7][y1] = "______"
                if(arraycount[2] > 0):
                    display[5][y1-2] = "|"
                    display[6][y1-2] = "|"
                    display[7][y1-2] = "|"
                if(arraycount[3] > 0):
                    display[5][y1+2] = "|"
                    display[6][y1+2] = "|"
                    display[7][y1+2] = "|"
            return y1    