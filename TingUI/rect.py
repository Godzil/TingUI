class Rect:
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.x0 = x
        self.y0 = y
        self.w = w
        self.h = h
        self.x1 = 0
        self.x2 = 0
        
    def setPos(self, x, y):
        self.x0 = x
        self.y0 = y
        self.x1 = self.x0 + self.w
        self.y1 = self.y0 + self.h

    def resize(self, w, h):
        self.h = h
        self.w = w
        self.x1 = self.x0 + self.w
        self.y1 = self.y0 + self.h