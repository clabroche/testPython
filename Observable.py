from Observer import *

class Observable:
    def __init__(self): 
        self.observers = []

    def register(self, observer):
        if isinstance(observer, Observer):
            self.observers.append(observer)
    def notify(self, observable): 
        for observer in self.observers:
            observer.update()