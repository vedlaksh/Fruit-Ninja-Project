from cmu_graphics import *
import random

class Kiwi:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = random.randint(0, 180)

        #Citation: https://www.istockphoto.com/photo/kiwi-fruit-isolated-gm1347811814-425201025?searchscope=image%2Cfilm
        self.url ='/Users/ved/Desktop/Term Project/Pictures/Kiwi.png'
    
    def drawKiwi(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
        
    def rotateAngle(self):
        self.angle += 4

class KiwiSlice:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://www.redbubble.com/i/sticker/Pixel-Kiwi-Slice-pixel-food-art-by-LittleFoodShop/147110028.EJUG5
        self.url ='/Users/ved/Desktop/Term Project/Pictures/kiwiSlice.png'
    
    def drawKiwiSlice(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4