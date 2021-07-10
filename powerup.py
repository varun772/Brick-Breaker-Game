import os
import numpy as np
import sys
import termios
import tty
import signal
from colorama import Fore, init,Back, Style


def powerup(display,x,y,powerups,array1,arrayr):
    if(powerups  == 1):
         display[x-1][y] = '|'
