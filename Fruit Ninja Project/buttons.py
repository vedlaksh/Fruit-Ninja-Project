from cmu_graphics import *

class BackButton:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.border = 'grey'
        self.opacity = 50
        self.angle = angle
    
    def drawBackButton(self):
        #Citation: https://www.freeiconspng.com/img/41946
        whiteArrow = '/Users/ved/Desktop/Term Project/Pictures/back.png'

        drawCircle(self.x, self.y, 20, fill = None, border = self.border, borderWidth = 3)
        drawImage(whiteArrow, self.x, self.y, rotateAngle = self.angle, align = 'center', opacity = self.opacity)

class NextPageButton:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.border = 'grey'
        self.opacity = 50
        self.angle = angle
    
    def drawNextPageButton(self):
        #Citation: https://www.freeiconspng.com/img/41946
        whiteArrow = '/Users/ved/Desktop/Term Project/Pictures/back.png'

        drawImage(whiteArrow, self.x, self.y, rotateAngle = self.angle, align = 'center', opacity = self.opacity, width = 30, height = 30)
        drawCircle(self.x, self.y, 25, fill = None, border = self.border, borderWidth = 3)

class HowToPlayButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border = 'grey'
        self.fill = 'grey'
    
    def drawHowToPlayButton(self):
        drawCircle(self.x, self.y, 20, fill = None, border = self.border, borderWidth = 3)
        drawLabel("?", self.x, self.y, fill = self.fill, size = 30, bold = True)

class PauseButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.border = 'grey'
    
    def drawPauseButton(self):
        drawRect(self.x, self.y, 35, 35, fill = None, border = self.border, borderWidth = 3, align = 'center')
        drawRect(self.x - 7, self.y, 10, 23, fill = None, border = self.border, borderWidth = 2, align = 'center')
        drawRect(self.x + 7, self.y, 10, 23, fill = None, border = self.border, borderWidth = 2, align = 'center')
