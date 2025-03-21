from cmu_graphics import *
import random

class Watermelon:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = random.randint(0, 180)

        #Citation: https://pearlyarts.com/product/whole-watermelon-clipart/#google_vignette
        self.url ='/Users/ved/Desktop/Term Project/Pictures/Watermelon.png'
    
    def drawWatermelon(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
          
    def rotateAngle(self):
        self.angle += 4

class WatermelonSlice:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://minecraft.fandom.com/wiki/Melon_Slice
        self.url ='/Users/ved/Desktop/Term Project/Pictures/sliceWatermelon.png'
    
    def drawWatermelonSlice(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4