import pygame
import random
import math
from pygame import mixer

pygame.init()

#display screen window
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('farm.png')
backgroundImg = pygame.transform.scale(background, (800, 600))

#add icon and caption
pygame.display.set_caption('Adventure game part-1')
icon = pygame.image.load('healthy-food.png')
pygame.display.set_icon(icon)

#player
player = pygame.image.load('boy.png')
playerImg = pygame.transform.scale(player, (75, 75))
playerX = 346
playerY = 520
playerX_change = 0

#fruits
fruitImg = []
fruitX = []
fruitY = []
fruitX_change = []
fruitY_change = []
num_of_fruits = 1

#banana
bananaImg =[]
bananaX = []
bananaY = []
bananaY_change = []
num_of_banana = 2

for i in range(num_of_banana):
    bananaImg.append(pygame.image.load('banana.png'))
    bananaX.append(random.randint(0, 735))
    bananaY.append(random.randint(0, 150))
    bananaY_change.append(0.8)

#music
mixer.music.load('background_music.wav')
mixer.music.play(-1)

for i in range(num_of_fruits):
    fruitImg.append(pygame.image.load('apple.png'))
    fruitX.append(random.randint(0, 735))
    fruitY.append(random.randint(0, 250))
    fruitX_change.append(0)#4
    fruitY_change.append(1)

#score text
score_value = 0
font = pygame.font.Font('font.ttf', 32)
textX = 10
textY = 10



#game over text
game_over_font = pygame.font.Font('font.ttf', 80)

def game_over():
    game_over_font = font.render("GAME OVER", True, (0,0,0))
    screen.blit(game_over_font, (250,250))

#score function
def show_score(x,y):
    score = font.render("score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

#player func
def player(x, y):
    screen.blit(playerImg, (x, y))
#fruit func
def fruit(x, y,i):
    screen.blit(fruitImg[i], (x, y))

def banana(x,y,i):
    screen.blit(bananaImg[i], (x, y))

#collision
def is_collision(playerX, fruitX, playerY, fruitY):
    distance = math.sqrt((math.pow(playerX - fruitX, 2)) + (math.pow(playerY - fruitY, 2)))
    if distance <50:
        return True
    else:
        return False

def is_collision_banana(playerX, bananaX, playerY, bananaY):
    distance = math.sqrt((math.pow(playerX - bananaX, 2)) + (math.pow(playerY - bananaY, 2)))
    if distance <50:
        return True
    else:
        return False

running = True
# loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    #fruit movement
    for i in range(num_of_fruits):

        #game over
        fruitY[i] += fruitY_change[i]
        bananaY[i] += bananaY_change[i]
        if fruitY[i] > 568 or bananaY[i] > 568:
            for j in range(num_of_fruits):
                fruitY[j] = 2000
                bananaY[j] = 2000
            game_over()
            break


        #if fruitX[i] <= 0:
         #   fruitX_change[i] = 0
          #  fruitY[i] += fruitY_change[i]
        #elif fruitX[i] >= 735:
         #   fruitX_change[i] = 0
          #  fruitY[i] += fruitY_change[i]

        collision = is_collision(playerX, fruitX[i], playerY, fruitY[i])
        if collision:
            crunch_sound = mixer.Sound('apple_crunch.wav')
            crunch_sound.play()
            fruitX[i] = random.randint(0, 735)
            fruitY[i] = random.randint(50, 150)
            score_value += 1
        fruit(fruitX[i], fruitY[i], i)


        collision_banana = is_collision_banana(playerX, bananaX[i], playerY, bananaY[i])
        if collision_banana:
            bananaX[i] = random.randint(0, 735)
            bananaY[i] = random.randint(0, 50)
            score_value += 1
        banana(bananaX[i], bananaY[i], i)

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()