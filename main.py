import pygame
import random

# Quick game thrown together to work out the fundamentals of pygame

# initialize pygame
pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600

window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])

background = pygame.image.load("images/background.png")

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("images/player.png")

playerX = WIN_WIDTH / 2 - 25
playerY = WIN_HEIGHT / 2 + 180

PLAYER_SPEED = 3


def player(x, y):
    window.blit(playerImg, [x, y])


# Invader
invaderImg = pygame.image.load("images/invader.png")
invaderX = random.randint(0, WIN_WIDTH - 64)
invaderY = random.randint(0, WIN_HEIGHT - 140)

invaderX_change = 1
invaderY_change = 40
INVADER_SPEED = 1


def invader(x, y):
    window.blit(invaderImg, [x, y])


# Missile
missileImg = pygame.image.load("images/keratin_missile.png")
missileY = playerY

missileX_change = 0
missileY_change = 10
MISSILE_STATE = "ready"


def fire_missile(x, y):
    global MISSILE_STATE
    global missileImg
    MISSILE_STATE = "fire"
    missileImg = pygame.transform.rotate(missileImg, 90)
    window.blit(missileImg, [x + 16, y - 25])
    missileImg = pygame.transform.rotate(missileImg, 180)
    window.blit(missileImg, [x + 16, y - 25])
    missileImg = pygame.transform.rotate(missileImg, 360)


# Game Loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    window.fill([0, 0, 51])
    window.blit(background, [0, 0])

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= PLAYER_SPEED
        if event.key == pygame.K_RIGHT:
            playerX += PLAYER_SPEED
        if event.key == pygame.K_SPACE:
            fire_missile(playerX, missileY)

    if playerX <= 0:
        playerX = 0
    elif playerX >= WIN_WIDTH - 64:
        playerX = WIN_WIDTH - 64

    invaderX += invaderX_change
    if invaderX <= 0:
        invaderX_change = INVADER_SPEED
        invaderY += invaderY_change
    elif invaderX >= WIN_WIDTH - 64:
        invaderX_change = -INVADER_SPEED
        invaderY += invaderY_change

    # Missile Movement
    if MISSILE_STATE is "fire":
        fire_missile(playerX, missileY)
        missileY -= missileY_change

    player(playerX, playerY)
    invader(invaderX, invaderY)
    pygame.display.update()
