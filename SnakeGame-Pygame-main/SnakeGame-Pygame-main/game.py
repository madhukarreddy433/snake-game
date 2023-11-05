import time
import math
import pygame
import random

# Initialize the game
pygame.init()

# set the window dimensions
WIDTH = 512
HEIGHT = 512

# create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set caption and icon for the game
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('snakeIcon.png')
pygame.display.set_icon(icon)

# background image
bgImage = pygame.image.load('background.png')

# Fruit
fruitImage = pygame.image.load('strawberry.png')
fruitX = random.randint(1, WIDTH - 32)
fruitY = random.randint(35, HEIGHT - 32)

# Snake
snakeImage = pygame.image.load('snake.png')
snakeX = WIDTH // 2
snakeY = HEIGHT // 2
snakeDir = "right"

# directions map
DIRECTIONS = {"right": (1, 0), "left": (-1, 0), "up": (0, -1), "down": (0, 1)}

# score
SCORE = 0
scoreFont = pygame.font.Font('freesansbold.ttf', 32)

# gameover
GAMEOVER = False
gameOverFont = pygame.font.Font('MonomaniacOne-Regular.ttf', 64)

# game music
pygame.mixer.music.load('backgroundMusic.mp3')
pygame.mixer.music.play(-1)


# display fruit
def displayFruit(x, y):
    screen.blit(fruitImage, (x, y))


# display snake
def displaySnake(x, y):
    screen.blit(snakeImage, (x, y))


# display score
def displayScore():
    score = scoreFont.render(f"SCORE: {SCORE}", True, (0, 0, 255))
    screen.blit(score, (10, 10))


# display gameover
def displayGameOver():
    gameover = gameOverFont.render(f"GAME OVER", True, (255, 255, 0))
    screen.blit(gameover, (110, 200))


# game loop
while not GAMEOVER:
    screen.fill((100, 255, 78))
    screen.blit(bgImage, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMEOVER = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snakeDir = "right"
            if event.key == pygame.K_LEFT:
                snakeDir = "left"
            if event.key == pygame.K_UP:
                snakeDir = "up"
            if event.key == pygame.K_DOWN:
                snakeDir = "down"

    # moving the snake
    changeX, changeY = DIRECTIONS[snakeDir]
    snakeX += changeX
    snakeY += changeY

    # check snake bumped into the wall
    if snakeX < 1 or snakeX > (WIDTH - 32) or snakeY < 1 or snakeY > (HEIGHT - 32):
        if snakeX < 1:
            snakeX = 1
        elif snakeX > (WIDTH - 32):
            snakeX = WIDTH - 32
        elif snakeY < 1:
            snakeY = 1
        else:
            snakeY = HEIGHT - 32
        GAMEOVER = True

    # Snake Caught the fruit
    distance = math.dist([snakeX, snakeY], [fruitX, fruitY])
    if distance < 32:
        SCORE += 1
        pygame.mixer.Sound('chime-and-chomp.mp3').play()
        fruitX = random.randint(1, WIDTH - 32)
        fruitY = random.randint(35, HEIGHT - 32)

    # display the fruit, snake and score
    displayFruit(fruitX, fruitY)
    displaySnake(snakeX, snakeY)
    displayScore()

    # gameover
    if GAMEOVER:
        displayGameOver()
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.Sound('gameoverSound.mp3').play()
        time.sleep(3.1)

    # update the screen
    pygame.display.update()

    # wait for sometime before moving the snake
    time.sleep(0.01)
