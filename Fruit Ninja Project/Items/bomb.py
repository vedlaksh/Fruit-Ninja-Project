from cmu_graphics import *
import random

class Bomb:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 90
    
    def drawBomb(self):
        drawCircle(self.x, self.y, 25, fill = 'black')
        drawRect(self.x, self.y, 7, 65, fill = 'black', rotateAngle = self.angle, align = 'center')
        drawRect(self.x, self.y, 7, 60, fill = 'black', rotateAngle = 45 + self.angle, align = 'center')
        drawRect(self.x, self.y, 7, 60, fill = 'black', rotateAngle = -45 + self.angle, align = 'center')
        drawRect(self.x, self.y, 7, 65, fill = 'black', rotateAngle = 90 + self.angle, align = 'center')
        drawRect(self.x, self.y, 43, 8, fill = 'purple', rotateAngle = 45 + self.angle, align = 'center')
        drawRect(self.x, self.y, 43, 8, fill = 'purple', rotateAngle = -45 + self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4