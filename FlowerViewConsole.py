from Observer import *
class FlowerViewConsole(Observer):
    def __init__(self, flower): 
        flower.register(self)
        self.flower = flower
    def update(self): 
        print('repaint console', self.flower.nbLeaf)
