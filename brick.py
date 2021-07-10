import os
import numpy as np
import sys
import termios
import tty
import signal
from colorama import Fore, init,Back, Style


class Brick():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.lenght = 10


    def printbrick(self,display,kim):
            for j in range(self.lenght):
                if(kim == 1):
                    display[self.x][self.y+j] = Back.GREEN+'b' + Style.RESET_ALL
                if(kim == 2):
                    display[self.x][self.y+j] = Back.RED+'b' + Style.RESET_ALL
                if(kim == 3):
                    display[self.x][self.y+j] = Back.WHITE+'b' + Style.RESET_ALL
                if(kim == 4):
                    display[self.x][self.y+j] = Back.YELLOW+'b' + Style.RESET_ALL
                if(kim == 5):
                   display[self.x][self.y+j] = Back.GREEN+'b' + Style.RESET_ALL
                #print(self.x)
                #print(self.y)


