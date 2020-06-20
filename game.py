import collections
import random
from random import choice, randint

import pygame

from apriori import Apriori

pygame.init()
pygame.font.init()
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
arrowWidth = 50
center_transaction_bg = pygame.image.load("./assets/gui/center_transaction_background.png")
right_transaction_bg = pygame.image.load("./assets/gui/right_transaction_background.png")
left_transaction_bg = pygame.image.load("./assets/gui/left_transaction_background.png")
startingGame_bg = pygame.image.load("./assets/gui/transactions_screen.png")
transaction_bgWidth = 60

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
        self.itemsList = itemsList
        self.rowHeight = 120
    def draw(self, row):
        screen.blit(left_transaction_bg, (0, row*self.rowHeight))
        for i in range(0, self.itemsList.__len__()):
            screen.blit(center_transaction_bg, (transaction_bgWidth*(i+1), row*self.rowHeight))
            self.draw_item(i, row)
        screen.blit(right_transaction_bg, (transaction_bgWidth*(self.itemsList.__len__()+1), row*self.rowHeight))
    def draw_item(self, i, row):
        font = pygame.font.SysFont('Arial', 18)
        text = font.render(self.itemsList[i], False, (255,255,255))
        text_rect = text.get_rect()
        screen.blit(text, ((2*transaction_bgWidth*(i + 1) +transaction_bgWidth)/2 - text_rect.width/2, row*self.rowHeight + 65))
        if self.itemsList[i] == "biscuit":
            screen.blit(biscuit, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "burger":
            screen.blit(burger, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "cheese":
            screen.blit(cheese, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "chicken":
            screen.blit(chicken, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "chocolate":
            screen.blit(chocolate, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "croissant":
            screen.blit(croissant, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "egg":
            screen.blit(egg, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "fish":
            screen.blit(fish, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "fruits":
            screen.blit(fruits, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "honey":
            screen.blit(honey, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "icecream":
            screen.blit(icecream, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "meat":
            screen.blit(meat, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "medicine":
            screen.blit(medicine, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "milk":
            screen.blit(milk, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "mushroom":
            screen.blit(mushroom, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "pistachio":
            screen.blit(pistachio, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "pizza":
            screen.blit(pizza, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "shrimp":
            screen.blit(shrimp, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "soda":
            screen.blit(soda, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "sweets":
            screen.blit(sweets, (transaction_bgWidth*(i + 1) , row*self.rowHeight))
        elif self.itemsList[i] == "vegetables":
            screen.blit(vegetables, (transaction_bgWidth*(i + 1) , row*self.rowHeight))


# returns the number of common elements between two arrays
def count(tab1, tab2):
    count = 0
    for i in range(0, len(tab1)):
        for j in range(0, len(tab2)):
            if tab1[i] == tab2[j] :
                count+=1
    return count

# returns the index of the array which contains the most common elements
def search_index(tab1, tab2):
    index = randint(0, len(tab1)-1)
    nbr_common_elements = 0
    for i in range(0, len(tab1)):
        nbr = count(tab1[i], tab2)
        if(nbr > nbr_common_elements) :
            nbr_common_elements = nbr
            index = i
    return index

# returns the choice of the apriori algorithm
def choice_apriori():
    global known_objects
    global choices
    global antecedents
    global consequents
    index = search_index(antecedents, known_objects)
    choice = search_index(choices, consequents[index])
    return choice

# draw the score
def draw_score():
    global score_player
    global score_algo
    font = pygame.font.SysFont('Arial', 18)
    font.set_bold(True)
    text3 = font.render('SCORE DU JOUEUR : '+str(score_player), False, (47,60,126), (251,234,235))
    text4 = font.render("SCORE DE L'ALGORITHME APRIORI : "+str(score_algo), False, (47,60,126), (251,234,235))
    screen.blit(text3, (50,50))
    screen.blit(text4, (50,80))

# draw the bubbles and the text
def draw_bubbles_text():
    font = pygame.font.SysFont('Comic Sans MS', 25)
    font.set_bold(True)
    text1 = font.render('Le client a acheté :', False, (220,20,60), (255,250,205))
    text2 = font.render("Deviner ce qu'il a acheté aussi :", False, (220,20,60), (255,250,205))
    screen.blit(text1, (170, 120))
    screen.blit(text2, (100, 345))
    choice_image = pygame.image.load('assets/items/choice.png')
    screen.blit(choice_image, (200, 150))
    screen.blit(choice_image, (350, 370))
    screen.blit(choice_image, (50, 370))

def redrawGameWindow():
    # draws background, character then foreground
    global guessingGame
    clock.tick(20)
    screen.blit(background, (0, 0))
    if shopping or guessingGame:
        if client is not None:
            client.draw()
            screen.blit(foreground, (0, 0))
        draw_score()
        if guessingGame == True :
            draw_choice()

    if startingGame:
        screen.blit(startingGame_bg, (0, 0))
        display_known_transactions(knownTransactionsIndex)

    pygame.display.update()
    clock.tick(30)

def display_known_transactions(index):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render("Appuyez sur 'Espace' quand vous serai pret", False, (255,255,255))
    text_rect = text.get_rect()
    screen.blit(text, ((screenWidth/2 - text_rect.width/2, screenHeight - 100)))
    if not knownTransactionsIndex == 0:
        screen.blit(left_arrow, (screenWidth/2-(arrowWidth+3), screenHeight - 50))
    if (knownTransactionsIndex+1) * TRANSACTIONS_PER_PAGE < known_transactions.__len__():
        screen.blit(right_arrow, (screenWidth/2+3, screenHeight - 50))
    for i in range(0,TRANSACTIONS_PER_PAGE):
        if i+index*TRANSACTIONS_PER_PAGE < known_transactions.__len__():
            transactionsList[i+index*TRANSACTIONS_PER_PAGE].draw(i)
        else:
            break

def draw_choice():
    global num_transaction
    global unknown_transactions
    global number_known_objects
    global number_unknown_objects
    global known_objects
    global unknown_objects
    global choices
    global is_drawn
    global guessingGame
    global right_choice_id
    global left_circle
    global right_circle
    global score_algo
    global score_player
    global enchainement_player
    global enchainement_algo
    global score_is_calculated
    global objects
    transaction = unknown_transactions[num_transaction]
    random.shuffle(transaction) #Randomly mix the transaction
    # draw the bubbles of choices and text
    draw_bubbles_text()
    # distributes false and real objects
    if is_drawn == False : # to avoid re-executing instructions multiple times
        if len(transaction) > 4 :
            number_known_objects = randint(len(transaction)-4,4)
        else :
            number_known_objects = randint(1, len(transaction))
        number_unknown_objects = len(transaction) - number_known_objects
        known_objects = []
        unknown_objects = []
        for i in range(0, len(transaction)):
            if(i<number_known_objects):
                known_objects.append(transaction[i])
            else:
                unknown_objects.append(transaction[i])
        false_choice = []
        choices = []
        # create the vector of possible choices
        if(randint(0,10)<5): # here the true choice has the id=0 it means he's on the right
            while True :
                choices = []
                false_choice = []
                # add the right choice first
                choices.append(unknown_objects)
                right_choice_id = 0
                # then randomly add another choice
                for i in range(0, number_unknown_objects):
                    false_choice.append(choice(objects))
                choices.append(false_choice)
                # the choices must be different
                if collections.Counter(choices[0]) != collections.Counter(choices[1]) :
                    break
        else : # here the true choice has the id=1 it means he's on the left
            while True :
                false_choice = []
                choices = []
                # randomly add a wrong choice
                for i in range(0, number_unknown_objects):
                    false_choice.append(choice(objects))
                choices.append(false_choice)
                # then add the right choice
                choices.append(unknown_objects)
                right_choice_id = 1
                # the choices must be different
                if collections.Counter(choices[0]) != collections.Counter(choices[1]) :
                    break
        is_drawn = True

    # calculate the score (only once that's why we use this condition)
    if (right_circle or left_circle) and score_is_calculated == False :
        if right_circle :
            player_choice = 0
        else :
            player_choice = 1
        old_score_player = score_player
        if(player_choice == right_choice_id) :
            if(enchainement_player == True):
                score_player *= 2
            else :
                score_player += 20
        if(old_score_player==score_player) :
            enchainement_player = False
        else :
            enchainement_player = True
        score_is_calculated = True
        # The apriori algorithm guesses the shopping list
        algo_choice = choice_apriori()
        old_score_algo = score_algo
        if(algo_choice == right_choice_id):
            if(enchainement_algo == True):
                score_algo *= 2
            else :
                score_algo += 20
        if(old_score_algo==score_algo):
            enchainement_algo = False
        else :
            enchainement_algo = True
    # drawing the bubbles after the player chooses
    if right_circle and right_choice_id == 0:
        choice_image = pygame.image.load('assets/items/right_choice.png')
        screen.blit(choice_image, (350, 370))
    elif left_circle and right_choice_id == 1:
        choice_image = pygame.image.load('assets/items/right_choice.png')
        screen.blit(choice_image, (50, 370))
    elif right_circle and right_choice_id == 1:
        choice_image = pygame.image.load('assets/items/bad_choice.png')
        screen.blit(choice_image, (350, 370))
    elif left_circle and right_choice_id == 0:
        choice_image = pygame.image.load('assets/items/bad_choice.png')
        screen.blit(choice_image, (50, 370))
    # put the objects in the bubbles :
    # put the objects in the first bubble
    for i in range(0, number_known_objects):
        str = 'assets/items/'+known_objects[i]+'.png'
        image_known_objects = pygame.image.load(str)
        if i>=2 :
            screen.blit(image_known_objects, (295, 170+70*(i-2)))
        else :
            screen.blit(image_known_objects, (225, 170+70*i))
    # put the objects in the second bubble
    for i in range(0, len(choices[0])):
        str = 'assets/items/'+choices[0][i]+'.png'
        image_known_objects = pygame.image.load(str)
        if i>=2 :
            screen.blit(image_known_objects, (440, 390+70*(i-2)))
        else :
            screen.blit(image_known_objects, (370, 390+70*i))
    # put the objects in the third bubble
    for i in range(0, len(choices[1])):
        str = 'assets/items/'+choices[1][i]+'.png'
        image_known_objects = pygame.image.load(str)
        if i>=2 :
            screen.blit(image_known_objects, (140, 390+70*(i-2)))
        else :
            screen.blit(image_known_objects, (70, 390+70*i))

def guessing_game():
    global client
    global shopping
    global guessingGame
    global num_transaction
    global is_drawn
    global left_circle
    global right_circle
    global score_is_calculated
    guessingGame = True
    if left_circle or right_circle :
        client.leave_store()
        if (client.x, client.y) == (280, 600):
            left_circle = False
            right_circle = False
            guessingGame = False
            client = None  # to generate a new client and set a new path for him
            num_transaction += 1
            is_drawn = False
            score_is_calculated = False
            client = Client()
            guessingGame = False
            shopping = True



num_transaction = 0
known_transactions = []
# reading data from the known_transactions.txt
with open('known_transactions.txt') as f:
    known_transactions_text = [line.rstrip('\n') for line in f] # transactions but with ','
    for i in range(0, len(known_transactions_text)):
        known_transactions.append(known_transactions_text[i].split(','))
random.shuffle(known_transactions) #Randomly mix the transactions

unknown_transactions = []
# reading data from the unknown_transactions.txt
with open('unknown_transactions.txt') as f:
    unknown_transactions_text = [line.rstrip('\n') for line in f] # transactions but with ','
    for i in range(0, len(unknown_transactions_text)):
        unknown_transactions.append(unknown_transactions_text[i].split(','))
random.shuffle(unknown_transactions) #Randomly mix the transactions

objects = []
# reading data from the objects.txt
with open('objects.txt') as f:
    objects = [line.rstrip('\n') for line in f]

client = None

mainMenu = True
startingGame = False
shopping = False
guessingGame = False

transactionsList = []
knownTransactionsIndex = 0
TRANSACTIONS_PER_PAGE = 5
number_known_objects = 0
number_unknown_objects = 0
known_objects = []
unknown_objects = []
choices = []
is_drawn = False
right_choice_id = -1
right_circle = False
left_circle = False
score_player = 0
score_algo = 0
enchainement_player = False
enchainement_algo = False
score_is_calculated = False
client = Client()
apriori = Apriori(known_transactions)
antecedents, consequents = apriori.get_rules()
# main loop
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if guessingGame == True :
                pos = pygame.mouse.get_pos()
                # check if the player has clicked on the right circle
                if((pos[0] - 454)**2 + (pos[1] - 441)**2 < 93**2):
                    right_circle = True
                # check if the player has clicked on the left circle
                elif ((pos[0] - 153)**2 + (pos[1] - 441)**2 < 93**2):
                    left_circle = True

    if mainMenu:
        print("Main menu")
        i = 0
        while i < known_transactions.__len__():
            transaction = Transaction(known_transactions[i])
            transactionsList.append(transaction)
            print(known_transactions[i])
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
        # transactions are completed
        if num_transaction > len(unknown_transactions)-1:
            break

    redrawGameWindow()


# leave the game
pygame.quit()
