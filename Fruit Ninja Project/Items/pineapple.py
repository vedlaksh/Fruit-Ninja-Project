from cmu_graphics import *
import random

class Pineapple:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = random.randint(0, 180)

        #Citation: https://www.istockphoto.com/vector/pineapple-icon-pineapple-tropical-fruit-vector-illustration-gm1398251835-452452738
        self.url ='/Users/ved/Desktop/Term Project/Pictures/Pineapple.png'

    def drawPineapple(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
        
    def rotateAngle(self):
        self.angle += 4
    
class PineappleSlice:
    def __init__(self, x, y, xv, yv):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.angle = 0

        #Citation: https://www.redbubble.com/i/sticker/Pixel-Pineapple-Slice-pixel-food-art-by-LittleFoodShop/147155392.EJUG5
        self.url = '/Users/ved/Desktop/Term Project/Pictures/pineappleSlice.png'
    
    def drawPineappleSlice(self):
        drawImage(self.url, self.x, self.y, rotateAngle = self.angle, align = 'center')
    
    def rotateAngle(self):
        self.angle += 4