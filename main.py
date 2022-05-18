
import pygame
import sys
import random
import time

WIDTH = 700
HEIGHT = 700

one_h = pygame.image.load('hearts/1h.png')
two_h = pygame.image.load('hearts/2h.png')
three_h = pygame.image.load('hearts/3h.png')
four_h = pygame.image.load('hearts/4h.png')
five_h = pygame.image.load('hearts/5h.png')
six_h = pygame.image.load('hearts/6h.png')
seven_h = pygame.image.load('hearts/7h.png')
eight_h = pygame.image.load('hearts/8h.png')
nine_h = pygame.image.load('hearts/9h.png')
ten_h = pygame.image.load('hearts/10h.png')
jack_h = pygame.image.load('hearts/jh.png')
queen_h = pygame.image.load('hearts/qh.png')
king_h = pygame.image.load('hearts/kh.png')

one_d = pygame.image.load('diamonds/1d.png')
two_d = pygame.image.load('diamonds/2d.png')
three_d = pygame.image.load('diamonds/3d.png')
four_d = pygame.image.load('diamonds/4d.png')
five_d = pygame.image.load('diamonds/5d.png')
six_d = pygame.image.load('diamonds/6d.png')
seven_d = pygame.image.load('diamonds/7d.png')
eight_d = pygame.image.load('diamonds/8d.png')
nine_d = pygame.image.load('diamonds/9d.png')
ten_d = pygame.image.load('diamonds/10d.png')
jack_d = pygame.image.load('diamonds/jd.png')
queen_d = pygame.image.load('diamonds/qd.png')
king_d = pygame.image.load('diamonds/kd.png')

one_s = pygame.image.load('spades/1s.png')
two_s = pygame.image.load('spades/2s.png')
three_s = pygame.image.load('spades/3s.png')
four_s = pygame.image.load('spades/4s.png')
five_s = pygame.image.load('spades/5s.png')
six_s = pygame.image.load('spades/6s.png')
seven_s = pygame.image.load('spades/7s.png')
eight_s = pygame.image.load('spades/8s.png')
nine_s = pygame.image.load('spades/9s.png')
ten_s = pygame.image.load('spades/10s.png')
jack_s = pygame.image.load('spades/js.png')
queen_s = pygame.image.load('spades/qs.png')
king_s = pygame.image.load('spades/ks.png')

one_c = pygame.image.load('clovers/1c.png')
two_c = pygame.image.load('clovers/2c.png')
three_c = pygame.image.load('clovers/3c.png')
four_c = pygame.image.load('clovers/4c.png')
five_c = pygame.image.load('clovers/5c.png')
six_c = pygame.image.load('clovers/6c.png')
seven_c = pygame.image.load('clovers/7c.png')
eight_c = pygame.image.load('clovers/8c.png')
nine_c = pygame.image.load('clovers/9c.png')
ten_c = pygame.image.load('clovers/10c.png')
jack_c = pygame.image.load('clovers/jc.png')
queen_c = pygame.image.load('clovers/qc.png')
king_c = pygame.image.load('clovers/kc.png')

card_images = [
    [one_h, two_h, three_h, four_h, five_h, six_h, seven_h, eight_h, nine_h, ten_h, jack_h, queen_h, king_h],
    [one_d, two_d, three_d, four_d, five_d, six_d, seven_d, eight_d, nine_d, ten_d, jack_h, queen_d, king_d],
    [one_s, two_s, three_s, four_s, five_s, six_s, seven_s, eight_s, nine_s, ten_s, jack_s, queen_s, king_s],
    [one_c, two_c, three_c, four_c, five_c, six_c, seven_c, eight_c, nine_c, ten_c, jack_c, queen_c, king_c]
]


background_color = (100,120,120)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egyptian Rat Screw")
screen.fill(background_color)

numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shapes = ['Heart', 'Diamond', 'Spade', 'Clovers']


attack_numbers = {'J':1, 'Q':2, 'K':3, 'A':4}

class Card:
    number = ''
    shape = ''
    is_attack_card = False
    image = ''
    
    def __init__(self, number, shape, is_attack_card, image):
        self.number = number
        self.shape = shape
        self.is_attack_card = is_attack_card
        self.image = image
        


        
        
deck = []
for s in range(len(shapes)):
    for n in range(len(numbers)):
        is_attack_card = False
        if numbers[n] in attack_numbers:
            is_attack_card = True
        else:
            is_attack_card = False
        deck.append(Card(numbers[n], shapes[s], is_attack_card, card_images[s][n]))
random.shuffle(deck)

    

player1_deck = []
player2_deck = []
player3_deck = []
player4_deck = []
        
        
def distribute():
    i = 0
    global player1_deck
    global player2_deck
    global player3_deck
    global player4_deck
    
    while i < len(deck):
        player1_deck.append(deck[i])
        player2_deck.append(deck[i+1])
        player3_deck.append(deck[i+2])
        player4_deck.append(deck[i+3])
        i += 4
        
distribute()
    
    
                
class Player:
    name = ''
    deck = []
    
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
                
    
player1 = Player("User", player1_deck)
player2 = Player("Andre Farinazo", player2_deck)
player3 = Player("Luke Wingert", player3_deck)
player4 = Player("Shay Jin", player4_deck)
    
players = [player1, player2, player3, player4]

turn = 1

table = []

def status():
    print("1:")
    for x in player1_deck:
        print(x.number, x.shape)
    
    print("2:")
    for x in player2_deck:
        print(x.number, x.shape)
    print("3:")
    for x in player3_deck:
        print(x.number, x.shape)
    print("4:")
    for x in player4_deck:
        print(x.number, x.shape)
    
font = pygame.font.Font('freesansbold.ttf',15)
def display_turn(card):
    global screen
    global font
    text = font.render("Player " + str(turn), True, (128,0,0), (0,0,128))
    screen.blit(text, (0,200))
    screen.blit(card.image, (0, 0))
    pygame.display.update()
    
def player_turn(turn, next_or_prev):
    if next_or_prev == 'prev':
        turn -= 1
                        
        if turn == 0:
            turn = 4
            
        return turn
    elif next_or_prev == 'next':
        turn += 1
        
        if turn == 5:
            turn = 1
        return turn
    
    return 0
        
def lost_round_msg(turn):
    global font
    text = font.render("Player " + str(turn) + " lost the round", True, (128,0,0), (0,0,128))
    screen.blit(text, (100,100))
    text = font.render('Player ' + str(turn) + '\'s Turn', True, (128,0,0), (0,0,128))
    screen.blit(text, (100,200))
    pygame.display.update()

def draw(player):
    global table
    card_drawn = player.deck.pop()
    table.append(card_drawn)
    return card_drawn
    
def whose_card(turn):
    global font
    text = font.render("Player " + str(turn), True, (128,0,0), (0,0,128))
    screen.blit(text, (0,200))
    
def take_turn(player):
    global turn
    global table
    
    if len(player.deck) > 0:
        if len(table) > 0:
            if table[len(table)-1].is_attack_card:
                time.sleep(0.5)
                card_drawn = draw(player)
                chances = attack_numbers[table[len(table)-2].number]
                
                if not card_drawn.is_attack_card:
                    chances -= 1
                
                display_turn(card_drawn)
                pygame.display.update()      
                             
                while not card_drawn.is_attack_card and len(player.deck) > 0 and chances != 0:
                    time.sleep(1)
                    card_drawn = draw(player)
                    display_turn(card_drawn)
                    chances -= 1
                    
                if not card_drawn.is_attack_card:
                    turn = player_turn(turn, 'prev')
                        
                    for card in table:
                        players[turn-1].deck.append(card)
            
                    lost_round_msg(turn)
                    time.sleep(1)
                    screen.fill(background_color)
                    pygame.display.update()
  
                elif len(player.deck) <= 0:
                    print(str(turn) + " ran out of cards!")
                else:
                    turn = player_turn(turn, 'next')
            else:
                card_drawn = draw(player)
                whose_card(turn)
                screen.blit(card_drawn.image, (0, 0))
                turn = player_turn(turn, 'next')
        else:
            card_drawn = draw(player)
            whose_card(turn)
            screen.blit(card_drawn.image, (0, 0))
            turn = player_turn(turn, 'next')
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(turn)
            if turn == 1:
                take_turn(player1)
            if turn == 2:
                take_turn(player2)
                        
            if turn == 3: 

                take_turn(player3)
            if turn == 4:     
               
                take_turn(player4)
        if turn == 2:
            take_turn(player2)
                        
        if turn == 3: 
            take_turn(player3)
        if turn == 4:     
            take_turn(player4)
        
    pygame.display.update()