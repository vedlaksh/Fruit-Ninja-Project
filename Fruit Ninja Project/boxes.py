from cmu_graphics import *

class BladeBoxes:
    def __init__(self, x, y):
        self.cx = x
        self.cy = y
        self.width = 200
        self.height = 325
        self.fill = 'grey'
    
    def drawBladeBox(self):
        drawRect(self.cx, self.cy, self.width, self.height, fill = self.fill, border = 'black', borderWidth = 3, align = 'center')

class BombBar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border = 'lightBlue'
        self.fill = 'blue'
    
    def drawBombBar(self):
        drawRect(self.x, self.y, 25, 120, fill = self.fill, border = self.border, borderWidth = 3, align = 'center')