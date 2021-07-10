from colorama import Fore,init,Back,Style
import os
import numpy as np

class Ball:
    def __init__(self):
        self.shape = np.array("o")
    
    def getballshape(self):
        return self.shape

    def moveball(var):
        return var + 5
    