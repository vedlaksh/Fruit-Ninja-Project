from cmu_graphics import *
import csv
import random
from gravity import Gravity
from launch import Launch
from launch import LaunchMultiplayer
from Items.bomb import Bomb
from Items.strawberry import Strawberry
from Items.pineapple import Pineapple
from Items.watermelon import Watermelon
from Items.peach import Peach
from Items.banana import Banana
from Items.pear import Pear
from Items.kiwi import Kiwi
from Items.apple import Apple
from Items.strawberry import StrawberrySlice
from Items.pineapple import PineappleSlice
from Items.watermelon import WatermelonSlice
from Items.peach import PeachSlice
from Items.banana import BananaSlice
from Items.pear import PearSlice
from Items.kiwi import KiwiSlice
from Items.apple import AppleSlice
from X import firstStrike
from X import secondStrike
from X import thirdStrike
from boxes import BladeBoxes
from boxes import BombBar
from buttons import BackButton
from buttons import HowToPlayButton
from buttons import PauseButton
from buttons import NextPageButton
from helpers import inFruit
from helpers import inButton
from helpers import printGameModes
from helpers import inBladeBox
from drawBlades import drawBlade
from drawBlades import drawBladePlayer1
from drawBlades import drawBladePlayer2
from draw import drawBackground
from draw import drawBackgroundMultiplayer

def onAppStart(app):
    startApp(app)
    resetGame(app)

def resetGame(app):
    app.scorePlayer1 = 0
    app.scorePlayer2 = 0
    app.fruitCutPlayer1 = 0
    app.fruitCutPlayer2 = 0
    app.xCountPlayer1 = 0
    app.xCountPlayer2 = 0
    app.bombDeployCountPlayer1 = 0
    app.bombDeployCountPlayer2 = 0

    app.delayMultiplayer = 0

    app.multiplayerTimer = 90

    app.fruitFrequencyPlayer1 = 200
    app.bombFrequencyPlayer1 = 400

    app.fruitFrequencyPlayer2 = 200
    app.bombFrequencyPlayer2 = 400

    app.fruitsPlayer1 = []
    app.slicedFruitPlayer1 = []
    app.bombsPlayer1 = []

    app.fruitsPlayer2 = []
    app.slicedFruitPlayer2 = []
    app.bombsPlayer2 = []

    app.fruits = []
    app.slicedFruit = []
    app.bombs = []

    app.delayClassic = 0

    app.score = 0
    app.xCount = 0
    app.fruitFrequency = 200
    app.bombFrequency = 400

def startApp(app):
    app.playerName = app.getTextInput('Enter player name:')

    app.stepsPerSecond = 1000000
    app.counterStart = 0
    app.counterClassic = 0
    app.counterMultiplayer = 0

    app.width = 500
    app.height = 500

    app.gameMode1 = 'Classic'
    app.gameMode2 = 'Multiplayer'
    app.gameMode3 = 'Locker'

    app.leaderboardClassic = False
    app.backButtonLeaderboardClassic = BackButton(25, 25, 180)

    app.leaderboardMultiplayer = False
    app.backButtonLeaderboardMultiplayer = BackButton(25, 25, 180)

    app.gameOverClassic = False
    app.gameOverMultiplayer = False

    app.gameMultiplayer = False
    app.pausedMultiplayer = False

    app.bombBarPlayer1 = BombBar(775, 200)
    app.bombBarPlayer2 = BombBar(775, 500)

    app.firstStrikePlayer1 = firstStrike(675, 35)
    app.secondStrikePlayer1 = secondStrike(675, 35)
    app.thirdStrikePlayer1 = thirdStrike(675, 35)
    app.firstStrikePlayer2 = firstStrike(675, 340)
    app.secondStrikePlayer2 = secondStrike(675, 340)
    app.thirdStrikePlayer2 = thirdStrike(675, 340)
    app.pauseButtonPlayer1 = PauseButton(30, 270)

    app.cxPlayer2 = 400
    app.cyPlayer2 = 450
    app.dxPlayer2 = 0
    app.dyPlayer2 = 0

    app.bladePlayer1 = []
    app.bladePlayer2 = []

    app.gameLocker = False
    app.backButtonLocker = BackButton(25, 25, 180)
    app.nextPageButton0 = NextPageButton(250, 465, 0)
    app.nextPageButton1 = NextPageButton(300, 465, 0)
    app.backPageButton1 = NextPageButton(200, 465, 180)
    app.backPageButton2 = NextPageButton(250, 465, 180)

    app.howToPlay = False
    app.backButtonHowToPlay = BackButton(475, 25, 0) 

    app.cx = 200
    app.cy = 200

    app.gameStart = True
    app.howToPlayButton = HowToPlayButton(25, 25)
    app.startStrawberry = Strawberry(100, 350, 0, 0)
    app.startPineapple = Pineapple(250, 350, 0, 0)
    app.startWatermelon = Watermelon(400, 350, 0, 0)

    app.gameClassic = False
    app.paused = False
    app.firstStrike = firstStrike(375, 35)
    app.secondStrike = secondStrike(375, 35)
    app.thirdStrike = thirdStrike(375, 35)
    app.pauseButtonClassic = PauseButton(30, 470)

    app.page = 0

    app.classicBladeBox = BladeBoxes(125, 275)
    app.magentaRushBladeBox = BladeBoxes(375, 275)
    app.rainbowRampageBladeBox = BladeBoxes(125, 275)
    app.shapeFuryBladeBox = BladeBoxes(375, 275)
    app.particlePartyBladeBox = BladeBoxes(250, 275)

    app.classicBlade = True
    app.magentaRushBlade = False
    app.rainbowRampageBlade = False
    app.shapeFuryBlade = False
    app.particlePartyBlade = False

    app.magentaRush = []
    app.rainbowRampage = []
    app.shapeFury = []
    app.particleParty = []

    #Citation: https://wall.alphacoders.com/big.php?i=1318895
    app.url = '/Users/ved/Desktop/Term Project/Pictures/Background.jpeg'
    #Citation: https://gallery.yopriceville.com/Free-Clipart-Pictures/Scrolls-PNG/Scroll_PNG_Clip_Art_Image-263687686
    app.pauseScreen = '/Users/ved/Desktop/Term Project/Pictures/Pause.png'
    #Citation: https://icons8.com/icons/set/restart--white
    app.restart = '/Users/ved/Desktop/Term Project/Pictures/restart.png'
    #Citation: https://www.cleanpng.com/png-ribbon-medal-clip-art-2964438/
    app.leaderboardGameOver = '/Users/ved/Desktop/Term Project/Pictures/leaderboard.png'
    #Citation: https://stock.adobe.com/search?k=red+banner&asset_id=456819036
    app.winnerBanner = '/Users/ved/Desktop/Term Project/Pictures/banner.png'

def redrawAll(app):
    if app.gameStart == True: 
        #Draw background.
        drawBackground(app)

        #Draw player name. 
        drawLabel(app.playerName, 450, 25, fill = 'white', size = 25, bold = True, font = 'Gang of Three')

        #Draw title.
        drawLabel("Fruit", 250, 80, fill = 'crimson', size = 100, bold = True, font = 'Gang of Three')
        drawLabel("Ninja", 250, 170, fill = 'white', size = 100, bold = True, font = 'Gang of Three')

        #Draw "How to Play" button. 
        app.howToPlayButton.drawHowToPlayButton()

        #Draw "Classic" game mode. 
        drawCircle(100, 350, 65, border = 'crimson', fill = None, borderWidth = 18)
        printGameModes(app.gameMode1, app.counterStart, 100, 350)
        app.startStrawberry.drawStrawberry()

        #Draw "Multiplayer" game mode. 
        drawCircle(250, 350, 65, border = 'crimson', fill = None, borderWidth = 18) 
        printGameModes(app.gameMode2, app.counterStart, 250, 350)
        app.startPineapple.drawPineapple()
        
        #Draw "Locker" game mode. 
        drawCircle(400, 350, 65, border = 'crimson', fill = None, borderWidth = 18)
        printGameModes(app.gameMode3, app.counterStart, 400, 350)
        app.startWatermelon.drawWatermelon()

        #Draw blade.
        drawBlade(app)
    
    if app.howToPlay == True:
        #Draw background.
        drawBackground(app)

        #Draw "How to Play" title. 
        drawLabel('How to Play', 250, 35, fill = 'crimson', size = 50, bold = True, font = 'Gang of Three')
        drawRect(250, 35, 325, 65, fill = None, border = 'crimson', borderWidth = 3, align = 'center')

        #Draw "Classic" subheading. 
        drawLabel('Classic', 250, 100, fill = 'black', size = 35, bold = True, font = 'Gang of Three')
        drawRect(250, 100, 150, 45, fill = None, border = 'black', borderWidth = 3, align = 'center')

        #Draw rules for "Classic" mode. 
        drawLabel('Slice fruit to increase score! Each missed fruit will', 250, 150, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('result in a strike. Slicing a bomb or recieving three', 250, 175, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('strikes will result in a loss. Aim to beat your', 250, 200, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('high score!', 250, 225, fill = 'white', size = 18, bold = True, font = 'Gang of Three')

        #Draw "Multiplayer" subheading. 
        drawLabel('Multiplayer', 250, 275, fill = 'black', size = 35, bold = True, font = 'Gang of Three')
        drawRect(250, 275, 225, 45, fill = None, border = 'black', borderWidth = 3, align = 'center')

        #Draw rules for "Multiplayer" mode.
        drawLabel('Compete against an opponent to see who can achieve', 250, 325, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('the higher score. Slice fruit to increase score! Each', 250, 350, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('missed fruit will result in a strike. Slicing a bomb will', 250, 375, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('reduce your score by five. Three strikes will set', 250, 400, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('your score back to zero. Slicing three fruit will allow', 250, 425, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('you to launch a bomb onto your opponents screen. The', 250, 450, fill = 'white', size = 18, bold = True, font = 'Gang of Three')
        drawLabel('highest score after the timer runs up wins!', 250, 475, fill = 'white', size = 18, bold = True, font = 'Gang of Three')

        #Draw back button.
        app.backButtonHowToPlay.drawBackButton()

        #Draw Blade. 
        drawBlade(app)

    if app.gameClassic == True:
        if app.paused:
            #Draw background.
            drawBackground(app)
            drawImage(app.pauseScreen, 250, 250, align = 'center')

            #Draw "Paused" label. 
            drawLabel('Paused', 250, 100, fill = 'brown', size = 50, bold = True, font = 'Gang of Three')

            #Draw current score. 
            scorePeachPaused = Peach(215, 175, 0, 0)
            scorePeachPaused.drawPeach()
            drawLabel(app.score, 285, 175, fill = 'brown', size = 50, bold = True, font = 'Gang of Three')

            #Authored with the help of ChatGPT.
            #Draw best score. 
            bestScore = 0
            with open('scores.csv', 'r') as file:
                reader = csv.reader(file)
                
                for row in reader:
                    if row:
                        score = (int)(row[0])
                        name = row[1]
                        if name.lower() == app.playerName.lower() and score > bestScore:
                            bestScore = score
                    
            drawLabel('Best:', 215, 235, size = 35, fill = 'brown', bold = True, font = 'Gang of Three')
            drawLabel(bestScore, 285, 235, fill = 'brown', size = 35, bold = True, font = 'Gang of Three')
    
            #Draw X that sends user to start screen. 
            drawRect(170, 325, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
            drawRect(170, 325, 42, 10, fill = 'white', rotateAngle = 47, align = 'center')
            drawRect(170, 325, 42, 10, fill = 'white', rotateAngle = -47, align = 'center')

            #Draw "restart" image that restarts classic game. 
            drawRect(250, 325, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
            drawImage(app.restart, 250, 325, align = 'center')

            #Draw play button that resumes game. 
            drawRect(330, 325, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
            drawRegularPolygon(327, 325, 22, 3, fill= 'white', rotateAngle = 90, align = 'center')

            #Draw blade.
            drawBlade(app)

        else:
            #Draw background.
            drawBackground(app)

            #Draw score. 
            scorePeach = Peach(45, 35, 0, 0)
            scorePeach.drawPeach()
            drawLabel(app.score, 100, 35, fill = 'red', size = 50, bold = True, font = 'Gang of Three')

            #Authored with the help of ChatGPT.
            # Draw best score.
            bestScore = 0
            with open('scores.csv', 'r') as file:
                reader = csv.reader(file)
                
                for row in reader:
                    if row:
                        score = (int)(row[0])
                        name = row[1]
                        if name.lower() == app.playerName.lower() and score > bestScore:
                            bestScore = score
                    
            drawLabel('Best:', 45, 75, size = 25, fill = 'red', bold = True, font = 'Gang of Three')
            drawLabel(bestScore, 100, 75, fill = 'red', size = 25, bold = True, font = 'Gang of Three')

            #Draw strikes. 
            app.firstStrike.drawStrike()
            app.secondStrike.drawStrike()
            app.thirdStrike.drawStrike()

            #Shade in strikes based on strike count. 
            if app.xCount == 0:
                app.firstStrike.border = 'lightBlue'
                app.firstStrike.fill = 'blue'
                app.secondStrike.border = 'lightBlue'
                app.secondStrike.fill = 'blue'
                app.thirdStrike.border = 'lightBlue'
                app.thirdStrike.fill = 'blue'
            elif app.xCount == 1:
                app.firstStrike.shade()
            elif app.xCount == 2:
                app.firstStrike.shade()
                app.secondStrike.shade()
            elif app.xCount == 3:
                app.firstStrike.shade()
                app.secondStrike.shade()
                app.thirdStrike.shade()

            #Draw pause button. 
            app.pauseButtonClassic.drawPauseButton()

            #Draw fruits. 
            for i in range(len(app.fruits)):
                fruit = type(app.fruits[i])
                if fruit == Apple:
                    app.fruits[i].drawApple()
                elif fruit == Banana:
                    app.fruits[i].drawBanana()
                elif fruit == Kiwi:
                    app.fruits[i].drawKiwi()
                elif fruit == Peach:
                    app.fruits[i].drawPeach()
                elif fruit == Pear:
                    app.fruits[i].drawPear()
                elif fruit == Pineapple:
                    app.fruits[i].drawPineapple()
                elif fruit == Strawberry:
                    app.fruits[i].drawStrawberry()
                elif fruit == Watermelon:
                    app.fruits[i].drawWatermelon()
            
            #Draw bombs. 
            for i in range(len(app.bombs)):
                app.bombs[i].drawBomb()

            #Draw slices. 
            for i in range(len(app.slicedFruit)):
                slicedFruit = type(app.slicedFruit[i])
                if slicedFruit == AppleSlice:
                    app.slicedFruit[i].drawAppleSlice()
                elif slicedFruit == BananaSlice:
                    app.slicedFruit[i].drawBananaSlice()
                elif slicedFruit == KiwiSlice:
                    app.slicedFruit[i].drawKiwiSlice()
                elif slicedFruit == PeachSlice:
                    app.slicedFruit[i].drawPeachSlice()
                elif slicedFruit == PearSlice:
                    app.slicedFruit[i].drawPearSlice()
                elif slicedFruit == PineappleSlice:
                    app.slicedFruit[i].drawPineappleSlice()
                elif slicedFruit == StrawberrySlice:
                    app.slicedFruit[i].drawStrawberrySlice()
                elif slicedFruit == WatermelonSlice:
                    app.slicedFruit[i].drawWatermelonSlice()

            #Draw blade.
            drawBlade(app)
    
    if app.leaderboardClassic == True:
        #Draw background.
        drawBackground(app)
        drawImage(app.pauseScreen, 250, 250, align = 'center')

        #Draw "Classic" banner. 
        drawImage(app.winnerBanner, 250, 40, align = 'center', width = 450, height = 130)
        drawLabel('Classic', 250, 33, fill = 'white', size = 45, font = 'Gang of Three')

        #Draw "Leaderboard" label. 
        drawLabel('Leaderboard', 250, 100, fill = 'brown', size = 35, bold = True, font = 'Gang of Three')

        #Draw back button.
        app.backButtonLeaderboardClassic.drawBackButton()

        #Authored with the help of ChatGPT.
        #Draw leaderboard.
        with open('scores.csv', 'r') as file:
            reader = csv.reader(file)

            topFive = []
            for row in reader:
                if row:
                    score = (int)(row[0])
                    name = row[1]
                    topFive.append((score, name))
        
        #Store the top five scores. 
        topFive.sort(reverse = True)
        topFive = topFive[:5]

        #Draw the top five scores. 
        for i in range(len(topFive)):
            score, name = topFive[i]
            place = (str)(i + 1) + '.'
            drawLabel(place, 175, 165 + (45 * i), fill = 'brown', size = 25, bold = True, font = 'Gang of Three')
            drawLabel(name, 255, 165 + (45 * i), fill = 'brown', size = 25, bold = True, font = 'Gang of Three')
            drawLabel(score, 335, 165 + (45 * i), fill = 'brown', size = 25, bold = True, font = 'Gang of Three')

        #Draw blade.
        drawBlade(app)

    if app.gameMultiplayer == True:
        if app.pausedMultiplayer == True:
            #Draw background.
            drawBackgroundMultiplayer(app)
            drawImage(app.pauseScreen, 400, 300, align = 'center')

            #Draw "Paused" label. 
            drawLabel('Paused', 400, 150, fill = 'brown', size = 50, bold = True, font = 'Gang of Three')

            #Draw current score. 
            scorePeachPlayer1Paused = Peach(365, 225, 0, 0)
            scorePeachPlayer1Paused.drawPeach()
            drawLabel(app.scorePlayer1, 435, 225, fill = 'red', size = 50, bold = True, font = 'Gang of Three')

            scoreStrawberryPlayer2Paused = Strawberry(365, 300, 0, 0)
            scoreStrawberryPlayer2Paused.drawStrawberry()
            drawLabel(app.scorePlayer2, 435, 300, fill = 'red', size = 50, bold = True, font = 'Gang of Three')
    
            #Draw X that sends user to start screen. 
            drawRect(320, 385, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
            drawRect(320, 385, 42, 10, fill = 'white', rotateAngle = 47, align = 'center')
            drawRect(320, 385, 42, 10, fill = 'white', rotateAngle = -47, align = 'center')

            #Draw "restart" image that restarts classic game. 
            drawRect(400, 385, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
            drawImage(app.restart, 400, 385, align = 'center')

            #Draw play button that resumes game. 
            drawRect(480, 385, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
            drawRegularPolygon(477, 385, 22, 3, fill= 'white', rotateAngle = 90, align = 'center')

            #Draw blade.
            drawBladePlayer1(app)

        else:
            #Draw background.
            drawBackgroundMultiplayer(app)

            #Draw score. 
            scorePeach1 = Peach(45, 35, 0, 0)
            scorePeach1.drawPeach()
            drawLabel(app.scorePlayer1, 100, 35, fill = 'red', size = 50, bold = True, font = 'Gang of Three')

            scoreStrawberry2 = Strawberry(45, 340, 0, 0)
            scoreStrawberry2.drawStrawberry()
            drawLabel(app.scorePlayer2, 100, 340, fill = 'red', size = 50, bold = True, font = 'Gang of Three')

            #Draw bomb bar.
            drawLabel(app.bombDeployCountPlayer1, 715, 160, fill = 'purple', size = 50, bold = True, font = 'Gang of Three') 
            bombBarBombPlayer1 = Bomb(715, 225, 0, 0)
            bombBarBombPlayer1.drawBomb()
            app.bombBarPlayer1.drawBombBar()
            if app.fruitCutPlayer1 == 1:
                drawRect(775, 240, 25, 40, fill = 'red', border = 'lightBlue', borderWidth = 3, align = 'center')
            elif app.fruitCutPlayer1 == 2:
                drawRect(775, 220, 25, 80, fill = 'red', border = 'lightBlue', borderWidth = 3, align = 'center')
            elif app.fruitCutPlayer1 == 3:
                drawRect(775, 200, 25, 120, fill = 'red', border = 'lightBlue', borderWidth = 3, align = 'center')
            drawLabel('Press "space" to deploy', 695, 280, fill = 'yellow', size = 17, bold = True, font = 'Gang of Three') 

            drawLabel(app.bombDeployCountPlayer2, 715, 460, fill = 'purple', size = 50, bold = True, font = 'Gang of Three') 
            bombBarBombPlayer1 = Bomb(715, 525, 0, 0)
            bombBarBombPlayer1.drawBomb() 
            app.bombBarPlayer2.drawBombBar()
            if app.fruitCutPlayer2 == 1:
                drawRect(775, 540, 25, 40, fill = 'red', border = 'lightBlue', borderWidth = 3, align = 'center')
            elif app.fruitCutPlayer2 == 2:
                drawRect(775, 520, 25, 80, fill = 'red', border = 'lightBlue', borderWidth = 3, align = 'center')
            elif app.fruitCutPlayer2 == 3:
                drawRect(775, 500, 25, 120, fill = 'red', border = 'lightBlue', borderWidth = 3, align = 'center')
            drawLabel('Press "/" to deploy', 715, 580, fill = 'yellow', size = 17, bold = True, font = 'Gang of Three')   

            #Draw strikes.
            app.firstStrikePlayer1.drawStrike()
            app.secondStrikePlayer1.drawStrike()
            app.thirdStrikePlayer1.drawStrike()

            app.firstStrikePlayer2.drawStrike()
            app.secondStrikePlayer2.drawStrike()
            app.thirdStrikePlayer2.drawStrike()

            #Shade in strikes based on player 1 strike count. 
            if app.xCountPlayer1 == 0:
                app.firstStrikePlayer1.border = 'lightBlue'
                app.firstStrikePlayer1.fill = 'blue'
                app.secondStrikePlayer1.border = 'lightBlue'
                app.secondStrikePlayer1.fill = 'blue'
                app.thirdStrikePlayer1.border = 'lightBlue'
                app.thirdStrikePlayer1.fill = 'blue'
            elif app.xCountPlayer1 == 1:
                app.firstStrikePlayer1.shade()
            elif app.xCountPlayer1 == 2:
                app.firstStrikePlayer1.shade()
                app.secondStrikePlayer1.shade()
            elif app.xCountPlayer1 == 3:
                app.firstStrikePlayer1.shade()
                app.secondStrikePlayer1.shade()
                app.thirdStrikePlayer1.shade()

            #Shade in strikes based on player 2 strike count. 
            if app.xCountPlayer2 == 0:
                app.firstStrikePlayer2.border = 'lightBlue'
                app.firstStrikePlayer2.fill = 'blue'
                app.secondStrikePlayer2.border = 'lightBlue'
                app.secondStrikePlayer2.fill = 'blue'
                app.thirdStrikePlayer2.border = 'lightBlue'
                app.thirdStrikePlayer2.fill = 'blue'
            elif app.xCountPlayer2 == 1:
                app.firstStrikePlayer2.shade()
            elif app.xCountPlayer2 == 2:
                app.firstStrikePlayer2.shade()
                app.secondStrikePlayer2.shade()
            elif app.xCountPlayer2 == 3:
                app.firstStrikePlayer2.shade()
                app.secondStrikePlayer2.shade()
                app.thirdStrikePlayer2.shade()
            
            #Draw pause button. 
            app.pauseButtonPlayer1.drawPauseButton()

            #Draw player 1's fruits. 
            for i in range(len(app.fruitsPlayer1)):
                fruit = type(app.fruitsPlayer1[i])
                if fruit == Apple:
                    app.fruitsPlayer1[i].drawApple()
                elif fruit == Banana:
                    app.fruitsPlayer1[i].drawBanana()
                elif fruit == Kiwi:
                    app.fruitsPlayer1[i].drawKiwi()
                elif fruit == Peach:
                    app.fruitsPlayer1[i].drawPeach()
                elif fruit == Pear:
                    app.fruitsPlayer1[i].drawPear()
                elif fruit == Pineapple:
                    app.fruitsPlayer1[i].drawPineapple()
                elif fruit == Strawberry:
                    app.fruitsPlayer1[i].drawStrawberry()
                elif fruit == Watermelon:
                    app.fruitsPlayer1[i].drawWatermelon()
            
            #Draw player 2's fruits. 
            for i in range(len(app.fruitsPlayer2)):
                fruit = type(app.fruitsPlayer2[i])
                if fruit == Apple:
                    app.fruitsPlayer2[i].drawApple()
                elif fruit == Banana:
                    app.fruitsPlayer2[i].drawBanana()
                elif fruit == Kiwi:
                    app.fruitsPlayer2[i].drawKiwi()
                elif fruit == Peach:
                    app.fruitsPlayer2[i].drawPeach()
                elif fruit == Pear:
                    app.fruitsPlayer2[i].drawPear()
                elif fruit == Pineapple:
                    app.fruitsPlayer2[i].drawPineapple()
                elif fruit == Strawberry:
                    app.fruitsPlayer2[i].drawStrawberry()
                elif fruit == Watermelon:
                    app.fruitsPlayer2[i].drawWatermelon()
            
            #Draw player 1's bombs. 
            for i in range(len(app.bombsPlayer1)):
                app.bombsPlayer1[i].drawBomb()
            
            #Draw player 2's bombs. 
            for i in range(len(app.bombsPlayer2)):
                app.bombsPlayer2[i].drawBomb()
            
            #Draw player 1's slices. 
            for i in range(len(app.slicedFruitPlayer1)):
                slicedFruit = type(app.slicedFruitPlayer1[i])
                if slicedFruit == AppleSlice:
                    app.slicedFruitPlayer1[i].drawAppleSlice()
                elif slicedFruit == BananaSlice:
                    app.slicedFruitPlayer1[i].drawBananaSlice()
                elif slicedFruit == KiwiSlice:
                    app.slicedFruitPlayer1[i].drawKiwiSlice()
                elif slicedFruit == PeachSlice:
                    app.slicedFruitPlayer1[i].drawPeachSlice()
                elif slicedFruit == PearSlice:
                    app.slicedFruitPlayer1[i].drawPearSlice()
                elif slicedFruit == PineappleSlice:
                    app.slicedFruitPlayer1[i].drawPineappleSlice()
                elif slicedFruit == StrawberrySlice:
                    app.slicedFruitPlayer1[i].drawStrawberrySlice()
                elif slicedFruit == WatermelonSlice:
                    app.slicedFruitPlayer1[i].drawWatermelonSlice()
            
            #Draw player 2's slices. 
            for i in range(len(app.slicedFruitPlayer2)):
                slicedFruit = type(app.slicedFruitPlayer2[i])
                if slicedFruit == AppleSlice:
                    app.slicedFruitPlayer2[i].drawAppleSlice()
                elif slicedFruit == BananaSlice:
                    app.slicedFruitPlayer2[i].drawBananaSlice()
                elif slicedFruit == KiwiSlice:
                    app.slicedFruitPlayer2[i].drawKiwiSlice()
                elif slicedFruit == PeachSlice:
                    app.slicedFruitPlayer2[i].drawPeachSlice()
                elif slicedFruit == PearSlice:
                    app.slicedFruitPlayer2[i].drawPearSlice()
                elif slicedFruit == PineappleSlice:
                    app.slicedFruitPlayer2[i].drawPineappleSlice()
                elif slicedFruit == StrawberrySlice:
                    app.slicedFruitPlayer2[i].drawStrawberrySlice()
                elif slicedFruit == WatermelonSlice:
                    app.slicedFruitPlayer2[i].drawWatermelonSlice()

            #Draw blades.
            drawBladePlayer1(app)
            drawBladePlayer2(app)
                
            #Draw bar.
            drawLine(0, 300, 800, 300, fill= 'white', lineWidth = 13)

            #Draw timer. 
            drawRect(400, 300, 100, 50, fill = 'white', border = 'black', borderWidth = 3, align = 'center')
            drawLabel(app.multiplayerTimer, 400, 300, size = 35, fill = 'black', font = 'Gang of Three')
      
    if app.gameOverClassic:
        #Draw background.
        drawBackground(app)
        drawImage(app.pauseScreen, 250, 250, align = 'center')

        #Draw "Game Over!" label. 
        drawLabel('Game Over!', 250, 100, fill = 'brown', size = 42, bold = True, font = 'Gang of Three')

        #Draw current score. 
        scorePeachGameOver = Peach(215, 175, 0, 0)
        scorePeachGameOver.drawPeach()
        drawLabel(app.score, 285, 175, fill = 'red', size = 50, bold = True, font = 'Gang of Three')

        #Authored with the help of ChatGPT.
        #Draw best score. 
        bestScore = 0
        with open('scores.csv', 'r') as file:
            reader = csv.reader(file)
            
            for row in reader:
                if row:
                    score = (int)(row[0])
                    name = row[1]
                    if name.lower() == app.playerName.lower() and score > bestScore:
                        bestScore = score
                
        drawLabel('Best:', 215, 235, size = 35, fill = 'brown', bold = True, font = 'Gang of Three')
        drawLabel(bestScore, 285, 235, fill = 'brown', size = 35, bold = True, font = 'Gang of Three')

        #Draw X that sends user to start screen. 
        drawRect(170, 325, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
        drawRect(170, 325, 42, 10, fill = 'white', rotateAngle = 47, align = 'center')
        drawRect(170, 325, 42, 10, fill = 'white', rotateAngle = -47, align = 'center')

        #Draw "restart" image that restarts classic game. 
        drawRect(250, 325, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
        drawImage(app.restart, 250, 325, align = 'center')

        #Draw button that opens leaderboard. 
        drawRect(330, 325, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
        drawImage(app.leaderboardGameOver, 330, 325, align = 'center')

        #Draw blade.
        drawBlade(app)

    if app.leaderboardMultiplayer == True:
        #Draw background.
        drawBackgroundMultiplayer(app)
        drawImage(app.pauseScreen, 400, 300, align = 'center')

        #Draw "Multiplayer" banner. 
        drawImage(app.winnerBanner, 400, 60, align = 'center')
        drawLabel('Multiplayer', 400, 50, fill = 'white', size = 55, font = 'Gang of Three')

        #Draw "Leaderboard" label. 
        drawLabel('Leaderboard', 400, 150, fill = 'brown', size = 35, bold = True, font = 'Gang of Three')

        #Draw back button.
        app.backButtonLeaderboardMultiplayer.drawBackButton()

        #Authored with the help of ChatGPT.
        #Draw leaderboard.
        with open('scoresMultiplayer.csv', 'r') as file:
            reader = csv.reader(file)

            topFive = []
            for row in reader:
                if row:
                    score = (int)(row[0])
                    name = row[1]
                    topFive.append((score, name))
        
        topFive.sort(reverse = True)
        topFive = topFive[:5]

        for i in range(len(topFive)):
            score, name = topFive[i]
            place = (str)(i + 1) + '.'
            drawLabel(place, 325, 215 + (45 * i), fill = 'brown', size = 25, bold = True, font = 'Gang of Three')
            drawLabel(name, 405, 215 + (45 * i), fill = 'brown', size = 25, bold = True, font = 'Gang of Three')
            drawLabel(score, 485, 215 + (45 * i), fill = 'brown', size = 25, bold = True, font = 'Gang of Three')

        #Draw blade.
        drawBladePlayer1(app)

    if app.gameOverMultiplayer == True:
        #Draw background.
        drawBackgroundMultiplayer(app)
        drawImage(app.pauseScreen, 400, 300, align = 'center')

        #Anounce winner. 
        drawImage(app.winnerBanner, 400, 60, align = 'center')
        if app.scorePlayer1 > app.scorePlayer2:
            drawLabel('Player 1 Wins!', 400, 50, fill = 'white', size = 55, font = 'Gang of Three')
        elif app.scorePlayer1 < app.scorePlayer2:
            drawLabel('Player 2 Wins!', 400, 50, fill = 'white', size = 55, font = 'Gang of Three')
        elif app.scorePlayer1 == app.scorePlayer2:
            drawLabel('Tie!', 400, 50, fill = 'white', size = 55, font = 'Gang of Three')

        #Draw "Game Over!" label. 
        drawLabel('Game Over!', 400, 150, fill = 'brown', size = 42, bold = True, font = 'Gang of Three')

        #Draw current score. 
        scorePeachPlayer1GameOver = Peach(365, 225, 0, 0)
        scorePeachPlayer1GameOver.drawPeach()
        drawLabel(app.scorePlayer1, 435, 225, fill = 'red', size = 50, bold = True, font = 'Gang of Three')

        scoreStrawberryPlayer2GameOver = Strawberry(365, 300, 0, 0)
        scoreStrawberryPlayer2GameOver.drawStrawberry()
        drawLabel(app.scorePlayer2, 435, 300, fill = 'red', size = 50, bold = True, font = 'Gang of Three')

        #Draw X that sends user to start screen. 
        drawRect(320, 385, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
        drawRect(320, 385, 42, 10, fill = 'white', rotateAngle = 47, align = 'center')
        drawRect(320, 385, 42, 10, fill = 'white', rotateAngle = -47, align = 'center')

        #Draw "restart" image that restarts classic game. 
        drawRect(400, 385, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
        drawImage(app.restart, 400, 385, align = 'center')

        #Draw button that opens leaderboard. 
        drawRect(480, 385, 50, 50, fill = 'brown', border = 'black', borderWidth = 3, align = 'center')
        drawImage(app.leaderboardGameOver, 480, 385, align = 'center')

        #Draw blade.
        drawBladePlayer1(app)

    if app.gameLocker == True:
        #Draw background.
        drawBackground(app)
        drawLabel('Locker', 250, 40, fill = 'crimson', size = 75, bold = True, font = 'Gang of Three')
        drawRect(250, 40, 300, 70, fill = None, border = 'crimson', borderWidth = 3, align = 'center')

        #Draw back button. 
        app.backButtonLocker.drawBackButton()

        #Draw disclaimer.
        drawLabel("Use the arrow keys to cycle through pages", 250, 90, fill = 'yellow', size = 15, bold = True, font = 'Gang of Three')

        #Draw page 0.
        if app.page == 0:
            app.nextPageButton0.drawNextPageButton()

            #Draw "Classic" blade box.
            app.classicBladeBox.drawBladeBox()
            drawCircle(125, 275, 20, fill = 'crimson')
            drawLabel("Classic", 125, 150, fill = 'crimson', size = 25, bold = True, font = 'Gang of Three')
            drawRect(125, 150, 175, 35, fill = None, border = 'crimson', borderWidth = 3, align = 'center')

            #Draw "Magenta Rush" blade box. 
            app.magentaRushBladeBox.drawBladeBox()
            for i in range(10):
                drawCircle(340 + (10 * i), 320 - (10 * i), 20, fill = 'magenta', opacity = 100 - (10 * i))
            drawLabel("Magenta Rush", 375, 150, fill = 'magenta', size = 25, bold = True, font = 'Gang of Three')
            drawRect(375, 150, 185, 35, fill = None, border = 'magenta', borderWidth = 3, align = 'center')
        
        #Draw page 1. 
        elif app.page == 1:
            app.nextPageButton1.drawNextPageButton()
            app.backPageButton1.drawNextPageButton()

            #Draw "RainbowRush" blade box. 
            app.rainbowRampageBladeBox.drawBladeBox()
            colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue']
            for i in range(6):
                drawCircle(110 + (10 * i), 320 - (10 * i), 20 - (2 * i), fill =  colors[i])
            drawLabel("Rainbow Rampage", 125, 150, fill = 'purple', size = 20, bold = True, font = 'Gang of Three')
            drawRect(125, 150, 180, 35, fill = None, border = 'purple', borderWidth = 3, align = 'center')

            #Draw "Shape Fury" blade box. 
            app.shapeFuryBladeBox.drawBladeBox()
            colors2 = ['black', 'gold', 'black', 'gold', 'black']
            shapes = ['triangle', 'square', 'pentagon', 'circle', 'septagon']
            for i in range (5):
                if shapes[i] == 'triangle':
                    drawRegularPolygon(340 + (20 * i), 350 - (30 * i), 25, 3, fill = colors2[i], align = 'center')
                elif shapes[i] == 'square':
                    drawRect(340 + (20 * i), 350 - (30 * i), 35, 35, fill = colors2[i], align = 'center')
                elif shapes[i] == 'pentagon':
                    drawRegularPolygon(340 + (20 * i), 350 - (30 * i), 25, 5, fill = colors2[i], align = 'center')
                elif shapes[i] == 'circle':
                    drawCircle(340 + (20 * i), 350 - (30 * i), 25, fill = colors2[i])
                elif shapes[i] == 'septagon':
                    drawRegularPolygon(340 + (20 * i), 350 - (30 * i), 25, 7, fill = colors2[i], align = 'center')
            drawLabel("Shape Fury", 375, 150, fill = 'black', size = 20, bold = True, font = 'Gang of Three')
            drawRect(375, 150, 180, 35, fill = None, border = 'gold', borderWidth = 3, align = 'center')
        
        #Draw page 2.
        elif app.page == 2:
            app.backPageButton2.drawNextPageButton()

            #Draw "Particle Party" blade box. 
            app.particlePartyBladeBox.drawBladeBox()
            colors = ['midnightBlue', 'indigo', 'darkSlateGray', 'darkViolet', 'mediumSlateBlue']
            opacity = random.randint(50, 75)
            for i in range(5):
                drawCircle(230 + (10 * i), 300 - (10 * i), 20, fill =  colors[i], opacity = opacity)
            drawLabel("Particle Party", 250, 150, fill = 'darkViolet', size = 20, bold = True, font = 'Gang of Three')
            drawRect(250, 150, 180, 35, fill = None, border = 'darkSlateGray', borderWidth = 3, align = 'center')
        
        #Draw blade.
        drawBlade(app)       

def onKeyPress(app, key):
    #Shift through pages in locker. 
    if app.gameLocker == True:
        if app.page == 0:
            if key == 'right':
                app.page += 1
        elif app.page == 1:
            if key == 'right':
                app.page += 1
            elif key == 'left':
                app.page -= 1
        elif app.page == 2:
            if key == 'left':
                app.page -= 1
    
    if app.gameClassic == True:
        if key == 's':
            app.gameClassic = False
            app.gameOverClassic = True

    #Controls the movement of player 2. 
    if app.gameMultiplayer == True:
        if key == 'right':
            app.dxPlayer2 = 1
        elif key == 'left':
            app.dxPlayer2 = -1
        elif key == 'up':
            app.dyPlayer2 = -1
        elif key == 'down':
            app.dyPlayer2 = 1

        #Controls the deployable bombs. 
        elif key == 'space':
            if app.bombDeployCountPlayer1 > 0:
                app.bombDeployCountPlayer1 -= 1
                LaunchMultiplayer.launchNextBombPlayer2(app)
        elif key == '/':
            if app.bombDeployCountPlayer2 > 0:
                app.bombDeployCountPlayer2 -= 1
                LaunchMultiplayer.launchNextBombPlayer1(app)
        
        elif key == 's':
            if app.multiplayerTimer - 10 > 0:
                app.multiplayerTimer -= 10

def onMousePress(app, mouseX, mouseY):
    if app.gameStart:
        #Sends player to rules if pressed. 
        if inButton(mouseX, mouseY, 25, 25, 20):
            app.gameStart = False
            app.howToPlay = True

    if app.howToPlay == True:
        #Sends player to start screen if pressed. 
        if inButton(mouseX, mouseY, 475, 25, 20):
            app.howToPlay = False
            app.gameStart = True
    
    if app.gameLocker == True:
        #Sends player to start screen if pressed. 
        if inButton(mouseX, mouseY, 25, 25, 20):
            app.gameStart = True
            app.gameLocker = False
        
        #Selects blade if box is clicked on page 0. 
        if app.page == 0:
            if inBladeBox(mouseX, mouseY, app.classicBladeBox.cx, app.classicBladeBox.cy, app.classicBladeBox.width, app.classicBladeBox.height):
                app.classicBlade = True
                app.magentaRushBlade = False
                app.rainbowRampageBlade = False
                app.shapeFuryBlade = False
                app.particlePartyBlade = False

            elif inBladeBox(mouseX, mouseY, app.magentaRushBladeBox.cx, app.magentaRushBladeBox.cy, app.magentaRushBladeBox.width, app.magentaRushBladeBox.height):
                app.classicBlade = False
                app.magentaRushBlade = True
                app.rainbowRampageBlade = False
                app.shapeFuryBlade = False
                app.particlePartyBlade = False

        #Selects blade if box is clicked on page 1. 
        if app.page == 1:
            if inBladeBox(mouseX, mouseY, app.rainbowRampageBladeBox.cx, app.rainbowRampageBladeBox.cy, app.rainbowRampageBladeBox.width, app.rainbowRampageBladeBox.height):
                app.classicBlade = False
                app.magentaRushBlade = False
                app.rainbowRampageBlade = True
                app.shapeFuryBlade = False
                app.particlePartyBlade = False
            
            elif inBladeBox(mouseX, mouseY, app.shapeFuryBladeBox.cx, app.shapeFuryBladeBox.cy, app.shapeFuryBladeBox.width, app.shapeFuryBladeBox.height):
                app.classicBlade = False
                app.magentaRushBlade = False
                app.rainbowRampageBlade = False
                app.shapeFuryBlade = True
                app.particlePartyBlade = False
        
        #Selects blade if box is clicked on page 2. 
        if app.page == 2:
            if inBladeBox(mouseX, mouseY, app.particlePartyBladeBox.cx, app.particlePartyBladeBox.cy, app.particlePartyBladeBox.width, app.particlePartyBladeBox.height):
                app.classicBlade = False
                app.magentaRushBlade = False
                app.rainbowRampageBlade = False
                app.shapeFuryBlade = False
                app.particlePartyBlade = True

    if app.gameClassic:
        if app.paused:
            #Sends player to home screen if button is pressed. 
            if inButton(mouseX, mouseY, 170, 325, 50):
                resetGame(app)
                app.paused = False
                app.gameStart = True
                app.gameClassic = False

            #Restarts the game if button is pressed. 
            elif inButton(mouseX, mouseY, 250, 325, 50):
                resetGame(app)
                app.paused = False

            #Resumes the game if button is presed. 
            elif inButton(mouseX, mouseY, 330, 325, 50):
                app.paused = False
                
        else:
            #Pauses the game if pause button is pressed. 
            if inButton(mouseX, mouseY, 30, 470, 35):
                app.paused = True
    
    if app.gameMultiplayer:
        if app.pausedMultiplayer:
            #Sends player to home screen if button is pressed. 
            if inButton(mouseX, mouseY, 320, 385, 50):
                resetGame(app)
                app.width = 500
                app.height = 500
                app.pausedMultiplayer = False
                app.gameStart = True
                app.gameMultiplayer = False

            #Restarts the game if button is pressed. 
            elif inButton(mouseX, mouseY, 400, 385, 50):
                resetGame(app)
                app.pausedMultiplayer = False

            #Resumes the game if button is presed. 
            elif inButton(mouseX, mouseY, 480, 385, 50):
                app.pausedMultiplayer = False

        else:
            #Pauses the game if pause button is pressed. 
            if inButton(mouseX, mouseY, 30, 270, 35):
                app.pausedMultiplayer = True
    
    elif app.gameOverClassic:
        #Sends player to start screen when button is pressed. 
        if inButton(mouseX, mouseY, 170, 325, 50):
            resetGame(app)
            app.gameOverClassic = False
            app.gameStart = True
            app.gameClassic = False

        #Restarts game if button is pressed. 
        elif inButton(mouseX, mouseY, 250, 325, 50):
            resetGame(app)
            app.gameOverClassic = False
            app.gameClassic = True
        
        #Sends player to the leaderboard screen if button is pressed. 
        elif inButton(mouseX, mouseY, 330, 325, 50):
            app.gameOverClassic = False
            app.leaderboardClassic = True 
    
    elif app.leaderboardClassic == True:
        #Sends player back if button is pressed. 
        if inButton(mouseX, mouseY, 25, 25, 20):
            app.gameOverClassic = True
            app.leaderboardClassic = False
    
    elif app.leaderboardMultiplayer == True:
        #Sends player back if button is pressed. 
        if inButton(mouseX, mouseY, 25, 25, 20):
            app.gameOverMultiplayer = True
            app.leaderboardMultiplayer = False

    elif app.gameOverMultiplayer:
        #Sends players to start screen when button is pressed. 
        if inButton(mouseX, mouseY, 320, 385, 50):
            resetGame(app)
            app.width = 500
            app.height = 500
            app.gameOverMultiplayer = False
            app.gameStart = True
            app.gameMultiplayer = False
        
        #Restarts game if button is pressed. 
        elif inButton(mouseX, mouseY, 400, 385, 50):
            resetGame(app)
            app.gameOverMultiplayer = False
            app.gameMultiplayer = True
        
        #Sends players to the leaderboard screen if button is pressed. 
        elif inButton(mouseX, mouseY, 480, 385, 50):
            app.gameOverMultiplayer = False
            app.leaderboardMultiplayer = True

def onMouseMove(app, mouseX, mouseY):
    app.cx = mouseX
    app.cy = mouseY

    #Creates the list of circles for the "Magenta Rush" blade.  
    if app.magentaRushBlade == True:
        app.magentaRush.append((mouseX, mouseY))
        if len(app.magentaRush) > 10:
            app.magentaRush.pop(0)
    
    #Creates the list of circles for the "Rainbow Rampage" blade. 
    if app.rainbowRampageBlade == True:
        colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue']
        randomColor = random.randint(0, 5)
        app.rainbowRampage.append((mouseX, mouseY, colors[randomColor]))
        if len(app.rainbowRampage) > 10:
            app.rainbowRampage.pop(0)
    
    #Creates the list of shapes for the "Shape Fury" blade.
    if app.shapeFuryBlade == True:
        shapes = ['triangle', 'square', 'pentagon', 'circle', 'septagon']
        colors = ['black', 'gold']
        randomShape = random.randint(0, 4)
        color = random.randint(0, 1)
        app.shapeFury.append((mouseX, mouseY, shapes[randomShape], colors[color]))
        if len(app.shapeFury) > 10:
            app.shapeFury.pop(0) 
    
    #Creates the list of points for the "Particle Party" blade. 
    if app.particlePartyBlade == True:
        particleSize = random.randint(5, 15)
        opacity = random.randint(50, 75)
        colors = ['midnightBlue', 'indigo', 'darkSlateGray', 'darkViolet', 'mediumSlateBlue']
        color = random.randint(0, 4)
        app.particleParty.append((mouseX, mouseY, colors[color], particleSize, opacity)) 
        if len(app.particleParty) > 15:
            app.particleParty.pop(0)
    
    if app.gameLocker == True:
        #Highlights back button if hovered over.
        if inButton(mouseX, mouseY, 25, 25, 20):
            app.backButtonLocker.border = 'white'
            app.backButtonLocker.opacity = 100
        else:
            app.backButtonLocker.border = 'grey'
            app.backButtonLocker.opacity = 50

        #Highlights blade boxes if hovered over on page 0. 
        if app.page == 0:
            if inBladeBox(mouseX, mouseY, app.classicBladeBox.cx, app.classicBladeBox.cy, app.classicBladeBox.width, app.classicBladeBox.height):
                app.classicBladeBox.fill = 'white'
            else:
                app.classicBladeBox.fill = 'grey'
            
            if inBladeBox(mouseX, mouseY, app.magentaRushBladeBox.cx, app.magentaRushBladeBox.cy, app.magentaRushBladeBox.width, app.magentaRushBladeBox.height):
                app.magentaRushBladeBox.fill = 'white'
            else:
                app.magentaRushBladeBox.fill = 'grey'

        #Highlights blade boxes if hovered over on page 1. 
        if app.page == 1:
            if inBladeBox(mouseX, mouseY, app.rainbowRampageBladeBox.cx, app.rainbowRampageBladeBox.cy, app.rainbowRampageBladeBox.width, app.rainbowRampageBladeBox.height):
                app.rainbowRampageBladeBox.fill = 'white'
            else:
                app.rainbowRampageBladeBox.fill = 'grey'

            if inBladeBox(mouseX, mouseY, app.shapeFuryBladeBox.cx, app.shapeFuryBladeBox.cy, app.shapeFuryBladeBox.width, app.shapeFuryBladeBox.height):
                app.shapeFuryBladeBox.fill = 'white'
            else:
                app.shapeFuryBladeBox.fill = 'grey'
        
        #Highlights blade boxes if hovered over on page 2. 
        if app.page == 2:
            if inBladeBox(mouseX, mouseY, app.particlePartyBladeBox.cx, app.particlePartyBladeBox.cy, app.particlePartyBladeBox.width, app.particlePartyBladeBox.height):
                app.particlePartyBladeBox.fill = 'white'
            else:
                app.particlePartyBladeBox.fill = 'grey'

    
    if app.howToPlay == True:
        #Highlights the back button if hovered over. 
        if inButton(mouseX, mouseY, 475, 25, 20):
            app.backButtonHowToPlay.border = 'white'
            app.backButtonHowToPlay.opacity = 100
        else: 
            app.backButtonHowToPlay.border = 'grey'
            app.backButtonHowToPlay.opacity = 50
    
    if app.leaderboardClassic == True:
        #Highlights the back button if hovered over. 
        if inButton(mouseX, mouseY, 25, 25, 20):
            app.backButtonLeaderboardClassic.border = 'white'
            app.backButtonLeaderboardClassic.opacity = 100
        else: 
            app.backButtonLeaderboardClassic.border = 'grey'
            app.backButtonLeaderboardClassic.opacity = 50
    
    if app.leaderboardMultiplayer == True:
        #Highlights the back button if hovered over. 
        if inButton(mouseX, mouseY, 25, 25, 20):
            app.backButtonLeaderboardMultiplayer.border = 'white'
            app.backButtonLeaderboardMultiplayer.opacity = 100
        else: 
            app.backButtonLeaderboardMultiplayer.border = 'grey'
            app.backButtonLeaderboardMultiplayer.opacity = 50
 
    if app.gameStart == True:
        #Highlights the "How To Play" button if hovered over. 
        if inButton(mouseX, mouseY, 25, 25, 20):
            app.howToPlayButton.border = 'white'
            app.howToPlayButton.fill = 'white'
        else: 
            app.howToPlayButton.border = 'grey'
            app.howToPlayButton.fill = 'grey'

        #Choose game mode.
        if inFruit(app.cx, app.cy, 100, 350):
            app.gameStart = False
            app.gameClassic = True
            app.gameMultiplayer = False
            app.gameLocker = False
        elif inFruit(app.cx, app.cy, 250, 350):
            app.playerName2 = app.getTextInput("Enter opponent's name:")
            app.gameStart = False
            app.gameClassic = False
            app.gameMultiplayer = True
            app.gameLocker = False
            app.width = 800
            app.height = 600
        elif inFruit(app.cx, app.cy, 400, 350):
            app.gameStart = False
            app.gameClassic = False
            app.gameMultiplayer = False
            app.gameLocker = True
    
    if app.gameClassic == True:
        #Highlights pause button if hovered over. 
        if inButton(mouseX, mouseY, 30, 470, 35):
            app.pauseButtonClassic.border = 'white'
        else:
            app.pauseButtonClassic.border = 'grey'

        #Slices fruit if blade slices within fruit. 
        i = 0
        while i < len(app.fruits):
            if inFruit(app.cx, app.cy, app.fruits[i].x, app.fruits[i].y):
                fruit = type(app.fruits[i])
                x = app.fruits[i].x
                y = app.fruits[i].y
                app.score += 1
                app.fruits.pop(i)
                Launch.spawnSlice(app, fruit, x, y)
            else:
                i += 1

        #Ends game if blade slices within a bomb.
        for j in range(len(app.bombs)):
            if inFruit(app.cx, app.cy, app.bombs[j].x, app.bombs[j].y):
                app.gameOverClassic = True
                app.gameClassic = False

            updated = False
            with open('scores.csv', 'r') as file:
                reader = csv.reader(file)

                allRows = [row for row in reader if row]

            for row in allRows:
                score = (int)(row[0])
                name = row[1]
                if name.lower() == app.playerName.lower():
                    if app.score >= score:
                        row[0] = (str)(app.score)
                    updated = True
                    break
                
            if updated == False:
                allRows.append([(str)(app.score), app.playerName.lower()])
            
            with open('scores.csv', 'w', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerows(allRows)  
    
    if app.gameMultiplayer == True:
        #Bounds player 1's mouse movement. 
        x = mouseX 
        y = mouseY
        if not app.pausedMultiplayer: 
            if x + 8 > app.width:
                x = app.width - 8
            elif x - 8 < 0:
                x = 8
            if y + 8 > 295:
                y = 295 - 8
            elif y - 8 < 0:
                y = 8

        #Creates the list of circles for player 1's blade.
        app.bladePlayer1.append((x, y))
        if len(app.bladePlayer1) > 10:
            app.bladePlayer1.pop(0)

        #Highlights player 1's pause button if hovered over.
        if inButton(mouseX, mouseY, 30, 270, 35):
            app.pauseButtonPlayer1.border = 'white'
        else:
            app.pauseButtonPlayer1.border = 'darkGrey'
        
        #Slices fruit if player 1's blade slices within fruit. 
        i = 0
        while i < len(app.fruitsPlayer1):
            if inFruit(app.cx, app.cy, app.fruitsPlayer1[i].x, app.fruitsPlayer1[i].y):
                fruit = type(app.fruitsPlayer1[i])
                x = app.fruitsPlayer1[i].x
                y = app.fruitsPlayer1[i].y
                app.scorePlayer1 += 1
                if app.fruitCutPlayer1 == 3:
                    app.bombDeployCountPlayer1 += 1
                app.fruitsPlayer1.pop(i)
                LaunchMultiplayer.spawnSlicePlayer1(app, fruit, x, y)
                if app.fruitCutPlayer1 < 4:
                    app.fruitCutPlayer1 += 1
                elif app.fruitCutPlayer1 == 4:
                    app.fruitCutPlayer1 = 0
            else:
                i += 1
        
        #Reduces player 1's score if blade slices within a bomb.
        j = 0
        while j < len(app.bombsPlayer1):
            if inFruit(app.cx, app.cy, app.bombsPlayer1[j].x, app.bombsPlayer1[j].y):
                if app.scorePlayer1 >= 5:
                    app.scorePlayer1 -= 5
                elif app.scorePlayer1 < 5:
                    app.scorePlayer1 = 0
                app.bombsPlayer1.pop(j)
            else:
                j += 1
    
    if app.gameOverMultiplayer == True:
        x = mouseX 
        y = mouseY

        #Creates the list of circles for player 1's blade.
        app.bladePlayer1.append((x, y))
        if len(app.bladePlayer1) > 10:
            app.bladePlayer1.pop(0)
    
    if app.leaderboardMultiplayer == True:
        x = mouseX 
        y = mouseY

        #Creates the list of circles for player 1's blade.
        app.bladePlayer1.append((x, y))
        if len(app.bladePlayer1) > 10:
            app.bladePlayer1.pop(0)

def takeStep(app):
    if app.gameClassic == True:
        #Game physics for fruit. 
        for i in range(len(app.fruits)):
            app.fruits[i].y, app.fruits[i].yv = Gravity.falling(app.fruits[i].y, app.fruits[i].yv, 500, 0.01)
            app.fruits[i].x = Gravity.lateralMovement(app.fruits[i].x, app.fruits[i].xv, 0.01)
            app.fruits[i].rotateAngle()
        
        #Game physics for bombs. 
        for j in range(len(app.bombs)):
            app.bombs[j].y, app.bombs[j].yv = Gravity.falling(app.bombs[j].y, app.bombs[j].yv, 500, 0.01)
            app.bombs[j].x = Gravity.lateralMovement(app.bombs[j].x, app.bombs[j].xv, 0.01)
            app.bombs[j].rotateAngle()
        
        #Game physics for slices. 
        for k in range(len(app.slicedFruit)):
            app.slicedFruit[k].y, app.slicedFruit[k].yv = Gravity.falling(app.slicedFruit[k].y, app.slicedFruit[k].yv, 500, 0.01)
            app.slicedFruit[k].x = Gravity.lateralMovement(app.slicedFruit[k].x, app.slicedFruit[k].xv, 0.01)
            app.slicedFruit[k].rotateAngle()
        
        #Removes fruit that fall below screen. Adds a strike. 
        length = len(app.fruits)
        app.fruits = [fruit for fruit in app.fruits if fruit.y < 520]
        if length != len(app.fruits):
            app.xCount += length - len(app.fruits)
        
        #Removes bombs that fall below screen. 
        app.bombs = [bomb for bomb in app.bombs if bomb.y < 520]

        #Removes slices that fall below screen.
        app.slicedFruit = [sliced for sliced in app.slicedFruit if sliced.y < 520]
        
        if app.delayClassic >= 1:
            #Launches fruit based on variable frequency. 
            if app.counterClassic % app.fruitFrequency == 0:
                Launch.launchNextFruit(app)
            
            #Launches bomb based on variable frequency.
            if app.counterClassic % app.bombFrequency == 0:
                Launch.launchNextBomb(app)

        #Varies the frequency of launches based on score. 
        if app.score % 10 == 0 and app.score != 0:
            if app.fruitFrequency >= 50 and app.bombFrequency >= 60:
                app.fruitFrequency = app.fruitFrequency - (1 * (app.score / 5))
                app.bombFrequency = app.bombFrequency - (2 * (app.score / 5))
                   
        #Ends the game if the player gets three strikes. 
        if app.xCount == 3:
            app.gameClassic = False
            app.gameOverClassic = True

            #Authored with the help of ChatGPT
            #Stores the highest score for each player. 
            updated = False
            with open('scores.csv', 'r') as file:
                reader = csv.reader(file)

                allRows = [row for row in reader if row]

            for row in allRows:
                score = (int)(row[0])
                name = row[1]
                if name.lower() == app.playerName.lower():
                    if app.score >= score:
                        row[0] = (str)(app.score)
                    updated = True
                    break
                
            if updated == False:
                allRows.append([(str)(app.score), app.playerName.lower()])
            
            with open('scores.csv', 'w', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerows(allRows)  
        
        app.counterClassic += 1
        app.delayClassic += 1

def takeStepMultiplayer(app):
    if app.gameMultiplayer == True:
        #Moves player 2's blade. 
        app.cxPlayer2 += (2.5 * app.dxPlayer2)
        app.cyPlayer2 += (2.5 * app.dyPlayer2)

        #Bounds player 2's mouse movement. 
        x = app.cxPlayer2 
        y = app.cyPlayer2
        if x + 8 > app.width:
            x = app.width - 8
        elif x - 8 < 0:
            x = 8
        if y + 8 > app.height:
            y = app.height - 8
        elif y - 8 < 310:
            y = 310

        #Creates the list of circles for player 2's blade.
        app.bladePlayer2.append((x, y))
        if len(app.bladePlayer2) > 10:
            app.bladePlayer2.pop(0)
        
        #Slices fruit if player 2's blade slices within fruit. 
        k = 0
        while k < len(app.fruitsPlayer2):
            if inFruit(app.cxPlayer2, app.cyPlayer2, app.fruitsPlayer2[k].x, app.fruitsPlayer2[k].y):
                fruit = type(app.fruitsPlayer2[k])
                x = app.fruitsPlayer2[k].x
                y = app.fruitsPlayer2[k].y
                app.scorePlayer2 += 1
                if app.fruitCutPlayer2 == 3:
                    app.bombDeployCountPlayer2 += 1
                app.fruitsPlayer2.pop(k)
                LaunchMultiplayer.spawnSlicePlayer2(app, fruit, x, y)
                if app.fruitCutPlayer2 < 4:
                    app.fruitCutPlayer2 += 1
                elif app.fruitCutPlayer2 == 4:
                    app.fruitCutPlayer2 = 0
            else:
                k += 1
        
        #Reduces player 2's score if blade slices within a bomb.
        j = 0
        while j < len(app.bombsPlayer2):
            if inFruit(app.cxPlayer2, app.cyPlayer2, app.bombsPlayer2[j].x, app.bombsPlayer2[j].y):
                if app.scorePlayer2 >= 5:
                    app.scorePlayer2 -= 5
                elif app.scorePlayer2 < 5:
                    app.scorePlayer2 = 0
                app.bombsPlayer2.pop(j)
            else:
                j += 1

        #Game physics for player 1's fruit. 
        for i in range(len(app.fruitsPlayer1)):
            app.fruitsPlayer1[i].y, app.fruitsPlayer1[i].yv = Gravity.falling(app.fruitsPlayer1[i].y, app.fruitsPlayer1[i].yv, 500, 0.01)
            app.fruitsPlayer1[i].x = Gravity.lateralMovement(app.fruitsPlayer1[i].x, app.fruitsPlayer1[i].xv, 0.01)
            app.fruitsPlayer1[i].rotateAngle()

        #Game physics for player 2's fruit. 
        for i in range(len(app.fruitsPlayer2)):
            app.fruitsPlayer2[i].y, app.fruitsPlayer2[i].yv = Gravity.falling(app.fruitsPlayer2[i].y, app.fruitsPlayer2[i].yv, 500, 0.005)
            app.fruitsPlayer2[i].x = Gravity.lateralMovement(app.fruitsPlayer2[i].x, app.fruitsPlayer2[i].xv, 0.005)
            app.fruitsPlayer2[i].rotateAngle()
        
        #Game physics for player 1's bombs. 
        for j in range(len(app.bombsPlayer1)):
            app.bombsPlayer1[j].y, app.bombsPlayer1[j].yv = Gravity.falling(app.bombsPlayer1[j].y, app.bombsPlayer1[j].yv, 500, 0.01)
            app.bombsPlayer1[j].x = Gravity.lateralMovement(app.bombsPlayer1[j].x, app.bombsPlayer1[j].xv, 0.01)
            app.bombsPlayer1[j].rotateAngle()
        
        #Game physics for player 2's bombs. 
        for j in range(len(app.bombsPlayer2)):
            app.bombsPlayer2[j].y, app.bombsPlayer2[j].yv = Gravity.falling(app.bombsPlayer2[j].y, app.bombsPlayer2[j].yv, 500, 0.005)
            app.bombsPlayer2[j].x = Gravity.lateralMovement(app.bombsPlayer2[j].x, app.bombsPlayer2[j].xv, 0.005)
            app.bombsPlayer2[j].rotateAngle()
        
        #Game physics for player 1's slices. 
        for k in range(len(app.slicedFruitPlayer1)):
            app.slicedFruitPlayer1[k].y, app.slicedFruitPlayer1[k].yv = Gravity.falling(app.slicedFruitPlayer1[k].y, app.slicedFruitPlayer1[k].yv, 500, 0.01)
            app.slicedFruitPlayer1[k].x = Gravity.lateralMovement(app.slicedFruitPlayer1[k].x, app.slicedFruitPlayer1[k].xv, 0.01)
            app.slicedFruitPlayer1[k].rotateAngle()
        
        #Game physics for player 2's slices. 
        for k in range(len(app.slicedFruitPlayer2)):
            app.slicedFruitPlayer2[k].y, app.slicedFruitPlayer2[k].yv = Gravity.falling(app.slicedFruitPlayer2[k].y, app.slicedFruitPlayer2[k].yv, 500, 0.01)
            app.slicedFruitPlayer2[k].x = Gravity.lateralMovement(app.slicedFruitPlayer2[k].x, app.slicedFruitPlayer2[k].xv, 0.01)
            app.slicedFruitPlayer2[k].rotateAngle()
        
        #Removes fruit that fall below player 1's screen. Adds a strike. 
        length1 = len(app.fruitsPlayer1)
        app.fruitsPlayer1 = [fruit for fruit in app.fruitsPlayer1 if fruit.y < 270]
        if length1 != len(app.fruitsPlayer1):
            app.xCountPlayer1 += length1 - len(app.fruitsPlayer1)

        #Removes fruit that fall below player 2's screen. Adds a strike. 
        length2 = len(app.fruitsPlayer2)
        app.fruitsPlayer2 = [fruit for fruit in app.fruitsPlayer2 if fruit.y < 620]
        if length2 != len(app.fruitsPlayer2):
            app.xCountPlayer2 += length2 - len(app.fruitsPlayer2)
        
        #Removes bombs that fall below player 1's screen. 
        app.bombsPlayer1 = [bomb for bomb in app.bombsPlayer1 if bomb.y < 270]

        #Removes bombs that fall below player 2's screen. 
        app.bombsPlayer2 = [bomb for bomb in app.bombsPlayer2 if bomb.y < 620]

        #Removes slices that fall below player 1's screen.
        app.slicedFruitPlayer1 = [sliced for sliced in app.slicedFruitPlayer1 if sliced.y < 270]

        #Removes slices that fall below player 2's screen.
        app.slicedFruitPlayer2 = [sliced for sliced in app.slicedFruitPlayer2 if sliced.y < 620]
        
        if app.delayMultiplayer >= 1:
            #Launches player 1's fruit based on variable frequency. 
            if app.counterMultiplayer % app.fruitFrequencyPlayer1 == 0:
                LaunchMultiplayer.launchNextFruitPlayer1(app)
            
            #Launches player 1's bomb based on variable frequency.
            if app.counterMultiplayer % app.bombFrequencyPlayer1 == 0:
                LaunchMultiplayer.launchNextBombPlayer1(app)

            #Launches player 2's fruit based on variable frequency. 
            if app.counterMultiplayer % app.fruitFrequencyPlayer2 == 0:
                LaunchMultiplayer.launchNextFruitPlayer2(app)
            
            #Launches player 2's bomb based on variable frequency.
            if app.counterMultiplayer % app.bombFrequencyPlayer2 == 0:
                LaunchMultiplayer.launchNextBombPlayer2(app)
        
        if app.delayMultiplayer >= 200:
            #Changes multiplayer timer. 
            if app.counterMultiplayer % 50 == 0:
                if app.multiplayerTimer > 0:
                    app.multiplayerTimer -= 1
            
            #Ends game if timer strikes 0.
            if app.multiplayerTimer == 0:
                app.gameOverMultiplayer = True
                app.gameMultiplayer = False

                #Authored with the help of ChatGPT
                #Stores the highest score for each player. 
                updatedPlayer1 = False
                updatedPlayer2 = False
                with open('scoresMultiplayer.csv', 'r') as file:
                    reader = csv.reader(file)

                    allRows = [row for row in reader if row]

                for row in allRows:
                    score = (int)(row[0])
                    name = row[1]
                    if name.lower() == app.playerName.lower():
                        if app.scorePlayer1 > score:
                            row[0] = (str)(app.scorePlayer1)
                        updatedPlayer1 = True
                    elif name.lower() == app.playerName2.lower():
                        if app.scorePlayer2 > score:
                            row[0] = (str)(app.scorePlayer2)
                        updatedPlayer2 = True
                    
                if updatedPlayer1 == False:
                    allRows.append([(str)(app.scorePlayer1), app.playerName.lower()])
                
                if updatedPlayer2 == False:
                    allRows.append([(str)(app.scorePlayer2), app.playerName2.lower()])
                
                with open('scoresMultiplayer.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerows(allRows)

        #Varies the frequency of launches based on player 1's score. 
        if app.scorePlayer1 % 20 == 0 and app.scorePlayer1 != 0:
            if app.fruitFrequencyPlayer1 >= 50 and app.bombFrequencyPlayer1 >= 60:
                app.fruitFrequencyPlayer1 = app.fruitFrequencyPlayer1 - (1 * (app.scorePlayer1 / 5))
                app.bombFrequencyPlayer1 = app.bombFrequencyPlayer1 - (2 * (app.scorePlayer1 / 5))
                    
        #Resets player's score if they get three strikes. 
        if app.xCountPlayer1 == 3:
            app.xCountPlayer1 = 0
            app.scorePlayer1 = 0
        elif app.xCountPlayer2 == 3:
            app.xCountPlayer2 = 0
            app.scorePlayer2 = 0
        
        app.counterMultiplayer += 1
        app.delayMultiplayer += 1

def onStep(app):
    if app.gameStart == True:
        app.counterStart += 0.5

        #Spin fruit on start screen. 
        app.startStrawberry.rotateAngle()
        app.startPineapple.rotateAngle()
        app.startWatermelon.rotateAngle()

    if app.gameClassic == True:
        if not app.paused:
            takeStep(app)
    
    if app.gameMultiplayer == True:
        if not app.pausedMultiplayer:
            takeStepMultiplayer(app)
        
def main():
    runApp()

main()