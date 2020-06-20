import random

import pygame

pygame.init()

size = screenWidth, screenHeight = 648, 720

#set size of the window
screen = pygame.display.set_mode(size)

# just the background image
background = pygame.image.load('./assets/tiles/background.png')
# where the objects hide the character
foreground = pygame.image.load('./assets/tiles/foreground.png')

# set title of the window
pygame.display.set_caption("Data Mining Game")

# helps determine the FPS
clock = pygame.time.Clock()

#load then play music
music = pygame.mixer.music.load("./assets/sounds/bgm.wav")
pygame.mixer.music.play(-1)

# loading characters sprites
# character_1
character_1_walkup = [pygame.image.load('./assets/sprites/character_1/U1.png'),
                      pygame.image.load('./assets/sprites/character_1/U2.png'),
                      pygame.image.load('./assets/sprites/character_1/U3.png'),
                      pygame.image.load('./assets/sprites/character_1/U4.png')]
character_1_walkdown = [pygame.image.load('./assets/sprites/character_1/D1.png'),
                        pygame.image.load('./assets/sprites/character_1/D2.png'),
                        pygame.image.load('./assets/sprites/character_1/D3.png'),
                        pygame.image.load('./assets/sprites/character_1/D4.png')]
character_1_walkright = [pygame.image.load('./assets/sprites/character_1/R1.png'),
                         pygame.image.load('./assets/sprites/character_1/R2.png'),
                         pygame.image.load('./assets/sprites/character_1/R3.png'),
                         pygame.image.load('./assets/sprites/character_1/R4.png')]
character_1_walkleft = [pygame.image.load('./assets/sprites/character_1/L1.png'),
                        pygame.image.load('./assets/sprites/character_1/L2.png'),
                        pygame.image.load('./assets/sprites/character_1/L3.png'),
                        pygame.image.load('./assets/sprites/character_1/L4.png')]
#character_2
character_2_walkup = [pygame.image.load('./assets/sprites/character_2/U2.png'),
                      pygame.image.load('./assets/sprites/character_2/U2.png'),
                      pygame.image.load('./assets/sprites/character_2/U3.png'),
                      pygame.image.load('./assets/sprites/character_2/U4.png')]
character_2_walkdown = [pygame.image.load('./assets/sprites/character_2/D2.png'),
                        pygame.image.load('./assets/sprites/character_2/D2.png'),
                        pygame.image.load('./assets/sprites/character_2/D3.png'),
                        pygame.image.load('./assets/sprites/character_2/D4.png')]
character_2_walkright = [pygame.image.load('./assets/sprites/character_2/R2.png'),
                         pygame.image.load('./assets/sprites/character_2/R2.png'),
                         pygame.image.load('./assets/sprites/character_2/R3.png'),
                         pygame.image.load('./assets/sprites/character_2/R4.png')]
character_2_walkleft = [pygame.image.load('./assets/sprites/character_2/L2.png'),
                        pygame.image.load('./assets/sprites/character_2/L2.png'),
                        pygame.image.load('./assets/sprites/character_2/L3.png'),
                        pygame.image.load('./assets/sprites/character_2/L4.png')]
#character_3
character_3_walkup = [pygame.image.load('./assets/sprites/character_3/U3.png'),
                      pygame.image.load('./assets/sprites/character_3/U2.png'),
                      pygame.image.load('./assets/sprites/character_3/U3.png'),
                      pygame.image.load('./assets/sprites/character_3/U4.png')]
character_3_walkdown = [pygame.image.load('./assets/sprites/character_3/D3.png'),
                        pygame.image.load('./assets/sprites/character_3/D2.png'),
                        pygame.image.load('./assets/sprites/character_3/D3.png'),
                        pygame.image.load('./assets/sprites/character_3/D4.png')]
character_3_walkright = [pygame.image.load('./assets/sprites/character_3/R3.png'),
                         pygame.image.load('./assets/sprites/character_3/R2.png'),
                         pygame.image.load('./assets/sprites/character_3/R3.png'),
                         pygame.image.load('./assets/sprites/character_3/R4.png')]
character_3_walkleft = [pygame.image.load('./assets/sprites/character_3/L3.png'),
                        pygame.image.load('./assets/sprites/character_3/L2.png'),
                        pygame.image.load('./assets/sprites/character_3/L3.png'),
                        pygame.image.load('./assets/sprites/character_3/L4.png')]
#character_4
character_4_walkup = [pygame.image.load('./assets/sprites/character_4/U4.png'),
                      pygame.image.load('./assets/sprites/character_4/U2.png'),
                      pygame.image.load('./assets/sprites/character_4/U3.png'),
                      pygame.image.load('./assets/sprites/character_4/U4.png')]
character_4_walkdown = [pygame.image.load('./assets/sprites/character_4/D4.png'),
                        pygame.image.load('./assets/sprites/character_4/D2.png'),
                        pygame.image.load('./assets/sprites/character_4/D3.png'),
                        pygame.image.load('./assets/sprites/character_4/D4.png')]
character_4_walkright = [pygame.image.load('./assets/sprites/character_4/R4.png'),
                         pygame.image.load('./assets/sprites/character_4/R2.png'),
                         pygame.image.load('./assets/sprites/character_4/R3.png'),
                         pygame.image.load('./assets/sprites/character_4/R4.png')]
character_4_walkleft = [pygame.image.load('./assets/sprites/character_4/L4.png'),
                        pygame.image.load('./assets/sprites/character_4/L2.png'),
                        pygame.image.load('./assets/sprites/character_4/L3.png'),
                        pygame.image.load('./assets/sprites/character_4/L4.png')]

right_arrow = pygame.image.load("./assets/gui/right_arrow.png")
left_arrow = pygame.image.load("./assets/gui/left_arrow.png")
arrowWidth = 14
center_transaction_bg = pygame.image.load("./assets/gui/center_transaction_background.png")
right_transaction_bg = pygame.image.load("./assets/gui/right_transaction_background.png")
left_transaction_bg = pygame.image.load("./assets/gui/left_transaction_background.png")
startingGame_bg = pygame.image.load("./assets/gui/transactions_screen.png")
transaction_bgWidth = 80

biscuit = pygame.image.load("./assets/items/biscuit.png")
burger = pygame.image.load("./assets/items/burger.png")
cheese = pygame.image.load("./assets/items/cheese.png")
chicken = pygame.image.load("./assets/items/chicken.png")
chocolate = pygame.image.load("./assets/items/chocolate.png")
croissant = pygame.image.load("./assets/items/croissant.png")
egg = pygame.image.load("./assets/items/egg.png")
fish = pygame.image.load("./assets/items/fish.png")
fruits = pygame.image.load("./assets/items/fruits.png")
honey = pygame.image.load("./assets/items/honey.png")
icecream = pygame.image.load("./assets/items/icecream.png")
meat = pygame.image.load("./assets/items/meat.png")
medicine = pygame.image.load("./assets/items/medicine.png")
milk = pygame.image.load("./assets/items/milk.png")
mushroom = pygame.image.load("./assets/items/mushroom.png")
pistachio = pygame.image.load("./assets/items/pistachio.png")
pizza = pygame.image.load("./assets/items/pizza.png")
shrimp = pygame.image.load("./assets/items/shrimp.png")
soda = pygame.image.load("./assets/items/soda.png")
sweets = pygame.image.load("./assets/items/sweets.png")
vegetables = pygame.image.load("./assets/items/vegetables.png")

known_transactions = [('chocolate', 'milk', 'croissant'),
                      ('pizza', 'burger', 'icecream'),
                      ('icecream', 'soda', 'pistachio'),
                      ('pistachio', 'chocolate', 'honey'),
                      ('fish', 'shrimp', 'sweets'), ('mushroom', 'medicine'),
                      ('fruits', 'chicken', 'cheese', 'meat'),
                      ('burger', 'icecream', 'pizza'),
                      ('biscuit', 'milk', 'egg'), ('sweets', 'shrimp', 'fish'),
                      ('chocolate', 'honey', 'pistachio'),
                      ('medicine', 'mushroom'),
                      ('pizza', 'burger', 'icecream'),
                      ('biscuit', 'milk', 'egg'),
                      ('honey', 'pistachio', 'chocolate'),
                      ('croissant', 'chocolate', 'milk'),
                      ('mushroom', 'medicine'),
                      ('chocolate', 'milk', 'croissant')]

known_transactions_counter = 0


# paths
path1 = [(280, 280), (180, 280), (180, 430), (180,120), (180, 280), (280, 280), (280, 230), (490, 230), (490, 400)]
path2 = [(280, 510), (80, 510), (80, 280), (280, 280), (280, 400), (490, 400)]
path3 = [(280, 230), (490, 230), (490, 190), (490, 400)]
path4 = [(280, 280), (80, 280), (80, 120), (80,510), (280, 510), (280, 400), (490, 400)]
pathsList = [path1, path2, path3, path4]

# the path from the counter to the exit door
exitPath = [(280, 400), (280, 600)]


class Client(object):
    def __init__(self):
        self.characterSize  = 80, 120
        self.characterWidth = 80
        self.characterHeight = 120
        self.x = 280
        self.y = 570

        # directions
        self.up = True  # the character should enter while going up
        self.down = False
        self.right = False
        self.left = False

        # the index of which tuple is the character at when walking through a certain path
        self.pathIndex = 0

        # last direction of where the character walked so to display him standing in that direction when he stops
        self.lastDirection = "none"

        # walking speed in pixels MUST NOT BE CHANGED BECAUSE IT MATCHES WITH THE PATH TUPLES also it's looking good
        self.step = 10

        # it tells if the client is still buying so that we can start the guessing game
        self.finishedShopping= False

        # frames index, helps to display sprites from 0 to 3
        self.walkCount = 0
        self.path = random.choice(pathsList)

        characterNumber = random.choice([1, 2, 3, 4])

        if characterNumber == 1:
            self.walkUp = character_1_walkup
            self.walkDown = character_1_walkdown
            self.walkRight = character_1_walkright
            self.walkLeft = character_1_walkleft
        elif characterNumber == 2:
            self.walkUp = character_2_walkup
            self.walkDown = character_2_walkdown
            self.walkRight = character_2_walkright
            self.walkLeft = character_2_walkleft
        elif characterNumber == 3:
            self.walkUp = character_3_walkup
            self.walkDown = character_3_walkdown
            self.walkRight = character_3_walkright
            self.walkLeft = character_3_walkleft
        elif characterNumber == 4:
            self.walkUp = character_4_walkup
            self.walkDown = character_4_walkdown
            self.walkRight = character_4_walkright
            self.walkLeft = character_4_walkleft

    def draw(self):
        if self.walkCount >= 4:
            self.walkCount = 0

        if self.up:
            screen.blit(self.walkUp[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            screen.blit(self.walkDown[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(self.walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.left:
            screen.blit(self.walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.lastDirection == "up":
                screen.blit(self.walkUp[0], (self.x, self.y))
            elif self.lastDirection == "down":
                screen.blit(self.walkDown[0], (self.x, self.y))
            elif self.lastDirection == "right":
                screen.blit(self.walkRight[0], (self.x, self.y))
            elif self.lastDirection == "left":
                screen.blit(self.walkLeft[0], (self.x, self.y))
            else:
                screen.blit(self.walkDown[0], (self.x, self.y))

    def do_shopping(self):
        self.walk_through_path()
        if (self.x, self.y) == (490, 400):
            self.finishedShopping = True  # to launch the guessing game the next time in the main loop
    # uses move_to to move to all the coordinates in a path one after the other until the path ends
    def walk_through_path(self):
        if self.path is not None:
            if self.pathIndex < self.path.__len__():  # if the client didn't reach the end of the path (the counter)
                self.move_to(*self.path[self.pathIndex])  # he moves to the next checkpoint
                if (self.x, self.y) == (self.path[self.pathIndex]):  # if he actually reached the checkpoint
                    self.pathIndex += 1
                    # when the character arrives to the counter
                    if self.pathIndex >= self.path.__len__() and not (self.x, self.y) == (280, 600):
                        self.lastDirection = "down"  # to make the character look down when he arrives to the counter
                        self.pathIndex = 0

    # uses the move_in_direction to move the character to a certain coordinates in the order right left down up
    def move_to(self, x, y):
        if x <= screenWidth and self.x < x:
            self.move_in_direction("right")
        elif x >= 0 and self.x > x:
            self.move_in_direction("left")
        elif y <= screenHeight and self.y < y:
            self.move_in_direction("down")
        elif y >= 0 and self.y > y:
            self.move_in_direction("up")

    # moves the character one step in a given direction
    def move_in_direction(self, direction):
        if direction == "up" and self.y - self.step >= 0:
            self.up = True
            self.lastDirection = "up"
            self.y -= self.step

        elif direction == "down" and self.y + self.characterHeight + self.step <= screenHeight:
            self.down = True
            self.lastDirection = "down"
            self.y += self.step

        elif direction == "right" and self.x + self.characterWidth + self.step <= screenWidth:
            self.right = True
            self.lastDirection = "right"
            self.x += self.step

        elif direction == "left" and self.x - self.step >= 0:
            self.left = True
            self.lastDirection = "left"
            self.x -= self.step

    # moves the character from the counter to the exit door
    def leave_store(self):
        if exitPath is not None:
            if self.pathIndex < exitPath.__len__():
                self.move_to(*exitPath[self.pathIndex])
                if (self.x, self.y) == (exitPath[self.pathIndex]):
                    self.pathIndex += 1
                    # when the character is walking through the exit path and he arrives to the the exit door
                    if (self.x, self.y) == (280, 600):
                        self.pathIndex = 0

    def clear_directions(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False

class Player(object):
    def __init__(self):
        self.score = 0

class Transaction(object):
    def __init__(self, itemsList):
        # self.itemsList = self.generate_items()
        self.itemsList = itemsList
        # if self.itemsList is not None:
        #     known_transactions_counter += 1
    def generate_items(self):
        if known_transactions_counter < known_transactions.__len__():
            return known_transactions[known_transactions_counter]
        else:
            return None
    def draw(self, row):
        screen.blit(left_transaction_bg, (0, row*130))
        for i in range(0, self.itemsList.__len__()):
            screen.blit(center_transaction_bg, (transaction_bgWidth*(i+1), row*130))
            self.draw_item(i, row)
        screen.blit(right_transaction_bg, (transaction_bgWidth*(self.itemsList.__len__()+1), row*130))
    def draw_item(self, i, row):
        if self.itemsList[i] is "biscuit":
            screen.blit(biscuit, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "burger":
            screen.blit(burger, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "cheese":
            screen.blit(cheese, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "chicken":
            screen.blit(chicken, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "chocolate":
            screen.blit(chocolate, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "croissant":
            screen.blit(croissant, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "egg":
            screen.blit(egg, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "fish":
            screen.blit(fish, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "fruits":
            screen.blit(fruits, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "honey":
            screen.blit(honey, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "icecream":
            screen.blit(icecream, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "meat":
            screen.blit(meat, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "medicine":
            screen.blit(medicine, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "milk":
            screen.blit(milk, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "mushroom":
            screen.blit(mushroom, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "pistachio":
            screen.blit(pistachio, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "pizza":
            screen.blit(pizza, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "shrimp":
            screen.blit(shrimp, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "soda":
            screen.blit(soda, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "sweets":
            screen.blit(sweets, (transaction_bgWidth*(i + 1) , row*130))
        elif self.itemsList[i] is "vegetables":
            screen.blit(vegetables, (transaction_bgWidth*(i + 1) , row*130))



def redrawGameWindow():
    # draws background, character then foreground

    clock.tick(20)
    screen.blit(background, (0, 0))
    if shopping or guessingGame:
        if client is not None:
            client.draw()
        screen.blit(foreground, (0, 0))

    # Guessing game drawing should be here to come on top of the rest

    if startingGame:
        screen.blit(startingGame_bg, (0, 0))
        display_known_transactions(knownTransactionsIndex)
        screen.blit(left_arrow, (screenWidth/2-(arrowWidth+3), screenHeight - 30))
        screen.blit(right_arrow, (screenWidth/2+3, screenHeight - 30))

    pygame.display.update()
    clock.tick(30)

def display_known_transactions(index):
    for i in range(0,TRANSACTIONS_PER_PAGE):
        if i+index*TRANSACTIONS_PER_PAGE < known_transactions.__len__():
            transactionsList[i+index*TRANSACTIONS_PER_PAGE].draw(i)
        else:
            break

def guessing_game():
    # this function should have the code of the guessing game which will set gessingGame to False when finishing

    global client
    global shopping
    global guessingGame

    # guessing game code should be here
    # when drawing something do it in the redrawGameWindow() and put it right before the update function call
    # you can also create a class for that and call it's drawing function from redrawGameWindow()

    client.leave_store()  # delete this after adding guessing_game code and add it when the guessing game finishes
    if (client.x, client.y) == (280, 600):
        client = None  # to generate a new client and set a new path for him
        guessingGame = False
        shopping = True


client = None

mainMenu = True
startingGame = False
shopping = False
guessingGame = False

transactionsList = []
knownTransactionsIndex = 0
TRANSACTIONS_PER_PAGE = 4

# main loop
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if mainMenu:
        print("Main menu")
        i = 0
        while i < known_transactions.__len__():
            transaction = Transaction(known_transactions[i])
            transactionsList.append(transaction)
            i += 1

        mainMenu = False
        startingGame = True
    elif startingGame:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and (knownTransactionsIndex+1) * TRANSACTIONS_PER_PAGE < known_transactions.__len__():
            knownTransactionsIndex += 1

        elif keys[pygame.K_LEFT] and knownTransactionsIndex > 0:
            knownTransactionsIndex -= 1

        elif keys[pygame.K_SPACE]:
            startingGame = False
            shopping = True

    elif shopping:
        if client is None:
            client = Client()
        else:
            client.clear_directions()

        if not client.finishedShopping:
            client.do_shopping()

        else:
            shopping = False
            guessingGame = True
    elif guessingGame:
        guessing_game()

    redrawGameWindow()


# leave the game
pygame.quit()
