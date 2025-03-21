from cmu_graphics import *
import random

class Apple:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = random.randint(0, 180)

        #Citation : https://www.istockphoto.com/vector/red-apple-gm506670795-45158274
        self.url ='/Users/ved/Desktop/Term Project/Pictures/Apple.png'
    
    def drawApple(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
        
    def rotateAngle(self):
        self.angle += 4

class AppleSlice:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://www.redbubble.com/i/sticker/Pixel-Apple-Slice-pixel-food-art-by-LittleFoodShop/147108677.EJUG5
        self.url ='/Users/ved/Desktop/Term Project/Pictures/appleSlice.png'
    
    def drawAppleSlice(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4