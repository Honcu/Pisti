import pygame
import sys
import os
import time
import players


def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

print(os.path)

screen_sizex = 1300
screen_sizey = 900

white = (255, 255, 255)
bg_green = (40, 80, 40)
bg_color = bg_green

pygame.init()
cardBack = pygame.image.load(resource_path('png/cardBack.png'))
screen = pygame.display.set_mode((screen_sizex, screen_sizey))
pygame.display.set_caption('PİŞTİ')
myfont = pygame.font.SysFont('monospace', 70)
smallFont = pygame.font.SysFont('monospace', 30)
screen.fill(bg_color)
clock = pygame.time.Clock()
pygame.display.flip()

cardImg = [None]
# Load 52 Images
two_clubs = pygame.image.load(resource_path('png/2_of_clubs.png'))
two_diamonds = pygame.image.load(resource_path('png/2_of_diamonds.png'))
two_hearts = pygame.image.load(resource_path('png/2_of_hearts.png'))
two_spades = pygame.image.load(resource_path('png/2_of_spades.png'))

three_clubs = pygame.image.load(resource_path('png/3_of_clubs.png'))
three_spades = pygame.image.load(resource_path('png/3_of_spades.png'))
three_diamonds = pygame.image.load(resource_path('png/3_of_diamonds.png'))
three_hearts = pygame.image.load(resource_path('png/3_of_hearts.png'))

four_clubs = pygame.image.load(resource_path('png/4_of_clubs.png'))
four_spades = pygame.image.load(resource_path('png/4_of_spades.png'))
four_diamonds = pygame.image.load(resource_path('png/4_of_diamonds.png'))
four_hearts = pygame.image.load(resource_path('png/4_of_hearts.png'))

five_clubs = pygame.image.load(resource_path('png/5_of_clubs.png'))
five_spades = pygame.image.load(resource_path('png/5_of_spades.png'))
five_diamonds = pygame.image.load(resource_path('png/5_of_diamonds.png'))
five_hearts = pygame.image.load(resource_path('png/5_of_hearts.png'))

six_clubs = pygame.image.load(resource_path('png/6_of_clubs.png'))
six_spades = pygame.image.load(resource_path('png/6_of_spades.png'))
six_diamonds = pygame.image.load(resource_path('png/6_of_diamonds.png'))
six_hearts = pygame.image.load(resource_path('png/6_of_hearts.png'))

seven_clubs = pygame.image.load(resource_path('png/7_of_clubs.png'))
seven_spades = pygame.image.load(resource_path('png/7_of_spades.png'))
seven_diamonds = pygame.image.load(resource_path('png/7_of_diamonds.png'))
seven_hearts = pygame.image.load(resource_path('png/7_of_hearts.png'))

eight_clubs = pygame.image.load(resource_path('png/8_of_clubs.png'))
eight_spades = pygame.image.load(resource_path('png/8_of_spades.png'))
eight_diamonds = pygame.image.load(resource_path('png/8_of_diamonds.png'))
eight_hearts = pygame.image.load(resource_path('png/8_of_hearts.png'))

nine_clubs = pygame.image.load(resource_path('png/9_of_clubs.png'))
nine_spades = pygame.image.load(resource_path('png/9_of_spades.png'))
nine_diamonds = pygame.image.load(resource_path('png/9_of_diamonds.png'))
nine_hearts = pygame.image.load(resource_path('png/9_of_hearts.png'))

ten_clubs = pygame.image.load(resource_path('png/10_of_clubs.png'))
ten_spades = pygame.image.load(resource_path('png/10_of_diamonds.png'))
ten_diamonds = pygame.image.load(resource_path('png/10_of_hearts.png'))
ten_hearts = pygame.image.load(resource_path('png/10_of_spades.png'))

jack_clubs = pygame.image.load(resource_path('png/jack_of_clubs.png'))
jack_spades = pygame.image.load(resource_path('png/jack_of_spades.png'))
jack_diamonds = pygame.image.load(resource_path('png/jack_of_diamonds.png'))
jack_hearts = pygame.image.load(resource_path('png/jack_of_hearts.png'))

queen_clubs = pygame.image.load(resource_path('png/queen_of_clubs.png'))
queen_spades = pygame.image.load(resource_path('png/queen_of_spades.png'))
queen_diamonds = pygame.image.load(resource_path('png/queen_of_diamonds.png'))
queen_hearts = pygame.image.load(resource_path('png/queen_of_hearts.png'))

king_clubs = pygame.image.load(resource_path('png/king_of_clubs.png'))
king_spades = pygame.image.load(resource_path('png/king_of_spades.png'))
king_diamonds = pygame.image.load(resource_path('png/king_of_diamonds.png'))
king_hearts = pygame.image.load(resource_path('png/king_of_hearts.png'))

ace_clubs = pygame.image.load(resource_path('png/ace_of_clubs.png'))
ace_spades = pygame.image.load(resource_path('png/ace_of_spades.png'))
ace_diamonds = pygame.image.load(resource_path('png/ace_of_diamonds.png'))
ace_hearts = pygame.image.load(resource_path('png/ace_of_hearts.png'))


cardImg.append([ace_clubs, ace_diamonds, ace_hearts, ace_spades])
cardImg.append([two_clubs, two_diamonds, two_hearts, two_spades])
cardImg.append([three_clubs, three_diamonds, three_hearts, three_spades])
cardImg.append([four_clubs, four_diamonds, four_hearts, four_spades])
cardImg.append([five_clubs, five_diamonds, five_hearts, five_spades])
cardImg.append([six_clubs, six_diamonds, six_hearts, six_spades])
cardImg.append([seven_clubs, seven_diamonds, seven_hearts, seven_spades])
cardImg.append([eight_clubs, eight_diamonds, eight_hearts, eight_spades])
cardImg.append([nine_clubs, nine_diamonds, nine_hearts, nine_spades])
cardImg.append([ten_clubs, ten_diamonds, ten_hearts, ten_spades])
cardImg.append([jack_clubs, jack_diamonds, jack_hearts, jack_spades])
cardImg.append([queen_clubs, queen_diamonds, queen_hearts, queen_spades])
cardImg.append([king_clubs, king_diamonds, king_hearts, king_spades])

# keeps user hand card positions
user_hand_card_pos = []
xpos = screen_sizex * 0.282
for i in range(0, 4):
    user_hand_card_pos.append([xpos, screen_sizey / 45 * 35])
    xpos += screen_sizex * 0.112


# draws card on screen
def draw_card(img, x, y):
    w = screen_sizex / 10
    h = screen_sizey / 5
    pygame.draw.rect(screen, white, (x - 5, y - 4, w + 10, h + 8), 0)
    new_image = pygame.transform.scale(img, (w, h))
    screen.blit(new_image, (x, y))


def card_image(n, suit):
    if suit == 'clubs':
        return cardImg[n][0]
    elif suit == 'diamonds':
        return cardImg[n][1]
    elif suit == 'hearts':
        return cardImg[n][2]
    elif suit == 'spades':
        return cardImg[n][3]


def draw_middle3(middle):
    w = screen_sizex / 15
    h = screen_sizey / 15 * 2
    card_xpos = screen_sizex / 20 * 12
    for i in range(0, 3):
        image = card_image(middle[i][0], middle[i][1])
        pygame.draw.rect(screen, white, (card_xpos - 3.33, screen_sizey / 20 * 11 - 2.66, w + 6.66, h + 5.32), 0)
        new_image = pygame.transform.scale(image, (w, h))
        screen.blit(new_image, (card_xpos, screen_sizey / 20 * 11))
        card_xpos = card_xpos + screen_sizex * 0.006 + w + 6.66
    state = smallFont.render("Ortayı aldın. Kapalı 3 kart:", True, white)
    screen.blit(state, (screen_sizex / 20 * 12, screen_sizey / 2))
    pygame.display.update()
    time.sleep(3)
    pygame.draw.rect(screen, bg_color, (screen_sizex / 20 * 12 - 3.33, screen_sizey / 20 * 11 - 2.66, card_xpos - screen_sizex / 20 * 12, h + 5.32), 0)


def collection_value(collection):
    value = 0
    for item in collection:
        if item == [10, "diamonds"]:
            value = value + 3
        elif item == [2, "clubs"]:
            value = value + 2
        elif item[0] == 1 or item[0] == 11:
            value = value + 1
    return value


def first_start():
    title = "--- PİŞTİ ---"
    screen.fill(bg_color)

    label = myfont.render(title, True, white)
    label_pos = label.get_rect()
    label_pos.centerx = screen.get_rect().centerx
    label_pos.centery = screen.get_rect().centery / 9 * 8
    screen.blit(label, label_pos)

    label2 = smallFont.render('Başlamak için SPACE tuşuna bas', True, white)
    label2_pos = label2.get_rect()
    label2_pos.centerx = screen.get_rect().centerx
    label2_pos.centery = screen.get_rect().centery / 9 * 10
    screen.blit(label2, label2_pos)
    pygame.display.update()

    while True:
        clock.tick(60)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            break
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                main()


def main():

    pack = players.Cards()

    # sets initial picked cards as null
    user_pick = []
    # comp_pick = []

    # sets initial scores as zero
    user_score = 0
    comp_score = 0

    # sets initial collected cards as empty
    user_card_col = []
    comp_card_col = []

    # fills middle
    middle = pack.fill4()

    # keeps track of who won the last hand and if first 3 cards collected
    last_hand_user = True
    mid3_closed = True

    # initialize computer
    comp_hand = [[0, "Null"], [0, "Null"], [0, "Null"], [0, "Null"]]
    comp = players.Computer(comp_hand)

    round_count = 1
    while True:
        pygame.display.update()
        screen.fill(bg_color)
        clock.tick(60)

        x1 = screen_sizex / 26 * 21

        while round_count < 7:

            round_label1 = smallFont.render("Round", True, white)
            screen.blit(round_label1, (950, 50))
            round_label2 = smallFont.render(str(round_count), True, white)
            screen.blit(round_label2, (x1, 50))
            x1 += screen_sizex / 130 * 3

            # starts round with dealing cards
            user_hand = pack.fill4()
            comp.set_hand(pack.fill4())

            # draw pack & hands
            if len(pack.get_cards()) > 0:
                draw_card(cardBack, 30, screen_sizey / 5 * 2)

            card_xpos = screen_sizex * 0.282
            for i in range(0, 4):
                if user_hand[i][0] > 0:
                    draw_card(card_image(user_hand[i][0], user_hand[i][1]), card_xpos, screen_sizey / 45 * 35)
                    draw_card(cardBack, card_xpos, screen_sizey / 45)
                else:
                    pygame.draw.rect(screen, bg_color, (card_xpos - 5, screen_sizey / 45 * 35 - 4, screen_sizex / 10 + 10, screen_sizey / 5 + 8))
                card_xpos += screen_sizex * 0.112
                pygame.display.update()

            turn = 1
            comp_card_xpos = screen_sizex * 0.282
            while turn < 5:
                # starts each turn by drawing the top card on middle
                pygame.draw.rect(screen, bg_color, (screen_sizex / 20 * 12, screen_sizey / 2, screen_sizex / 20 * 8, screen_sizey / 10))

                if len(middle) > 1:
                    draw_card(cardBack, screen_sizex / 20 * 9 - 15, screen_sizey / 5 * 2)
                if len(middle) > 0:
                    draw_card(card_image(middle[-1][0], middle[-1][1]), screen_sizex/20*9, screen_sizey/5*2)
                    pygame.display.update()

                # lets user pick a card
                clicked = False
                while not clicked:
                    ev = pygame.event.poll()
                    if ev.type == pygame.QUIT:
                        pygame.quit()
                        break
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        for i in range(0, 4):
                            if user_hand_card_pos[i][0] < mouse_pos[0] < user_hand_card_pos[i][0] + screen_sizey / 10:
                                if user_hand_card_pos[i][1] < mouse_pos[1] < user_hand_card_pos[i][1] + screen_sizey / 5:
                                    if user_hand[i][0] == 0:
                                        pass
                                    else:
                                        draw_card(card_image(user_hand[i][0], user_hand[i][1]), screen_sizex/20*9, screen_sizey/5*2)
                                        user_pick = [user_hand[i][0], user_hand[i][1]]
                                        pygame.draw.rect(screen, bg_color, (user_hand_card_pos[i][0] - 5, screen_sizey / 45 * 35 - 4, screen_sizex / 10 + 10, screen_sizey / 5 + 8))
                                        user_hand[i][0] = 0
                                        pygame.display.update()
                                        time.sleep(0.5)
                                        clicked = True

                if len(middle) == 1 and user_pick[0] == middle[-1][0]:  # user pişti
                    middle.append(user_pick)
                    user_card_col = user_card_col + middle
                    last_hand_user = True
                    middle = []
                    pygame.draw.rect(screen, bg_color, (screen_sizex / 20 * 9 - 20, screen_sizey / 5 * 2 - 4, screen_sizex / 10 + 25, screen_sizey / 5 + 8))
                    user_score = user_score + 10
                    state = smallFont.render("PİŞTİ YAPTIN!", True, white)
                    screen.blit(state, (screen_sizex / 20 * 12, screen_sizey / 2))
                elif len(middle) > 0 and user_pick[0] == 11:  # user valeyle ortayı aldı
                    middle.append(user_pick)
                    user_card_col = user_card_col + middle
                    if mid3_closed:
                        draw_middle3(middle)
                        mid3_closed = False
                    last_hand_user = True
                    middle = []
                    pygame.draw.rect(screen, bg_color, (screen_sizex / 20 * 9 - 20, screen_sizey / 5 * 2 - 4, screen_sizex / 10 + 25, screen_sizey / 5 + 8))
                    state = smallFont.render("Ortayı aldın", True, white)
                    screen.blit(state, (screen_sizex / 20 * 12, screen_sizey / 2))
                elif len(middle) > 0 and user_pick[0] == middle[-1][0]:  # user aynı sayıyla ortayı aldı
                    middle.append(user_pick)
                    user_card_col = user_card_col + middle
                    if mid3_closed:
                        draw_middle3(middle)
                        mid3_closed = False
                    last_hand_user = True
                    middle = []
                    pygame.draw.rect(screen, bg_color, (screen_sizex / 20 * 9 - 20, screen_sizey / 5 * 2 - 4, screen_sizex / 10 + 25, screen_sizey / 5 + 8))
                    state = smallFont.render("Ortayı aldın", True, white)
                    screen.blit(state, (screen_sizex / 20 * 12, screen_sizey / 2))
                else:
                    middle.append(user_pick)

                pygame.display.update()
                time.sleep(0.2)

                # computer picks a card
                comp_pick = comp.decision(middle)

                if len(middle) == 1 and comp_pick[0] == middle[-1][0]:  # comp pişti
                    middle.append(comp_pick)
                    comp_card_col = comp_card_col + middle
                    last_hand_user = False
                    middle = []
                    pygame.draw.rect(screen, bg_color, (screen_sizex / 20 * 9 - 20, screen_sizey / 5 * 2 - 4, screen_sizex / 10 + 25, screen_sizey / 5 + 8))
                    comp_score = comp_score + 10
                    state = smallFont.render("Bilgisayar PİŞTİ yaptı!", True, white)
                    screen.blit(state, (screen_sizex / 20 * 12, screen_sizey / 2))
                elif len(middle) > 0 and comp_pick[0] == 11:  # comp valeyle ortayı aldı
                    middle.append(comp_pick)
                    comp_card_col = comp_card_col + middle
                    mid3_closed = False
                    last_hand_user = False
                    middle = []
                    pygame.draw.rect(screen, bg_color, (screen_sizex / 20 * 9 - 20, screen_sizey / 5 * 2 - 4, screen_sizex / 10 + 25, screen_sizey / 5 + 8))
                    state = smallFont.render("Bilgisayar ortayı aldı", True, white)
                    screen.blit(state, (screen_sizex / 20 * 12, screen_sizey / 2))
                elif len(middle) > 0 and comp_pick[0] == middle[-1][0]:  # comp aynı sayıyla ortayı aldı
                    middle.append(comp_pick)
                    comp_card_col = comp_card_col + middle
                    mid3_closed = False
                    last_hand_user = False
                    middle = []
                    pygame.draw.rect(screen, bg_color, (screen_sizex / 20 * 9 - 20, screen_sizey / 5 * 2 - 4, screen_sizex / 10 + 25, screen_sizey / 5 + 8))
                    state = smallFont.render("Bilgisayar ortayı aldı", True, white)
                    screen.blit(state, (screen_sizex / 20 * 12, screen_sizey / 2))
                else:
                    middle.append(comp_pick)

                pygame.draw.rect(screen, bg_color, (comp_card_xpos - 5, screen_sizey / 45 - 4, screen_sizex / 10 + 10, screen_sizey / 5 + 8))
                comp_card_xpos += screen_sizex * 0.112
                pygame.display.update()
                time.sleep(0.2)

                turn += 1
            round_count += 1
        break

    screen.fill(bg_color)
    pygame.display.update()
    # assigns the last cards on the middle to player who won the last hand
    if last_hand_user:
        user_card_col = user_card_col + middle
    else:
        comp_card_col = comp_card_col + middle

    # adds 3 points to score of player who collected most cards
    if len(user_card_col) > len(comp_card_col):
        user_score = user_score + 3
    elif len(user_card_col) < len(comp_card_col):
        comp_score = comp_score + 3

    # adds card values in collection to scores
    user_score = user_score + collection_value(user_card_col)
    comp_score = comp_score + collection_value(comp_card_col)

    final_string1 = "Senin topladığın kart sayısı: " + str(len(user_card_col))
    final_string2 = "Bilgisayarın topladığı kart sayısı: " + str(len(comp_card_col))
    final_string3 = "Senin puanın: " + str(user_score)
    final_string4 = "Bilgisayarın puanı: " + str(comp_score)
    if user_score > comp_score:
        final_string5 = "Tebrikler! Kazandın!"
    elif user_score < comp_score:
        final_string5 = "Bilgisayar kazandı."
    else:
        final_string5 = "Berabere"
    final_string6 = "Tekrar oynamak için SPACE tuşuna bas"

    f_label1 = smallFont.render(final_string1, True, white)
    f_label1_pos = f_label1.get_rect()
    f_label1_pos.centerx = screen.get_rect().centerx
    f_label1_pos.centery = screen.get_rect().centery / 18 * 4
    screen.blit(f_label1, f_label1_pos)

    f_label2 = smallFont.render(final_string2, True, white)
    f_label2_pos = f_label2.get_rect()
    f_label2_pos.centerx = screen.get_rect().centerx
    f_label2_pos.centery = screen.get_rect().centery / 18 * 6
    screen.blit(f_label2, f_label2_pos)

    f_label3 = smallFont.render(final_string3, True, white)
    f_label3_pos = f_label3.get_rect()
    f_label3_pos.centerx = screen.get_rect().centerx
    f_label3_pos.centery = screen.get_rect().centery / 18 * 9
    screen.blit(f_label3, f_label3_pos)

    f_label4 = smallFont.render(final_string4, True, white)
    f_label4_pos = f_label4.get_rect()
    f_label4_pos.centerx = screen.get_rect().centerx
    f_label4_pos.centery = screen.get_rect().centery / 18 * 11
    screen.blit(f_label4, f_label4_pos)

    f_label5 = myfont.render(final_string5, True, white)
    f_label5_pos = f_label5.get_rect()
    f_label5_pos.centerx = screen.get_rect().centerx
    f_label5_pos.centery = screen.get_rect().centery / 18 * 14
    screen.blit(f_label5, f_label5_pos)

    f_label6 = smallFont.render(final_string6, True, white)
    f_label6_pos = f_label6.get_rect()
    f_label6_pos.centerx = screen.get_rect().centerx
    f_label6_pos.centery = screen.get_rect().centery
    screen.blit(f_label6, f_label6_pos)

    pygame.display.update()


first_start()
