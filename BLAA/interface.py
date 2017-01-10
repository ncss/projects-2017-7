from microbit import *
import random

grid = []

def setPixel(x, y, brightness):
    grid[x][y] = brightness


def updateDisplay():
    for x in range(0, 5):
        for y in range(0, 5):
            display.set_pixel(x, y, grid[x][y])


class Bird:
    resetGame = False
    dead = False
    gravity = 30.0
    jumpVelocity = 20.0
    
    def reset(self):
        self.birdPos = 0.0
        self.birdVelocity = 0.0
        self.dead = False
        self.deathPipe = None
        self.deathTimer = 0
        self.resetGame = False
    
    def setVelocity(self, velocity):
        self.birdVelocity = velocity

    def jump(self):
        self.setVelocity(self.jumpVelocity)

    def update(self, delta):
        self.birdVelocity -= self.gravity * delta
        self.birdPos += self.birdVelocity * delta
        if self.birdPos <= 0.0:
            self.birdPos = 0.0
            self.birdVelocity = 0.0
        if self.birdPos >= 4.99:
            self.birdPos = 4.99
            self.birdVelocity = 0.0
 
    def getPixelPos(self):
        return (0, int(4 - self.birdPos))
        
    def display(self):
      pos = self.getPixelPos()
      if pos[1] < 5 and pos[1] >= 0:
        setPixel(pos[0], pos[1], 9)
    
    def hitPipe(self, deathPipe):
      print("impact")
    
    def checkDeath(self, terrainMap):
        pos = self.getPixelPos()
        for pipe in terrainMap.pipes:
            for pixel in pipe.getPixels():
                if pixel[0] == pos[0] and pixel[1] == pos[1]:
                    self.hitPipe(pipe)
                

class Pipe:
    def __init__(self):
        self.pipeHeight = random.randint(1,3)
        self.pipeType = random.randint(0,1)
        self.pipePos = 5
  
    def getPixels(self):
        pixels = []
        pipeRange = range(1)
        if self.pipeType == 0: pipeRange = range(4, 4 - self.pipeHeight, -1)
        else: pipeRange = range(self.pipeHeight)
        for i in pipeRange:
            pixels.append((self.pipePos, i))
        return pixels

    def move(self):
      self.pipePos -= 1

class TerrainMap:
    pipes = [Pipe()]
    nextPipeTimer = 1

    def movePipes(self):
        self.nextPipeTimer -= 1
        if self.nextPipeTimer < 0:
            self.pipes.append(Pipe())
            self.nextPipeTimer = 3
            if self.pipes[0].pipePos < 0:
				del self.pipes[0]
        for pipe in self.pipes:
            pipe.move()

    def display(self):
        for pipe in self.pipes:
            for pixel in pipe.getPixels():
                if pixel[0] >= 0 and pixel[0] < 5 and pixel[1] >= 0 and pixel[1] < 5:
                      setPixel(pixel[0], pixel[1], 9)


bird = Bird()
terrainMap = TerrainMap()
moveTimer = 0.0
prevFrameTime = running_time()
grid = [[0,0,0,0,0] for i in range(5)]
while True:
    terrainMap.pipes = []
    bird.reset()
    while True:
        for x in range(5):
            for y in range(5):
                grid[x][y] = 0

        delta = (running_time() - prevFrameTime) / 1000.0
        prevFrameTime = running_time()
        if button_a.was_pressed():
            bird.jump()

        bird.update(delta)
        bird.checkDeath(terrainMap)
        moveTimer += delta
        if moveTimer > 0.3:
            moveTimer = 0
            terrainMap.movePipes()
            
        bird.display()
        terrainMap.display()
        updateDisplay()
        if bird.resetGame:
            display.clear()
            sleep(500)
            break

