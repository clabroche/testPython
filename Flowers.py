from Observer import *
from Observable import *
class Flowers(Observable):
    def __init__(self, name, nbLeaf = 10):
        Observable.__init__(self)
        self.name = name
        self.nbLeaf = nbLeaf
    
    def cutLeaf(self): 
        if self.nbLeaf > 0:
            self.nbLeaf = self.nbLeaf - 1
            self.notify(self)
        else:
            self.nbLeaf = 0
    
    def reinitLeafs(self):
        self.nbLeaf = 10
        self.notify(self)