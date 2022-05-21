
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
players_alive = [1, 2, 3, 4]

can_slap = False
slap = False



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
temp = []

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
TABLE_WIDTH = WIDTH / 1.3
TABLE_HEIGHT = HEIGHT / 3
user = pygame.image.load('user.jpeg')
user = pygame.transform.scale(user, (USER_WIDTH, USER_HEIGHT)) 
table_img = pygame.image.load('table.png')
table_img = pygame.transform.scale(table_img, (TABLE_WIDTH, TABLE_HEIGHT))
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

deck1_copy = player1_deck
deck2_copy = player2_deck
deck3_copy = player3_deck
deck4_copy = player4.deck
recent_attack_card = ""
    
    

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
    global slap
    global can_slap
    if turn == 5:
        text = font.render("Player " + str(1), True, (128,0,0), (0,0,128))
    else:
        text = font.render("Player " + str(turn), True, (128,0,0), (0,0,128))
    screen.blit(text, (0,200))
    screen.blit(card.image, (WIDTH/4+offset, HEIGHT/3+WIDTH/8))
    set_sound.play()
    pygame.display.update()  
    if slap:
        should_slap(player1)
    else:
        time.sleep(0.8)
    
def player_turn(turn, next_or_prev):
    global offset
    global players_alive
    pygame.draw.circle(screen, (240,240,240),(WIDTH/2,HEIGHT), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(WIDTH,HEIGHT/2), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(WIDTH/2,0), 150, 10)
    pygame.draw.circle(screen, (240,240,240),(0,HEIGHT/2), 150, 10)
    if next_or_prev == 'prev':
        if len(players[turn-1].deck) == 0:
            print("player " + str(turn) + " ran out of cards!")
        turn -= 1
                        
        if turn == 0:
            turn = 4
        if turn not in players_alive:
            turn = player_turn(turn, "prev")
            
        
        return turn
    elif next_or_prev == 'next':
        
        if len(players[turn-1].deck) == 0:
            print("player " + str(turn) + " ran out of cards!")
        turn += 1
        
        if turn == 5:
            turn = 1
            
        if turn not in players_alive:
            turn = player_turn(turn, "next")

        if turn == 1:
            pygame.draw.circle(screen, (215,185,230),(WIDTH/2,HEIGHT), 150, 10)
        elif turn == 2:
            pygame.draw.circle(screen, (215,185,230),(WIDTH,HEIGHT/2), 150, 10)
        elif turn == 3:
            pygame.draw.circle(screen, (215,185,230),(WIDTH/2,0), 150, 10)
        elif turn == 4:
            pygame.draw.circle(screen, (215,185,230),(0,HEIGHT/2), 150, 10)
            
        return turn
    
        
def lost_round_msg():
    global offset
    global font
    global can_slap
    global players_alive
    global turn
    
    offset = 0
    can_slap = False

    if not turn in players_alive:
        turn = player_turn(turn, "prev")
    text = font.render("Player " + str(turn) + " won the round", True, (0,0,0), background_color)
    screen.blit(text, (WIDTH/2-WIDTH/7, 200))
    
    if len(player1.deck) == 0 and 1 in players_alive:
        players_alive.pop(players_alive.index(1))
        can_slap = False
    if len(player2.deck) == 0 and 2 in players_alive:
        players_alive.pop(players_alive.index(2))
    if len(player3.deck) == 0 and 3 in players_alive:
        players_alive.pop(players_alive.index(3))
    if len(player4.deck) == 0 and 4 in players_alive:
        players_alive.pop(players_alive.index(4))
        
    print(players_alive)
    
    
    for i in range(10):
        
        time.sleep(0.05)
        
        if turn == 1:
            pygame.draw.circle(screen, (240,240,240),(WIDTH/2,HEIGHT), 150, 10)
        if turn == 2:
            pygame.draw.circle(screen, (240,240,240),(WIDTH,HEIGHT/2), 150, 10)
        if turn == 3:
            pygame.draw.circle(screen, (240,240,240),(WIDTH/2,0), 150, 10)
        if turn == 4:
            pygame.draw.circle(screen, (240,240,240),(0,HEIGHT/2), 150, 10)
            
        pygame.display.update()
        time.sleep(0.05)
        
        if turn == 1:
            pygame.draw.circle(screen, (134,50,20),(WIDTH/2,HEIGHT), 150, 10)
        if turn == 2:
            pygame.draw.circle(screen, (134,50,20),(WIDTH,HEIGHT/2), 150, 10)
        if turn == 3:
            pygame.draw.circle(screen, (134,50,20),(WIDTH/2,0), 150, 10)
        if turn == 4:
            pygame.draw.circle(screen, (134,50,20),(0,HEIGHT/2), 150, 10)
            
        pygame.display.update()    
        
    time.sleep(1.5)

def slap_lost_round_msg(turn):
    global font
    global offset 
    
    offset = 0
    text = font.render("Player " + str(turn) + " takes all the card", True, (0,0,0), background_color)
    screen.blit(text, (WIDTH/2-WIDTH/7, 200))
    pygame.display.update()

def draw(player):
    global offset
    global table
    global slap
    global turn
    global can_slap
    if not slap:
        can_slap = True
        offset += 15
            
        card_drawn = player.deck.pop()
        table.append(card_drawn)
        
        if is_slap(table):
            for card in table:
                print(card.number, card.shape)
            print('SLAP!!!')
            slap = True
        
            
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
    global trash_offset
    global trash_deck
    trash_deck = []
    trash_offset = 0
    global temp
    temp = []
    table = []
    time.sleep(1)
    screen.fill(background_color)
    init()
    pygame.display.update()

player1_chances = 0
            
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
    global can_slap
    global trash_deck
    global players_alive
    global trash_deck

    print('slap?')
    time.sleep(0.1)
    global x
    if x == 4:
        can_slap = False
        for card in table:
            players[1].deck.insert(0, card)
        for card in trash_deck:
            players[1].deck.insert(0, card)
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
    if 1 in players_alive:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and slap:
                for card in table:
                    players[0].deck.insert(0, card)
                for card in trash_deck:
                    players[0].deck.insert(0, card)
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
    global temp
    global recent_attack_card
    global players_alive
    if len(player.deck) > 0:
        if len(table) > 0:
            if (table[len(table)-1].is_attack_card and player == player1):
                temp.append(attack_numbers[table[len(table)-1].number])
                turn = 0
                player1_defense()
            elif turn == 0: # defense again
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
                                if pygame.mouse.get_pos()[0] > 205 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 270 and pygame.mouse.get_pos()[1] < 435 and can_slap and not slap and 1 in players_alive:
                                    print('?')
                                    print(1 in players_alive)
                                    slap_sound.play()
                                    slap_at_wrong_time()
                                    can_slap = False
                        
                    if not card_drawn.is_attack_card and not slap:
                        can_slap = False
                        turn = player_turn(turn, 'prev')
                        for card in table:
                            players[turn-1].deck.insert(0, card)
                        for card in trash_deck:
                            players[turn-1].deck.insert(0,card)
                
                        lost_round_msg()
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
                    print(turn)
        else:
            card_drawn = draw(player)
            whose_card(turn)
            display_turn(card_drawn)
            turn = player_turn(turn, 'next')
    pygame.display.update()

trash_offset = 0
trash_deck = []

def slap_at_wrong_time():
    global text
    global trash_offset
    global trash_deck
    global players_alive
    
    if 1 in players_alive:
        trash_card = player1.deck.pop()
        trash_deck.append(trash_card)
        slap_sound.play()
        
        text = font.render(str(len(player1.deck)) + " cards", True, (128,0,0), (100,120,128))
        screen.blit(text, (WIDTH/2-30,HEIGHT-15))
        text = font.render("-1 card for slapping at a wrong time", True, (128,0,0), (100,120,128))
        screen.blit(text, (WIDTH/2-WIDTH/5, HEIGHT-HEIGHT/3))
        screen.blit(trash_card.image, (WIDTH/1.3 + trash_offset, HEIGHT/1.3))
        
        pygame.display.update()
        time.sleep(0.1)
        trash_offset += 15
        pygame.draw.rect(screen, (100,120,128), pygame.Rect(WIDTH/2-WIDTH/4,HEIGHT-HEIGHT/3,300, 30),40)
        pygame.display.update()
    
def player1_defense():
    global player1_chances
    global turn
    global table
    global offset
    global slap
    global can_slap
    global temp
    global trash_deck
    
    if len(player1.deck) > 0:
        card_drawn = draw(player1)
        screen.blit(card_drawn.image, (WIDTH/2-WIDTH/4 + offset, HEIGHT/3+WIDTH/8))
        pygame.display.update()
        if is_slap(table):
               turn = 5
        else:
            if (not card_drawn.is_attack_card) and temp[0] > 0:
                display_turn(card_drawn)
                temp[0] -= 1
                if temp[0] == 0:
                    can_slap = False
                    turn = 1
                    turn = player_turn(turn, 'prev')
                    for card in table:
                        players[3].deck.insert(0, card)
                    for card in trash_deck:
                        players[3].deck.insert(0, card)
                    lost_round_msg()
                    reset()
            elif temp[0] > 0:
                turn = 1
                turn = player_turn(turn, 'next')
                display_turn(card_drawn)
            else: 
                can_slap = False
                turn = 1
                turn = player_turn(turn, 'prev')
                for card in table:
                    players[3].deck.insert(0,card)
                for card in trash_deck:
                    players[3].deck.insert(0,card)
                lost_round_msg()
                reset()

init()

while True:
    if turn > 1 or len(player1.deck) == 0:
        if slap:
            should_slap(player1)
            x += 1
        else: 
            print(len(players[turn-1].deck))
            if len(players[turn-1].deck) > 0:
                print('sup')
                take_turn(players[turn-1])
            else:
                turn = player_turn(turn, 'next')
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # WIDTH/2-35,HEIGHT-HEIGHT/3.5,70, 40
            if len(player1.deck) > 0 and 1 in players_alive:
                if pygame.mouse.get_pos()[0] > 319 and pygame.mouse.get_pos()[0] < 380 and pygame.mouse.get_pos()[1] > 504 and pygame.mouse.get_pos()[1] < 535:
                    if turn == 0:
                        take_turn(player1)
                    if turn == 1:
                        take_turn(player1)
                elif pygame.mouse.get_pos()[0] > 205 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 270 and pygame.mouse.get_pos()[1] < 435 and can_slap and (not slap) and 1 in players_alive:
                    print(1 in players_alive)
                    slap_sound.play()
                    slap_at_wrong_time()
    pygame.display.update()