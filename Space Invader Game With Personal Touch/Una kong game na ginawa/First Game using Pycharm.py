from symtable import Class

import pygame
import random
import math

from pygame import mixer
import sys

# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode((800,600))


#Background Sound
mixer.music.load("2021-08-16_-_8_Bit_Adventure_-_www.FesliyanStudios.com.mp3")
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("My First Game!")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load("Enemy.png"))
    enemyX.append(random.randint (0, 725))
    enemyY.append(random.randint (50, 150))
    enemyX_change.append(random.uniform(0.2, 0.5))
    enemyY_change.append(20)

# Bullet
# Ready = Bullet in spaceship
# Fire = Moving
bulletImg = pygame.image.load("bullet (1).png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "Ready"


#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

#Game Over function
game_over_font = pygame.font.Font('freesansbold.ttf',64)
def show_score (x,y):
    score = font.render("Score: " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = game_over_font.render("Game Over!" + str(score_value), True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y, i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg, (x+16, y +10))

def isCollision(enemyX,bulletX,enemyY,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False





#Para sa game menu


menu_background = pygame.image.load("preview-1.jpg")





def start_menu():
    running = True
    font = pygame.font.Font('freesansbold.ttf',32)

    #Button Sound Effects
    hover_sound = pygame.mixer.Sound("Video-Game-Positive-Sound-A1-8bit-www.fesliyanstudios.com.mp3")
    click_sound = pygame.mixer.Sound("Video-Game-Positive-Sound-A2-8bit-www.fesliyanstudios.com.mp3")

    hovered_button = None
    clicked_button = None

    class Button:
        def __init__(self, x, y, width, height, text):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text

        def draw(self):
            pygame.draw.rect(screen, (170, 170, 170), self.rect)
            text_surface = font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surface, (self.rect.x + 20, self.rect.y + 10))

        def is_clicked(self, pos):  # Fixed typo here
            return self.rect.collidepoint(pos)

    # Define Buttons
    start_button = Button(300, 250, 200, 50, "Start Game")
    settings_button = Button(300, 320, 200, 50, "Settings")
    quit_button = Button(300, 390, 200, 50, "Quit")

    while running:
        screen.blit(menu_background, (0,0))  # Background color (To be replaced with menu_background)
        title = font.render("My First Game!", True, (255, 255, 255))
        start_text = font.render("Press SPACE to Start", True, (255, 255, 255))

        screen.blit(title, (250, 150))  # Adjusted placement for better UI
        start_button.draw()
        settings_button.draw()
        quit_button.draw()

        pygame.display.update()  # Move inside the loop for proper updates

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                for button in [start_button, settings_button, quit_button]:
                    if button.rect.collidepoint(event.pos):
                        if hovered_button != button:
                            hover_sound.play()
                            hovered_button = button
                        break
                else:
                    hovered_button = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in [start_button, settings_button, quit_button]:
                    if button.rect.collidepoint(event.pos):
                        if clicked_button != button:
                            click_sound.play()  # ← ayos na ‘to
                            clicked_button = button
                        break
                else:
                    clicked_button = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(event.pos):  # Fixed method call
                    running = False  # Proceed to game loop
                if settings_button.is_clicked(event.pos):
                    print("Settings clicked")
                if quit_button.is_clicked(event.pos):
                    running = False
                    pygame.quit()
                    sys.exit()

# Wala munang music
mixer.music.stop()

# Tawagin ito bago ang game loop
start_menu()

#Background Music pagkatapos ng menu
mixer.music.load("2021-08-16_-_8_Bit_Adventure_-_www.FesliyanStudios.com.mp3")
mixer.music.play()



# Game Background
game_background = pygame.image.load("planet_ring_purple_149425_800x600.jpg")
# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 255, 255))

    # Background Image
    screen.blit(game_background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "Ready":
                 bullet_Sound = mixer.Sound('ytmp3free.cc_8-bit-laser-sound-effect-youtubemp3free.org.wav')
                 bullet_Sound.play()
                 bulletX = playerX
                 bullet_state = "Fire"
                 fire_bullet(bulletX,bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0



    # 5 = 5 - 0.1
    # 5 = 5 + 0.1
    #Boundaries of spaceship and enemy
    playerX += playerX_change
    if playerX <=0:
        playerX= 0
    elif playerX >=768:
        playerX= 768

    #Enemy Movement
    for i in range(num_of_enemies):

        #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change [i]
        if enemyX [i] <= 0:
            enemyX_change [i] = 0.2
            enemyY [i] += enemyY_change [i]
        elif enemyX [i] >= 725:
           enemyX_change [i]  = -0.2
           enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], bulletX, enemyY[i], bulletY)
        if collision:
            explosion_Sound = mixer.Sound('boom4.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "Ready"
            score_value += 1
            enemyX[i] = random.randint(0, 725)
            enemyY[i] = random.randint(0, 150)


        enemy(enemyX[i], enemyY[i], i)





    #Bullet Movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "Ready"

    if bullet_state == "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change







    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()