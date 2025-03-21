from cmu_graphics import *
import random

class Banana:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = random.randint(0, 180)

        #Citation: https://www.istockphoto.com/vector/vector-single-cartoon-banana-gm521504766-91378167
        self.url ='/Users/ved/Desktop/Term Project/Pictures/Banana.png'
    
    def drawBanana(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
        
    def rotateAngle(self):
        self.angle += 4

class BananaSlice:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://www.vecteezy.com/vector-art/48963000-pixel-graphic-banana-illustration-isolated-on-white-background-fruit-pixelated-for-the-pixel-art-game-and-icon-for-website-game
        self.url ='/Users/ved/Desktop/Term Project/Pictures/bananaSlice.png'
    
    def drawBananaSlice(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4