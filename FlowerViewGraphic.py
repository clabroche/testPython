from Observer import *
from tkinter import *
class FlowerViewGraphic(Observer):
    def __init__(self, flower, ui):
        flower.register(self)
        self.flower = flower
        self.ui = ui
        self.fenetre = ui.fenetre
        self.champ_label = Label(self.fenetre, text="Flower has {} petals".format(flower.nbLeaf))
        self.champ_label.pack()
        b = Button(self.fenetre, text="Recreate all petals", command=flower.reinitLeafs)
        b.pack()


    def update(self):
        if self.ui.finish != True:
            text = ""
            if self.flower.nbLeaf > 1 :
                text = 'Flower has {} petals'.format(self.flower.nbLeaf)
            else:
                text = 'Flower has {} petal'.format(self.flower.nbLeaf)
            self.champ_label['text'] = text
                
