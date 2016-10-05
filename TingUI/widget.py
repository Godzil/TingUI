from .rect import Rect

class Widget:
    """ Base class for all type of UI widgets """
    def __init__(self):
        self.bound = Rect()

    def setPos(self, x, y):
        self.bound.setPos(x, y)
        
    def resize(self, w, h):
        self.bound.resize(w, h)
