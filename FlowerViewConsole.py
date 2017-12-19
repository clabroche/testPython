from Observer import *
class FlowerViewConsole(Observer):
    def __init__(self, flower): 
        flower.register(self)
        self.flower = flower
    def update(self): 
        text = ""
        if self.flower.nbLeaf > 1:
            text = 'Flower has {} petals'.format(self.flower.nbLeaf)
        else:
            text = 'Flower has {} petal'.format(self.flower.nbLeaf)
        print(text)
