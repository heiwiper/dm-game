import pygame
import random
class First_window :
    def __init__(self):
        pass

    # read the data
    def reading_data(self, difficulty, known_transactions, unknown_transactions):
        # reading data from the known_transactions.txt
        with open('difficulty/'+difficulty+'/known_transactions.txt') as f:
            known_transactions_text = [line.rstrip('\n') for line in f] # transactions but with ','
            for i in range(0, len(known_transactions_text)):
                known_transactions.append(known_transactions_text[i].split(','))
        random.shuffle(known_transactions) #Randomly mix the transactions
        # reading data from the unknown_transactions.txt
        with open('difficulty/'+difficulty+'/known_transactions.txt') as f:
            unknown_transactions_text = [line.rstrip('\n') for line in f] # transactions but with ','
            for i in range(0, len(unknown_transactions_text)):
                unknown_transactions.append(unknown_transactions_text[i].split(','))
        random.shuffle(unknown_transactions) #Randomly mix the transactions

    def begin(self, screen, known_transactions, unknown_transactions):
        # first window loop
        begin_game = False
        while begin_game == False:
            background2 = pygame.image.load('assets/tiles/background2.png')
            screen.blit(background2, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if 290<pos[0]<360 and 227<pos[1]<258:
                        # easy mode selected
                        self.reading_data('easy', known_transactions, unknown_transactions)
                        begin_game = True
                    elif 278<pos[0]<392 and 298<pos[1]<331:
                        # normal mode selected
                        self.reading_data('normal', known_transactions, unknown_transactions)
                        begin_game = True
                    elif 296<pos[0]<367 and 372<pos[1]<408:
                        # hard mode chosen
                        self.reading_data('hard', known_transactions, unknown_transactions)
                        begin_game = True
