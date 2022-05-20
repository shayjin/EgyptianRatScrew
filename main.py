
import pygame
import sys
import random
import time

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

pygame.mixer.init()
set_sound = pygame.mixer.Sound('set.mp3')
slap_sound = pygame.mixer.Sound('slap.mp3')

background_color = (100,120,120)
WIDTH = 700
HEIGHT = 700
offset = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egyptian Rat Screw")
screen.fill(background_color)
font = pygame.font.Font('freesansbold.ttf',15)

numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shapes = ['Heart', 'Diamond', 'Spade', 'Clovers']
attack_numbers = {'J':1, 'Q':2, 'K':3, 'A':4}

can_slap = False



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
   

def initialize(deck):
    for s in range(len(shapes)):
        for n in range(len(numbers)):
            is_attack_card = False
            if numbers[n] in attack_numbers:
                is_attack_card = True
            else:
                is_attack_card = False
            deck.append(Card(numbers[n], shapes[s], is_attack_card, card_images[s][n]))
    return deck

deck = []
deck = initialize(deck)
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
player2 = Player("Luke W", player2_deck)
player3 = Player("Andre F", player3_deck)
player4 = Player("Shay J", player4_deck)
    
players = [player1, player2, player3, player4]

USER_WIDTH = WIDTH / 7
USER_HEIGHT = HEIGHT / 7
user = pygame.image.load('user.jpeg')
user = pygame.transform.scale(user, (USER_WIDTH, USER_HEIGHT)) 
table_img = pygame.image.load('table.jpeg')
turn = 1

def init():
    global screen
    global table
    global user
    global turn
    screen.blit(table_img, (WIDTH/2 - table_img.get_width()/2, HEIGHT/2 - table_img.get_height()/2))

    screen.blit(user, (WIDTH/2-user.get_width()/2, HEIGHT-user.get_height()))
    screen.blit(user, (WIDTH-user.get_width(), HEIGHT/2-user.get_height()/2))
    screen.blit(user, (WIDTH/2-user.get_width()/2, 0))
    screen.blit(user, (0, HEIGHT/2-user.get_height()/2))    

    pygame.draw.circle(screen, (240,240,240),(WIDTH/2,HEIGHT), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(WIDTH,HEIGHT/2), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(WIDTH/2,0), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(0,HEIGHT/2), 150, 10)
    if turn == 1:
        pygame.draw.circle(screen, (215,185,230),(WIDTH/2,HEIGHT), 150, 10)
    elif turn == 2:
        pygame.draw.circle(screen, (215,185,230),(WIDTH,HEIGHT/2), 150, 10)
    elif turn == 3:
        pygame.draw.circle(screen, (215,185,230),(WIDTH/2,0), 150, 10)
    elif turn == 4:
        pygame.draw.circle(screen, (215,185,230),(0,HEIGHT/2), 150, 10) 
        
    text = font.render(str(len(player1.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (WIDTH/2-30,HEIGHT-15))
    text = font.render(str(len(player2.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (WIDTH-80,HEIGHT/2+50))
    text = font.render(str(len(player3.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (WIDTH/2-30,USER_HEIGHT))
    text = font.render(str(len(player4.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (20,HEIGHT/2+50))
    
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(WIDTH/2-35,HEIGHT-HEIGHT/3.5,70, 40),5)
    text = font.render("Deal", True, (0,0,0), background_color)
    screen.blit(text,(WIDTH/2-17, HEIGHT/1.36))
    
    
    

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
    

def display_turn(card):
    global screen
    global font
    if turn == 5:
        text = font.render("Player " + str(1), True, (128,0,0), (0,0,128))
    else:
        text = font.render("Player " + str(turn), True, (128,0,0), (0,0,128))
    screen.blit(text, (0,200))
    screen.blit(card.image, (WIDTH/4+offset, HEIGHT/3+WIDTH/8))
    set_sound.play()
    pygame.display.update()  
    time.sleep(0.8)
    
def player_turn(turn, next_or_prev):
    global offset
    pygame.draw.circle(screen, (240,240,240),(WIDTH/2,HEIGHT), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(WIDTH,HEIGHT/2), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(WIDTH/2,0), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(0,HEIGHT/2), 150, 10)
    if next_or_prev == 'prev':
        turn -= 1
                        
        if turn == 0:
            turn = 4
            
        if len(players[turn-1].deck) == 0:
            print("player " + str(turn) + " ran out of cards!")
            turn = player_turn(turn, 'prev')
    elif next_or_prev == 'next':
        
        print(turn)
        if len(players[turn-1].deck) == 0:
            print("player " + str(turn) + " ran out of cards!")
            turn = player_turn(turn, 'next')
        turn += 1
        if turn == 5:
            turn = 1

        if turn == 1:
            pygame.draw.circle(screen, (215,185,230),(WIDTH/2,HEIGHT), 150, 10)
        elif turn == 2:
            pygame.draw.circle(screen, (215,185,230),(WIDTH,HEIGHT/2), 150, 10)
        elif turn == 3:
            pygame.draw.circle(screen, (215,185,230),(WIDTH/2,0), 150, 10)
        elif turn == 4:
            pygame.draw.circle(screen, (215,185,230),(0,HEIGHT/2), 150, 10)
            
    return turn
    
        
def lost_round_msg(turn):
    global offset
    global font
    text = font.render("Player " + str(turn) + " won the round", True, (0,0,0), background_color)
    screen.blit(text, (WIDTH/2-WIDTH/7, 200))
    offset = 0
    for i in range(10):
        if turn == 1:
            time.sleep(0.05)
            pygame.draw.circle(screen, (240,240,240),(WIDTH/2,HEIGHT), 150, 10)
            pygame.display.update()
            time.sleep(0.05)
            pygame.draw.circle(screen, (134,50,20),(WIDTH/2,HEIGHT), 150, 10)
            pygame.display.update() 
        if turn == 2:
            time.sleep(0.05)
            pygame.draw.circle(screen, (240,240,240),(WIDTH,HEIGHT/2), 150, 10)
            pygame.display.update()
            time.sleep(0.05)
            pygame.draw.circle(screen, (134,50,20),(WIDTH,HEIGHT/2), 150, 10)
            pygame.display.update() 
        if turn == 3:
            time.sleep(0.05)
            pygame.draw.circle(screen, (240,240,240),(WIDTH/2,0), 150, 10)
            pygame.display.update()
            time.sleep(0.05)
            pygame.draw.circle(screen, (134,50,20),(WIDTH/2,0), 150, 10)
            pygame.display.update() 
        if turn == 4:
            time.sleep(0.05)
            pygame.draw.circle(screen, (240,240,240),(0,HEIGHT/2), 150, 10)
            pygame.display.update()
            time.sleep(0.05)
            pygame.draw.circle(screen, (134,50,20),(0,HEIGHT/2), 150, 10)
            pygame.display.update()    
    time.sleep(1.5)
    print('player 1: ' + str(len(player1.deck)))
    print('player 2: ' + str(len(player2.deck)))
    print('player 3: ' + str(len(player3.deck)))
    print('player 4: ' + str(len(player4.deck)))

def slap_lost_round_msg(turn):
    global font
    global offset 
    offset = 0
    text = font.render("Player " + str(turn) + " takes all the card", True, (0,0,0), background_color)
    screen.blit(text, (WIDTH/2-WIDTH/7, 200))
    pygame.display.update()
    print('player 1: ' + str(len(player1.deck)))
    print('player 2: ' + str(len(player2.deck)))
    print('player 3: ' + str(len(player3.deck)))
    print('player 4: ' + str(len(player4.deck)))

slap = False

def draw(player):
    global offset
    global table
    global slap
    global turn
    global can_slap
    can_slap = True
    card_drawn = player.deck.pop()
    table.append(card_drawn)
    offset += 15
    if is_slap(table):
        for card in table:
            print(card.number, card.shape)
        print('SLAP!!!')
        slap = True
        turn = 5
        
    text = font.render(str(len(player1.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (WIDTH/2-30,HEIGHT-15))
    text = font.render(str(len(player2.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (WIDTH-80,HEIGHT/2+50))
    text = font.render(str(len(player3.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (WIDTH/2-30,USER_HEIGHT))
    text = font.render(str(len(player4.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (20,HEIGHT/2+50))
    time.sleep(0.1)
    return card_drawn
    
def whose_card(turn):
    global font
    text = font.render("Player " + str(turn), True, (128,0,0), (0,0,128))
    screen.blit(text, (0,200))

def reset():
    global screen
    global table
    table = []
    time.sleep(1)
    screen.fill(background_color)
    init()
    pygame.display.update()

player1_chances = 0

def player1_defense():
    global player1_chances
    global turn
    global table
    global offset
    if len(player1.deck) > 0:
        if is_slap(table):
            turn = 5
        else:
            card_drawn = draw(player1)
            screen.blit(card_drawn.image, (WIDTH/2-WIDTH/4 + offset, HEIGHT/3+WIDTH/8))
            pygame.display.update()
            if is_slap(table):
                turn = 5
            else:
                if (not card_drawn.is_attack_card) and player1_chances > 0:
                    display_turn(card_drawn)
                    player1_chances -= 1
                    turn = 0
                    if player1_chances == 0:
                        for card in table:
                            players[3].deck.append(card)
                        lost_round_msg(4)
                        reset()
                        turn = 4
                elif player1_chances > 0:
                    display_turn(card_drawn)
                    turn = 2
                else: 
                    turn = player_turn(turn, 'prev')
                            
                    for card in table:
                        players[turn-1].deck.append(card)
            
                    lost_round_msg(turn)
                    reset()
            
def is_slap(table):
    if len(table) == 2:
        if table[0].number == table[1].number:
            return True
        if table[0].number == 'Q' and table[1] == 'K':
            return True
        if table[0].number == 'K' and table[1] == 'Q':
            return True
    elif len(table) > 2:
        if table[len(table)-1].number == table[len(table)-2].number:
            return True
        if table[len(table)-1].number == table[len(table)-3].number:
            return True
        if table[len(table)-1].number == 'Q' and table[len(table)-2] == 'K':
            return True
        if table[len(table)-1].number == 'K' and table[len(table)-2] == 'Q':
            return True
    return False
x = 0 
def should_slap(player):
    global turn
    global table
    global slap
    print('slap?')
    time.sleep(0.1)
    global x
    if x == 10:
        for card in table:
            players[1].deck.append(card)
        table = []
        slap_sound.play()
        print('LUKE took all the cards')
        turn = 2
        slap = False
        slap_lost_round_msg(turn)
        for i in range(10):
            time.sleep(0.05)
            pygame.draw.circle(screen, (240,240,240),(WIDTH,HEIGHT/2), 150, 10)
            pygame.display.update()
            time.sleep(0.05)
            pygame.draw.circle(screen, (134,50,20),(WIDTH,HEIGHT/2), 150, 10)
            pygame.display.update()
        reset()
        x = 0
        return 0
    for event in pygame.event.get():
        print("first")
        if event.type == pygame.MOUSEBUTTONDOWN:
            for card in table:
                players[0].deck.append(card)
            table = []
            slap_sound.play()
            print('yoooo')
            turn = 1
            slap = False
            slap_lost_round_msg(turn)
            reset()
            x = 0
            return 0
            
    
def take_turn(player):
    global turn
    global table
    global player1_chances
    global offset
    global slap
    global can_slap
    
    if len(player.deck) > 0:
        if len(table) > 0:
            if table[len(table)-1].is_attack_card and player == player1:
                player1_chances = attack_numbers[table[len(table)-1].number]
                player1_defense()
            elif table[len(table)-1].is_attack_card:
                card_drawn = draw(player)
                if not slap:
                    chances = attack_numbers[table[len(table)-2].number]
                    
                    if not card_drawn.is_attack_card:
                        chances -= 1
                    
                    display_turn(card_drawn)     
                                
                    while not card_drawn.is_attack_card and len(player.deck) > 0 and chances > 0:
                        card_drawn = draw(player)
                        display_turn(card_drawn)
                        chances -= 1
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pygame.mouse.get_pos()[0] > 205 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 270 and pygame.mouse.get_pos()[1] < 435 and can_slap:
                                    print('?')
                                    slap_sound.play()
                                    slap_at_wrong_time()
                                    can_slap = False
                        
                    if not card_drawn.is_attack_card and not slap:
                        turn = player_turn(turn, 'prev')
                            
                        for card in table:
                            players[turn-1].deck.append(card)
                
                        lost_round_msg(turn)
                        reset()
    
                    elif len(player.deck) <= 0:
                        print(str(turn) + " ran out of cards!")
                        if slap:
                            turn = 5
                        else:
                            turn = player_turn(turn, 'next')
                    elif slap:
                        turn =5
                    else:
                        turn = player_turn(turn, 'next')
                else: 
                    display_turn(card_drawn)
                    turn = 5
            else:
                card_drawn = draw(player)
                whose_card(turn)
                display_turn(card_drawn)
                if slap:
                    turn = 5
                else:
                    turn = player_turn(turn, 'next')
        else:
            card_drawn = draw(player)
            whose_card(turn)
            display_turn(card_drawn)
            turn = player_turn(turn, 'next')
    pygame.display.update()

def slap_at_wrong_time():
    global text
    player1.deck.pop()
    slap_sound.play()
    text = font.render(str(len(player1.deck)) + " cards", True, (128,0,0), (100,120,128))
    screen.blit(text, (WIDTH/2-30,HEIGHT-15))
    text = font.render("-1 card for slapping at a wrong time", True, (128,0,0), (100,120,128))
    screen.blit(text, (WIDTH/2-WIDTH/5, HEIGHT-HEIGHT/3))
    pygame.display.update()
    time.sleep(2)
    pygame.draw.rect(screen, (100,120,128), pygame.Rect(WIDTH/2-WIDTH/4,HEIGHT-HEIGHT/3,300, 30),40)
    pygame.display.update()
    

init()

while True:
    if turn > 1:
        if slap:
            should_slap(player1)
            x += 1
        else: 
            print(can_slap)
            take_turn(players[turn-1])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] > 205 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 270 and pygame.mouse.get_pos()[1] < 435 and can_slap:
                        print('?')
                        slap_sound.play()
                        slap_at_wrong_time()
                        can_slap = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            # WIDTH/2-35,HEIGHT-HEIGHT/3.5,70, 40
            if pygame.mouse.get_pos()[0] > 320 and pygame.mouse.get_pos()[0] < 360 and pygame.mouse.get_pos()[1] > 510 and pygame.mouse.get_pos()[1] < 550:
                if turn == 0:
                    player1_defense()
                if turn == 1:
                    take_turn(player1)
            elif pygame.mouse.get_pos()[0] > 205 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 270 and pygame.mouse.get_pos()[1] < 435 and can_slap:
                print('?')
                slap_sound.play()
                slap_at_wrong_time()
                can_slap = False
    pygame.display.update()