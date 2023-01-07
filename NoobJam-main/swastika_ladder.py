import random
import time

import pygame

pygame.init()

SCREEN = pygame.display.set_mode((1000, 600))


# ludu board
board_img = pygame.image.load("25board.png")
board_img_X = 150
board_img_Y = 50

# hard code

# snake image
snake_img = pygame.image.load("Snake1.png")
snake_img_X = 250 + 10
snake_img_Y = 250 + 25

# Danger check
X_Start = snake_img_X - 10
Y_Start = snake_img_Y - 25

# ladder image
ladder_image = pygame.image.load("ladder.png")
ladder_image_X = 400
ladder_image_Y = 100

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

Final_Coin_Y = coin_img_Y


# draw board
def draw_board(x, y):
    SCREEN.blit(board_img, (x, y))


# draw snake
def draw_snake(x, y):
    SCREEN.blit(snake_img, (x, y))


def draw_ladder(x, y):
    SCREEN.blit(ladder_image, (x, y))


# draw dice
def draw_dice():
    SCREEN.blit(diceImg[player_score - 1], (800, 150))


def draw_coin(x, y):
    SCREEN.blit(coin_img, (x, y))


def coin_Stable():
    global Final_Coin_X
    Final_Coin_X = coin_img_X
    global Final_Coin_Y
    Final_Coin_Y = coin_img_Y


clock = pygame.time.Clock()
time_dice_turned = 0
left_to_right = 1
right_to_left = 1
coin_moving = False
dice_rolling = False
player_position = player_score
eating = False
coin_stable = 1

running = True
###
print(X_Start, Y_Start)
while running:
    SCREEN.fill((195, 115, 42))
    draw_board(board_img_X, board_img_Y)
    draw_snake(snake_img_X, snake_img_Y)
    draw_ladder(ladder_image_X, ladder_image_Y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dice_rolling:
                    dice_rolling = True

    coin_Stable()

    # shap khaile niche namche
    if eating:
        coin_img_Y += 100
        eating = False
        print("downfall")
        player_position -= 3
        left_to_right *= -1


    if coin_moving:
        if player_position < destination and destination <= 25:
            if player_position % 5 == 0:
                coin_img_Y -= 100
                left_to_right *= -1
            else:
                coin_img_X += left_to_right * 100

            player_position += 1

            if destination == player_position:
                print("destination ", coin_img_X, coin_img_Y)
                print("final coin x, y", Final_Coin_X, Final_Coin_Y)
                print("x_start, y_start", X_Start, Y_Start)
                # shap amk khacce
                if X_Start < coin_img_X and coin_img_X < X_Start + 100:
                    if Y_Start < coin_img_Y and coin_img_Y < Y_Start + 100:
                        print("shap amk khacce")
                        print("final coin x, y", Final_Coin_X, Final_Coin_Y)
                        print("x_start, y_start", X_Start, Y_Start)
                        eating = True

                coin_moving = False

    if dice_rolling:
        player_score = random.randint(1, 6)
        time_dice_turned += 1
        if time_dice_turned > 2:
            dice_rolling = False
            coin_moving = True
            time_dice_turned = 0
            destination = player_score + player_position

    draw_dice()
    # print(coin_img_X, coin_img_Y)


    draw_coin(coin_img_X, coin_img_Y)
    coin_Stable()


    clock.tick(60)
    time.sleep(.5)
    pygame.display.update()
