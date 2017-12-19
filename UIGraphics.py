from tkinter import *
import random
import sys
from threading import Thread
import time

class UI(Thread):
    def __init__(self): 
        Thread.__init__(self)
        self.init = False
        self.finish = False

    def run(self):
        self.fenetre = Tk()
        self.init = True
        self.fenetre.mainloop()
        self.finish = True


