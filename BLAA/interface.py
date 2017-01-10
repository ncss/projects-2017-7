import microbit
import random
import radio

radio.on()
radio.config(channel=65, address=0x6e637373)

grid = []

def setPixel(x, y, brightness):
    if x >= 0 and x < 5 and y >= 0 and y < 5:
        grid[x][y] = brightness

def updateDisplay():
    for x in range(0, 5):
        for y in range(0, 5):
            microbit.display.set_pixel(x, y, grid[x][y])

class Player:
    dead = False
    gravity = 15.0
    jumpVelocity = 20.0
    isCrouching = False
    
    def reset(self):
        self.pos = 0.0
        self.velocity = 0.0
        self.dead = False
        self.deathTimer = 0.0
        self.resetGame = False
        self.isCrouching = False
        self.crouchTimer = 0
        self.hidden = False
        self.score = 0
        self.timeAlive = 0

    def jump(self):
        self.velocity = self.jumpVelocity

    def update(self, delta):
        self.timeAlive += delta
        self.velocity -= self.gravity * delta
        self.pos += self.velocity * delta
        if self.pos <= 0.0:
            self.pos = 0.0
            self.velocity = 0.0
        if self.pos >= 3.99:
            self.pos = 3.99
            self.velocity = 0.0
        if self.isCrouching:
          self.crouchTimer += delta
          if self.crouchTimer > 0.75:
            self.crouchTimer = 0.0
            self.isCrouching = False
        if self.dead:
          self.deathTimer += delta
          self.hidden = self.deathTimer % 0.1 > 0.05
          if self.deathTimer > 0.5:
            self.deathTimer = 0.0
            self.dead = False
 
    def getPixelPos(self):
      pixelPos = [(0, 4 - int(self.pos))]
      if not self.isCrouching: pixelPos.append((0, 4 - int(self.pos) - 1))
      return pixelPos
        
    def display(self):
      pixelPos = self.getPixelPos()
      for pixel in pixelPos:
        setPixel(pixel[0], pixel[1], 9 if not self.hidden else 0)
        
    def checkDeath(self, terrainMap):
        playerPos = self.getPixelPos()
        for pipe in terrainMap.pipes:
            if self.dead: continue
            for pixel in pipe.getPixels():
              for playerPixel in playerPos:
                if pixel[0] == playerPixel[0] and pixel[1] == playerPixel[1]:
                    self.dead = True
                    self.score -= 1
                    radio.send("impact")
                    return

class Pipe:
    def __init__(self):
        self.pipeType = random.randint(0,1)
        if self.pipeType == 0: self.pipeHeight = random.randint(1,2)
        else: self.pipeHeight = random.randint(3,4)
        self.pipePos = 5
  
    def getPixels(self):
        pixels = []
        pipeRange = range(1)
        if self.pipeType == 0: pipeRange = range(4, 4 - self.pipeHeight, -1)
        else: pipeRange = range(self.pipeHeight)
        for i in pipeRange:
            pixels.append((self.pipePos, i))
        return pixels

    def move(self, player):
        self.pipePos -= 1
        if self.pipePos == -1:
            player.score += 1

class TerrainMap:
    pipes = [Pipe()]
    nextPipeTimer = 1

    def movePipes(self, player):
        self.nextPipeTimer -= 1
        if self.nextPipeTimer < 0:
            self.pipes.append(Pipe())
            self.nextPipeTimer = 8
            if self.pipes[0].pipePos < 0:
              del self.pipes[0]
        for pipe in self.pipes:
            pipe.move(player)

    def display(self):
        for pipe in self.pipes:
            for pixel in pipe.getPixels():
                setPixel(pixel[0], pixel[1], 9)


player = Player()
terrainMap = TerrainMap()
moveTimer = 0.0
prevFrameTime = microbit.running_time()
grid = [[0,0,0,0,0] for i in range(5)]
while True:
    terrainMap.pipes = []
    player.reset()
    while True:
        for x in range(5):
            for y in range(5):
                grid[x][y] = 0

        delta = (microbit.running_time() - prevFrameTime) / 1000.0
        prevFrameTime = microbit.running_time()
        if microbit.button_a.was_pressed(): player.jump()
        if microbit.button_b.was_pressed(): player.isCrouching = True
        
        message = radio.receive()
        if message and type(message) == str:
          if str(message) == "jump":
            player.jump()
          if str(message) == "crouch":
            player.isCrouching = True
        player.update(delta)

        player.checkDeath(terrainMap)
        moveTimer += delta
        if moveTimer > 0.3 - (player.timeAlive * 0.0015):
            moveTimer = 0
            terrainMap.movePipes(player)
        terrainMap.display()
        player.display()
        updateDisplay()
        if player.timeAlive > 60:
          microbit.display.scroll(str(player.score) + "pts!")
          break
