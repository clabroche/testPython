from Observer import *
from tkinter import *
class FlowerViewGraphic(Observer):
    def __init__(self, flower, ui):
        flower.register(self)
        self.flower = flower
        self.ui = ui
        self.fenetre = ui.fenetre
        self.champ_label = Label(self.fenetre, text="Flower has {} leafs".format(flower.nbLeaf))
        self.champ_label.pack()
        b = Button(self.fenetre, text="Recreate all leafs", command=flower.reinitLeafs)
        b.pack()


    def update(self):
        if self.ui.finish != True:
            self.champ_label['text'] = 'Flower has {} leafs'.format(self.flower.nbLeaf)
