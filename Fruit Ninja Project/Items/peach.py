from cmu_graphics import *
import random

class Peach:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://www.istockphoto.com/vector/isolated-peach-illustration-gm630020582-112280117
        self.url ='/Users/ved/Desktop/Term Project/Pictures/Peach.png'
    
    def drawPeach(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
        
    def rotateAngle(self):
        self.angle += 4

class PeachSlice:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://illustoon.com/?id=8282
        self.url ='/Users/ved/Desktop/Term Project/Pictures/peachSlice.png'
    
    def drawPeachSlice(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4