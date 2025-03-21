from cmu_graphics import *
import random

class Strawberry:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://www.etsy.com/listing/1164308595/strawberry-svg-strawberry-cut-file
        self.url ='/Users/ved/Desktop/Term Project/Pictures/Strawberry.png'
    
    def drawStrawberry(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
        
    def rotateAngle(self):
        self.angle += 4

class StrawberrySlice:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://pngtree.com/freepng/strawberry-slice-cartoon-pattern_7648962.html
        self.url ='/Users/ved/Desktop/Term Project/Pictures/strawberrySlice.png'
    
    def drawStrawberrySlice(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4