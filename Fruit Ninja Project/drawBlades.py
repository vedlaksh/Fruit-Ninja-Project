from cmu_graphics import *

def drawBlade(app):
    #Draws "Classic" blade.
    if app.classicBlade == True:
        drawCircle(app.cx, app.cy, 8, fill = 'crimson')

    #Draws "Magenta Rush" blade.
    elif app.magentaRushBlade == True:
        for i in range(len(app.magentaRush)):
            x, y = app.magentaRush[i]
            drawCircle(x, y, 8, fill = 'magenta', opacity = (10 * i))

    #Draws "Rainbow Rampage" blade. 
    elif app.rainbowRampageBlade == True:
        for i in range(len(app.rainbowRampage)):
            x, y, color = app.rainbowRampage[i]
            drawCircle(x, y, 8, fill = color)
    
    #Draws "Shape Fury" blade.
    elif app.shapeFuryBlade == True:
         for i in range(len(app.shapeFury)):
            x, y, shape, color = app.shapeFury[i]
            if shape == 'triangle':
                drawRegularPolygon(x, y, 15, 3, fill = color, align = 'center')
            elif shape == 'square':
                drawRect(x, y, 25, 25, fill = color, align = 'center')
            elif shape == 'pentagon':
                drawRegularPolygon(x, y, 15, 5, fill = color, align = 'center')
            elif shape == 'circle':
                drawCircle(x, y, 15, fill = color)
            elif shape == 'septagon':
                drawRegularPolygon(x, y, 15, 7, fill = color, align = 'center')  

    #Draws "Particle Party" blade. 
    elif app.particlePartyBlade == True:
        for i in range(len(app.particleParty)):
            x, y, color, particleSize, opacity = app.particleParty[i]
            drawCircle(x, y, particleSize, fill = color, opacity = opacity)

def drawBladePlayer1(app):
    #Draws player 1's blade. 
    for i in range(len(app.bladePlayer1)):
            x, y = app.bladePlayer1[i]
            drawCircle(x, y, 8, fill = 'pink')

def drawBladePlayer2(app):
     #Draws player 2's blade. 
     for i in range(len(app.bladePlayer2)):
            x, y = app.bladePlayer2[i]
            drawCircle(x, y, 8, fill = 'lightGreen')

