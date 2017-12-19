from Flowers import *
from FlowerViewConsole import *
from FlowerViewGraphic import *
from UIGraphics import *
from threading import Timer
import signal


# Set the signal handler


try:
    threadUI = UI()
    threadUI.daemon=True
    threadUI.start()
    while(threadUI.init != True):
        pass
    flower = Flowers('camelia')

    FlowerViewConsole(flower)
    FlowerViewGraphic(flower, threadUI)

    def cutAndWait(): 
        if threadUI.finish != True:
            flower.cutLeaf()
            Timer(1, cutAndWait).start()

    cutAndWait()


except ():
    print("attempting to close threads. Max wait =")
    threadUI.join()
    print("threads successfully closed")


