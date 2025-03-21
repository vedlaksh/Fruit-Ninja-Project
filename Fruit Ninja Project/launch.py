import random
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

class Launch:
    #Launches fruit. 
    @staticmethod
    def launchNextFruit(app):
        #Assigns random spawnpoint and selects the fruit to be launched. 
        randomX = random.randint(0, 500)
        randomFruit = random.randint(0, 7)

        #Sets the initial x and y velocities. 
        if randomX < 250:
            initialXV = random.randint(100, 200)
            initialYV = random.randint(600, 750)
        elif randomX >= 250:
            initialXV = random.randint(-200, -100)
            initialYV = random.randint(600, 750)

        if randomFruit == 0:
            app.fruits.append(Apple(randomX, 500, initialXV, initialYV))
        elif randomFruit == 1:
            app.fruits.append(Banana(randomX, 500, initialXV, initialYV))
        elif randomFruit == 2:
            app.fruits.append(Kiwi(randomX, 500, initialXV, initialYV))
        elif randomFruit == 3:
            app.fruits.append(Peach(randomX, 500, initialXV, initialYV))
        elif randomFruit == 4:
            app.fruits.append(Pear(randomX, 500, initialXV, initialYV))
        elif randomFruit == 5:
            app.fruits.append(Pineapple(randomX, 500, initialXV, initialYV))
        elif randomFruit == 6:
            app.fruits.append(Strawberry(randomX, 500, initialXV, initialYV))
        elif randomFruit == 7:
            app.fruits.append(Watermelon(randomX, 500, initialXV, initialYV))

    #Launches bombs. 
    @staticmethod
    def launchNextBomb(app):
        #Assigns random spawnpoint.
        randomX = random.randint(0, 500)

        #Sets the initial x and y velocties. 
        if randomX < 250:
            initialXV = random.randint(100, 200)
            initialYV = random.randint(600, 750)
        elif randomX >= 250:
            initialXV = random.randint(-200, -100)
            initialYV = random.randint(600, 750)

        app.bombs.append(Bomb(randomX, 500, initialXV, initialYV))
    
    #Spawns slices of the fruit when cut.
    @staticmethod
    def spawnSlice(app, fruit, x, y):
        if fruit == Apple:
            app.slicedFruit.append(AppleSlice(x, y, 100, 150))
            app.slicedFruit.append(AppleSlice(x, y, -100, 150))
        elif fruit == Banana:
            app.slicedFruit.append(BananaSlice(x, y, 100, 150))
        elif fruit == Kiwi:
            app.slicedFruit.append(KiwiSlice(x, y, 100, 150))
            app.slicedFruit.append(KiwiSlice(x, y, -100, 150))
        elif fruit == Peach:
            app.slicedFruit.append(PeachSlice(x, y, 100, 150))
            app.slicedFruit.append(PeachSlice(x, y, -100, 150))
        elif fruit == Pear:
            app.slicedFruit.append(PearSlice(x, y, 100, 150))
            app.slicedFruit.append(PearSlice(x, y, -100, 150))
        elif fruit == Pineapple:
            app.slicedFruit.append(PineappleSlice(x, y, 100, 150))
            app.slicedFruit.append(PineappleSlice(x, y, -100, 150))
        elif fruit == Strawberry:
            app.slicedFruit.append(StrawberrySlice(x, y, 100, 150))
            app.slicedFruit.append(StrawberrySlice(x, y, -100, 150))
        elif fruit == Watermelon:
            app.slicedFruit.append(WatermelonSlice(x, y, 100, 150))
            app.slicedFruit.append(WatermelonSlice(x, y, -100, 150))

class LaunchMultiplayer:
    #Launches fruit for player 1. 
    @staticmethod
    def launchNextFruitPlayer1(app):
        #Assigns random spawnpoint and selects the fruit to be launched. 
        randomX = random.randint(0, 800)
        randomFruit = random.randint(0, 7)

        #Sets the initial x and y velocities. 
        if randomX < 400:
            initialXV = random.randint(200, 300)
        elif randomX >= 400:
            initialXV = random.randint(-300, -200)

        if randomFruit == 0:
            app.fruitsPlayer1.append(Apple(randomX, 0, initialXV, 0))
        elif randomFruit == 1:
            app.fruitsPlayer1.append(Banana(randomX, 0, initialXV, 0))
        elif randomFruit == 2:
            app.fruitsPlayer1.append(Kiwi(randomX, 0, initialXV, 0))
        elif randomFruit == 3:
            app.fruitsPlayer1.append(Peach(randomX, 0, initialXV, 0))
        elif randomFruit == 4:
            app.fruitsPlayer1.append(Pear(randomX, 0, initialXV, 0))
        elif randomFruit == 5:
            app.fruitsPlayer1.append(Pineapple(randomX, 0, initialXV, 0))
        elif randomFruit == 6:
            app.fruitsPlayer1.append(Strawberry(randomX, 0, initialXV, 0))
        elif randomFruit == 7:
            app.fruitsPlayer1.append(Watermelon(randomX, 0, initialXV, 0))

    #Launches fruit for player 2. 
    @staticmethod
    def launchNextFruitPlayer2(app):
        #Assigns random spawnpoint and selects the fruit to be launched. 
        randomX = random.randint(0, 800)
        randomFruit = random.randint(0, 7)

        #Sets the initial x and y velocities. 
        if randomX < 400:
            initialXV = random.randint(200, 300)
            initialYV = random.randint(500, 575)
        elif randomX >= 400:
            initialXV = random.randint(-300, -200)
            initialYV = random.randint(500, 575)

        if randomFruit == 0:
            app.fruitsPlayer2.append(Apple(randomX, 610, initialXV, initialYV))
        elif randomFruit == 1:
            app.fruitsPlayer2.append(Banana(randomX, 610, initialXV, initialYV))
        elif randomFruit == 2:
            app.fruitsPlayer2.append(Kiwi(randomX, 610, initialXV, initialYV))
        elif randomFruit == 3:
            app.fruitsPlayer2.append(Peach(randomX, 610, initialXV, initialYV))
        elif randomFruit == 4:
            app.fruitsPlayer2.append(Pear(randomX, 610, initialXV, initialYV))
        elif randomFruit == 5:
            app.fruitsPlayer2.append(Pineapple(randomX, 610, initialXV, initialYV))
        elif randomFruit == 6:
            app.fruitsPlayer2.append(Strawberry(randomX, 610, initialXV, initialYV))
        elif randomFruit == 7:
            app.fruitsPlayer2.append(Watermelon(randomX, 610, initialXV, initialYV))

    #Launches player 1's bombs. 
    @staticmethod
    def launchNextBombPlayer1(app):
        #Assigns random spawnpoint.
        randomX = random.randint(0, 800)

        #Sets the initial x and y velocties. 
        if randomX < 400:
            initialXV = random.randint(200, 300)
        elif randomX >= 400:
            initialXV = random.randint(-300, -200)

        app.bombsPlayer1.append(Bomb(randomX, 0, initialXV, 0))

    #Launches player 2's bombs. 
    @staticmethod
    def launchNextBombPlayer2(app):
        #Assigns random spawnpoint.
        randomX = random.randint(0, 800)

        #Sets the initial x and y velocities.
        if randomX < 400:
            initialXV = random.randint(200, 300)
            initialYV = random.randint(500, 575)
        elif randomX >= 400:
            initialXV = random.randint(-300, -200)
            initialYV = random.randint(500, 575)

        app.bombsPlayer2.append(Bomb(randomX, 610, initialXV, initialYV))

    #Spawns slices of player 1's fruit when cut.
    @staticmethod
    def spawnSlicePlayer1(app, fruit, x, y):
        if fruit == Apple:
            app.slicedFruitPlayer1.append(AppleSlice(x, y, 100, 150))
            app.slicedFruitPlayer1.append(AppleSlice(x, y, -100, 150))
        elif fruit == Banana:
            app.slicedFruitPlayer1.append(BananaSlice(x, y, 100, 150))
        elif fruit == Kiwi:
            app.slicedFruitPlayer1.append(KiwiSlice(x, y, 100, 150))
            app.slicedFruitPlayer1.append(KiwiSlice(x, y, -100, 150))
        elif fruit == Peach:
            app.slicedFruitPlayer1.append(PeachSlice(x, y, 100, 150))
            app.slicedFruitPlayer1.append(PeachSlice(x, y, -100, 150))
        elif fruit == Pear:
            app.slicedFruitPlayer1.append(PearSlice(x, y, 100, 150))
            app.slicedFruitPlayer1.append(PearSlice(x, y, -100, 150))
        elif fruit == Pineapple:
            app.slicedFruitPlayer1.append(PineappleSlice(x, y, 100, 150))
            app.slicedFruitPlayer1.append(PineappleSlice(x, y, -100, 150))
        elif fruit == Strawberry:
            app.slicedFruitPlayer1.append(StrawberrySlice(x, y, 100, 150))
            app.slicedFruitPlayer1.append(StrawberrySlice(x, y, -100, 150))
        elif fruit == Watermelon:
            app.slicedFruitPlayer1.append(WatermelonSlice(x, y, 100, 150))
            app.slicedFruitPlayer1.append(WatermelonSlice(x, y, -100, 150)) 

    #Spawns slices of player 2's fruit when cut.
    @staticmethod
    def spawnSlicePlayer2(app, fruit, x, y):
        if fruit == Apple:
            app.slicedFruitPlayer2.append(AppleSlice(x, y, 100, 150))
            app.slicedFruitPlayer2.append(AppleSlice(x, y, -100, 150))
        elif fruit == Banana:
            app.slicedFruitPlayer2.append(BananaSlice(x, y, 100, 150))
        elif fruit == Kiwi:
            app.slicedFruitPlayer2.append(KiwiSlice(x, y, 100, 150))
            app.slicedFruitPlayer2.append(KiwiSlice(x, y, -100, 150))
        elif fruit == Peach:
            app.slicedFruitPlayer2.append(PeachSlice(x, y, 100, 150))
            app.slicedFruitPlayer2.append(PeachSlice(x, y, -100, 150))
        elif fruit == Pear:
            app.slicedFruitPlayer2.append(PearSlice(x, y, 100, 150))
            app.slicedFruitPlayer2.append(PearSlice(x, y, -100, 150))
        elif fruit == Pineapple:
            app.slicedFruitPlayer2.append(PineappleSlice(x, y, 100, 150))
            app.slicedFruitPlayer2.append(PineappleSlice(x, y, -100, 150))
        elif fruit == Strawberry:
            app.slicedFruitPlayer2.append(StrawberrySlice(x, y, 100, 150))
            app.slicedFruitPlayer2.append(StrawberrySlice(x, y, -100, 150))
        elif fruit == Watermelon:
            app.slicedFruitPlayer2.append(WatermelonSlice(x, y, 100, 150))
            app.slicedFruitPlayer2.append(WatermelonSlice(x, y, -100, 150))
        