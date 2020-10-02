import pygame

pygame.init()

size = screenWidth, screenHeight = 648, 720

characterSize = characterWidth, characterHeight = 96, 144
characterX = 0
characterY = 0

# loading character sprites
walkUp = [pygame.image.load('./sprites/character_1/U1.png'), pygame.image.load('./sprites/character_1/U2.png'), pygame.image.load('./sprites/character_1/U3.png'), pygame.image.load('./sprites/character_1/U4.png')]
walkDown = [pygame.image.load('./sprites/character_1/D1.png'), pygame.image.load('./sprites/character_1/D2.png'), pygame.image.load('./sprites/character_1/D3.png'), pygame.image.load('./sprites/character_1/D4.png')]
walkRight = [pygame.image.load('./sprites/character_1/R1.png'), pygame.image.load('./sprites/character_1/R2.png'), pygame.image.load('./sprites/character_1/R3.png'), pygame.image.load('./sprites/character_1/R4.png')]
walkLeft = [pygame.image.load('./sprites/character_1/L1.png'), pygame.image.load('./sprites/character_1/L2.png'), pygame.image.load('./sprites/character_1/L3.png'), pygame.image.load('./sprites/character_1/L4.png')]

# directions
up = False
down = False
right = False
left = False

lastDirection = "none"

step = 10 # walking speed in pixels

walkCount = 0 # frames imdex

#set size of the window
screen = pygame.display.set_mode(size)

background = pygame.image.load('tiles/background.png')
foreground = pygame.image.load('tiles/foreground.png')

# set title of the window
pygame.display.set_caption("Data Mining Game")

clock = pygame.time.Clock()

# draws background, character then foreground
def redrawGameWindow():
    clock.tick(20)
    global walkCount

    screen.blit(background, (0,0))

    if walkCount >= 4:
        walkCount = 0

    if up:
        screen.blit(walkUp[walkCount], (characterX, characterY))
        walkCount += 1
    elif down:
        screen.blit(walkDown[walkCount], (characterX, characterY))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount], (characterX, characterY))
        walkCount += 1
    elif left:
        screen.blit(walkLeft[walkCount], (characterX, characterY))
        walkCount += 1
    else:
        if lastDirection == "up":
            screen.blit(walkUp[0], (characterX, characterY))
        elif lastDirection == "down":
            screen.blit(walkDown[0], (characterX, characterY))
        elif lastDirection == "right":
            screen.blit(walkRight[0], (characterX, characterY))
        elif lastDirection == "left":
            screen.blit(walkLeft[0], (characterX, characterY))
        else:
            screen.blit(walkDown[0], (characterX, characterY))

    screen.blit(foreground, (0,0))
    pygame.display.update()
    clock.tick(30)


# detects key presses and perform actions accordingly
def keys_handler():
    global characterX
    global characterY
    global up, down, right, left
    global lastDirection
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and characterY - step >= 0:
        up = True
        lastDirection = "up"
        walkCount = 0
        characterY -= step

    elif keys[pygame.K_DOWN] and characterY + characterHeight + step <= screenHeight:
        down = True
        lastDirection = "down"
        walkCount = 0
        characterY += step

    elif keys[pygame.K_RIGHT] and characterX + characterWidth + step <= screenWidth:
        right = True
        lastDirection = "right"
        walkCount = 0
        characterX += step

    elif keys[pygame.K_LEFT] and characterX - step >= 0:
        left = True
        lastDirection = "left"
        walkCount = 0
        characterX -= step
    elif keys[pygame.K_SPACE]:
        print("{}, {}, {}".format(characterX, characterY, lastDirection))


# main loop
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys_handler()

    redrawGameWindow()

    up = False
    down = False
    right = False
    left = False

# leave the game
pygame.quit()
