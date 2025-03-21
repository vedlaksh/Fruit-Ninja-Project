from cmu_graphics import *
import math

#Determines if the fruit/bomb has been cut. 
def inFruit(mouseX, mouseY, x, y):
    return distance(mouseX, mouseY, x, y) <= 25

#Determines if the press was within the button. 
def inButton(mouseX, mouseY, x, y, radius):
    return distance(mouseX, mouseY, x, y) <= radius

#Helper function for inFruit and inButton.
def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

#Determines if the cursor is hovering above the blade box. 
def inBladeBox(mouseX, mouseY, cx, cy, width, height):
    top = cy - (height // 2)
    bottom = cy + (height // 2)
    left = cx - (width // 2)
    right = cx + (width // 2)
    return ((left <= mouseX <= right) and (top <= mouseY <= bottom))

#Spins game mode titles on start screen. 
def printGameModes(label, count, cx, cy):
    for i in range(len(label)):
        angle1 = math.radians((i * 15) + (count * 1))
        angle2 = math.radians((i * 15) + (count * 1) + 180)
        x1, y1 = getXandY(cx, cy, angle1, 57)
        x2, y2 = getXandY(cx, cy, angle2, 57)
        drawLabel(label[i], x1, y1, fill = 'white', size = 17, bold = True, font = 'Gang of Three')
        drawLabel(label[i], x2, y2, fill = 'white', size = 17, bold = True, font = 'Gang of Three')

#Helper for printGameModes. 
def getXandY(cx, cy, angle, radius):
    x = cx + (radius * math.sin(angle))
    y = cy - (radius * math.cos(angle))
    return (x, y)
