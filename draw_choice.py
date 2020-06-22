import collections
import random
from random import choice, randint
import pygame

class Draw_choice :
    known_objects, unknown_objects, choices, false_choice = ([],)*4
    right_circle, left_circle, enchainement_player, enchainement_algo, score_is_calculated, is_drawn= False, False, False, False, False, False
    right_choice_id, score_player, score_algo = -1,0,0

    @staticmethod
    def put_objects_bubble(screen, bubble, objects):
        if bubble == 0:
            x1, y1, x2 = 310, 180, 240
        elif bubble == 1:
            x1, y1, x2 = 455, 400, 385
        else :
            x1, y1, x2 = 155, 400, 85
        for i in range(0, len(objects)):
            str = 'assets/items/'+objects[i]+'.png'
            image_known_objects = pygame.image.load(str)
            if i>=2 :
                screen.blit(image_known_objects, (x1, y1+70*(i-2)))
            else :
                screen.blit(image_known_objects, (x2, y1+70*i))

    # draw the bubbles and the text
    @staticmethod
    def draw_bubbles_text(screen):
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

    @staticmethod
    def draw(screen,num_transaction,unknown_transactions,objects,apriori):
        transaction = unknown_transactions[num_transaction]
        random.shuffle(transaction) #Randomly mix the transaction
        # draw the bubbles of choices and text
        Draw_choice.draw_bubbles_text(screen)
        # distributes false and real objects
        if Draw_choice.is_drawn == False : # to avoid re-executing instructions multiple times
            if len(transaction) > 4 :
                number_known_objects = randint(len(transaction)-4,4)
            else :
                number_known_objects = randint(1, len(transaction)-1)
            number_unknown_objects = len(transaction) - number_known_objects
            Draw_choice.known_objects = []
            Draw_choice.unknown_objects = []
            for i in range(0, len(transaction)):
                if(i<number_known_objects):
                    Draw_choice.known_objects.append(transaction[i])
                else:
                    Draw_choice.unknown_objects.append(transaction[i])
            Draw_choice.false_choice = []
            Draw_choice.choices = []
            # create the vector of possible choices
            while True :
                Draw_choice.false_choice = []
                for i in range(0, number_unknown_objects):
                    Draw_choice.false_choice.append(choice(objects))
                if collections.Counter(Draw_choice.unknown_objects)!= collections.Counter(Draw_choice.false_choice):
                    break
            if(randint(0,10)<5):
                Draw_choice.choices.append(Draw_choice.unknown_objects)
                Draw_choice.choices.append(Draw_choice.false_choice)
                Draw_choice.right_choice_id = 0
            else :
                Draw_choice.choices.append(Draw_choice.false_choice)
                Draw_choice.choices.append(Draw_choice.unknown_objects)
                Draw_choice.right_choice_id = 1
            Draw_choice.is_drawn = True

        # calculate the score (only once that's why we use this condition)
        if (Draw_choice.right_circle or Draw_choice.left_circle) and Draw_choice.score_is_calculated == False :
            if Draw_choice.right_circle :
                player_choice = 0
            else :
                player_choice = 1
            Draw_choice.old_score_player = Draw_choice.score_player
            if(player_choice == Draw_choice.right_choice_id) :
                if(Draw_choice.enchainement_player == True):
                    Draw_choice.score_player *= 2
                else :
                    Draw_choice.score_player += 20
            if(Draw_choice.old_score_player==Draw_choice.score_player) :
                Draw_choice.enchainement_player = False
            else :
                Draw_choice.enchainement_player = True
            Draw_choice.score_is_calculated = True
            # The apriori algorithm guesses the shopping list
            algo_choice = apriori.choice_apriori(Draw_choice.known_objects, Draw_choice.choices)
            Draw_choice.old_score_algo = Draw_choice.score_algo
            if(algo_choice == Draw_choice.right_choice_id):
                if(Draw_choice.enchainement_algo == True):
                    Draw_choice.score_algo *= 2
                else :
                    Draw_choice.score_algo += 20
            if(Draw_choice.old_score_algo==Draw_choice.score_algo):
                Draw_choice.enchainement_algo = False
            else :
                Draw_choice.enchainement_algo = True
        # drawing the bubbles after the player chooses
        if Draw_choice.right_circle and Draw_choice.right_choice_id == 0:
            choice_image = pygame.image.load('assets/items/right_choice.png')
            screen.blit(choice_image, (350, 370))
        elif Draw_choice.left_circle and Draw_choice.right_choice_id == 1:
            choice_image = pygame.image.load('assets/items/right_choice.png')
            screen.blit(choice_image, (50, 370))
        elif Draw_choice.right_circle and Draw_choice.right_choice_id == 1:
            choice_image = pygame.image.load('assets/items/bad_choice.png')
            screen.blit(choice_image, (350, 370))
        elif Draw_choice.left_circle and Draw_choice.right_choice_id == 0:
            choice_image = pygame.image.load('assets/items/bad_choice.png')
            screen.blit(choice_image, (50, 370))
        # put the objects in the bubbles :
        Draw_choice.put_objects_bubble(screen, 0, Draw_choice.known_objects)
        Draw_choice.put_objects_bubble(screen, 1, Draw_choice.choices[0])
        Draw_choice.put_objects_bubble(screen, 2, Draw_choice.choices[1])
