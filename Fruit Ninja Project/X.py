from cmu_graphics import *

#Class for first strike on game screen. 
class firstStrike:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border = 'lightBlue'
        self.fill = 'blue'
    
    def drawStrike(self):
        drawRect(self.x, self.y, 35, 12, border = self.border, borderWidth = 2.5, 
                 fill = self.fill, rotateAngle = 47, align = 'center')
        drawRect(self.x, self.y, 35, 12, border = self.border, borderWidth = 2.5, 
                 fill = self.fill, rotateAngle = -47, align = 'center')
        drawRect(self.x, self.y, 12, 5, fill = self.fill, rotateAngle = -47, align = 'center')
        drawRect(self.x, self.y, 12, 5, fill = self.fill, rotateAngle = 47, align = 'center')
    
    def shade(self):
        self.border = 'red'
        self.fill = 'red'

#Class for second strike on game screen. 
class secondStrike:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border = 'lightBlue'
        self.fill = 'blue'
    
    def drawStrike(self):
        drawRect(self.x + 40, self.y, 50, 15, border = self.border, borderWidth = 3, 
                 fill = self.fill, rotateAngle = 47, align = 'center')
        drawRect(self.x + 40, self.y, 50, 15, border = self.border, borderWidth = 3, 
                 fill = self.fill, rotateAngle = -47, align = 'center')
        drawRect(self.x + 40, self.y, 15, 8, fill = self.fill, rotateAngle = -47, align = 'center')
        drawRect(self.x + 40, self.y, 15, 8, fill = self.fill, rotateAngle = 47, align = 'center')
    
    def shade(self):
        self.border = 'red'
        self.fill = 'red'

#Class for third strike on game screen. 
class thirdStrike:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border = 'lightBlue'
        self.fill = 'blue'
    
    def drawStrike(self):
        drawRect(self.x + 90, self.y, 60, 18, border = self.border, borderWidth = 3, 
                 fill = self.fill, rotateAngle = 47, align = 'center')
        drawRect(self.x + 90, self.y, 60, 18, border = self.border, borderWidth = 3, 
                 fill = self.fill, rotateAngle = -47, align = 'center')
        drawRect(self.x + 90, self.y, 21, 12, fill = self.fill, rotateAngle = -47, align = 'center')
        drawRect(self.x + 90, self.y, 21, 12, fill = self.fill, rotateAngle = 47, align = 'center')
    
    def shade(self):
        self.border = 'red'
        self.fill = 'red'