import random
import time

import pygame

pygame.init()

SCREEN = pygame.display.set_mode((1000, 600))

# ludu board
board_img = pygame.image.load("25board.png")
board_img_X = 150
board_img_Y = 50

# snake image
snake_img = pygame.image.load("snake.png")
snake_img_X = 240
snake_img_Y = 330

# coin image
coin_img = pygame.image.load("coin.png")
coin_img_X = 150 + 30
coin_img_Y = 50 + 430

# player initial score
player_score = 1

# load dice images
diceImg = []
diceImg.append(pygame.image.load('dice1p2.png'))
diceImg.append(pygame.image.load('dice2p2.png'))
diceImg.append(pygame.image.load('dice3p2.png'))
diceImg.append(pygame.image.load('dice4p2.png'))
diceImg.append(pygame.image.load('dice5p2.png'))
diceImg.append(pygame.image.load('dice6p2.png'))


# draw board
def draw_board(x, y):
    SCREEN.blit(board_img, (x, y))


# draw snake
def draw_snake(x, y):
    SCREEN.blit(snake_img, (x, y))


# draw dice
def draw_dice():
    print("dice = ", player_score)
    SCREEN.blit(diceImg[player_score - 1], (800, 150))


def draw_coin(x, y):
    SCREEN.blit(coin_img, (x, y))


clock = pygame.time.Clock()
time_dice_turned = 0
left_to_right = 1
coin_moving = False
dice_rolling = False
player_position = player_score
running = True
while running:
    SCREEN.fill((195, 115, 42))
    draw_board(board_img_X, board_img_Y)
    draw_snake(snake_img_X, snake_img_Y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dice_rolling:
                    dice_rolling = True

    if dice_rolling:
        player_score = random.randint(1, 6)

        # draw_dice()
        time_dice_turned += 1
        # time.sleep(.5)
        if time_dice_turned > 2:
            dice_rolling = False
            coin_moving = True
            time_dice_turned = 0
            destination = player_score + player_position
        print("Score", player_score)
        print("time dice turned", time_dice_turned)

    draw_dice()

    draw_coin(coin_img_X, coin_img_Y)
    if coin_moving:
        if player_position < destination:
            print("left to right", left_to_right)

            if player_position % 5 == 0:
                coin_img_Y -= 100
                left_to_right *= -1
            else:
                coin_img_X += left_to_right * 100
            print(coin_img_X)
            player_position += 1

            if destination == player_position:
                coin_moving = False

    print("coin moving , dice rolling", coin_moving, dice_rolling)
    clock.tick(60)
    time.sleep(.5)
    pygame.display.update()
