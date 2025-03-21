from cmu_graphics import *
import random

class Pear:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = random.randint(0, 180)

        #Citation: https://stock.adobe.com/images/green-pear-fruit-flat-vector-illustration-logo-icon-clipart/532454533?asset_id=532454533
        self.url ='/Users/ved/Desktop/Term Project/Pictures/Pear.png'
    
    def drawPear(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
        
    def rotateAngle(self):
        self.angle += 4

class PearSlice:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://www.gettyimages.com/detail/illustration/pears-cartoon-icon-vector-design-royalty-free-illustration/1220599228?adppopup=true
        self.url ='/Users/ved/Desktop/Term Project/Pictures/pearSlice.png'
    
    def drawPearSlice(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4