import random
import time

import pygame

pygame.init()

SCREEN = pygame.display.set_mode((1000, 600))

life_count=3
def corOrdinateToNmb(x,y):
    if (x>150 and x<250):
        if(y >50 and y <150):
            return 21
        if (y > 150 and y < 250):
            return 20
        if (y > 250 and y < 350):
            return 11
        if (y > 350 and y < 450):
            return 10
        if (y > 450 and y < 550):
            return 1
    if (x>250 and x<350):
        if(y >50 and y <150):
            return 22
        if (y > 150 and y < 250):
            return 19
        if (y > 250 and y < 350):
            return 12
        if (y > 350 and y < 450):
            return 9
        if (y > 450 and y < 550):
            return 2


    if (x>350 and x<450):
        if(y >50 and y <150):
            return 23
        if (y > 150 and y < 250):
            return 18
        if (y > 250 and y < 350):
            return 13
        if (y > 350 and y < 450):
            return 8
        if (y > 450 and y < 550):
            return 3


    if (x>450 and x<550):
        if(y >50 and y <150):
            return 24
        if (y > 150 and y < 250):
            return 17
        if (y > 250 and y < 350):
            return 14
        if (y > 350 and y < 450):
            return 7
        if (y > 450 and y < 550):
            return 4

    if (x > 550 and x < 650):
        if (y > 50 and y < 150):
            return 25
        if (y > 150 and y < 250):
            return 16
        if (y > 250 and y < 350):
            return 15
        if (y > 350 and y < 450):
            return 6
        if (y > 450 and y < 550):
            return 5


def nmbToCo_ladder(nmb):
    if nmb==10:
        return (175,375)
    if nmb == 9:
        return (275, 375)
    if nmb == 8:
        return (375, 375)
    if nmb == 7:
        return (475, 375)
    if nmb == 6:
        return (575, 375)
    if nmb == 11:
        return (175, 275)
    if nmb == 12:
        return (275, 275)
    if nmb == 13:
        return (375, 275)
    if nmb == 14:
        return (475, 275)
    if nmb == 15:
        return (575, 275)
    if nmb==20:
        return (175,175)
    if nmb == 19:
        return (275, 175)
    if nmb == 18:
        return (375, 175)
    if nmb == 17:
        return (475, 175)
    if nmb == 16:
        return (575, 175)
    if nmb == 21:
        return (175, 75)
    if nmb == 22:
        return (275, 75)
    if nmb == 23:
        return (375, 75)
    if nmb == 24:
        return (475, 75)
    if nmb == 25:
        return (575, 75)



#coOrdinateToNmb for Ladder
def nmbToCordinate_green(nmb):
    if nmb==10:
        return (160,375)
    if nmb == 9:
        return (260, 375)
    if nmb == 8:
        return (360, 375)
    if nmb == 7:
        return (460, 375)
    if nmb == 6:
        return (560, 375)
    if nmb == 11:
        return (160, 275)
    if nmb == 12:
        return (260, 275)
    if nmb == 13:
        return (360, 275)
    if nmb == 14:
        return (460, 275)
    if nmb == 15:
        return (560, 275)
    if nmb==20:
        return (160,175)
    if nmb == 19:
        return (260, 175)
    if nmb == 18:
        return (360, 175)
    if nmb == 17:
        return (460, 175)
    if nmb == 16:
        return (560, 175)
    if nmb == 21:
        return (160, 75)
    if nmb == 22:
        return (260, 75)
    if nmb == 23:
        return (360, 75)
    if nmb == 24:
        return (460, 75)
    if nmb == 25:
        return (560, 75)


# ludu board
board_img = pygame.image.load("25board.png")
board_img_X = 150
board_img_Y = 50

#hard code

# snake image
snake_img = pygame.image.load("Snake1.png")
snake_img_X = 250+10
snake_img_Y = 250+25

#snake2 image
redSnake_img = pygame.image.load("redSnake.png")
redSnake_img_X = 450+10
redSnake_img_Y = 150+25

#Danger check
X_Start=snake_img_X-10
Y_Start=snake_img_Y-25

#Danger Red Snake
X_redSnake_Start=redSnake_img_X-10
Y_redSnake_Start=redSnake_img_Y-25

#ladder image
ladder_image=pygame.image.load("ladder2.png")
ladder_image_X=175
ladder_image_Y=75

#moi otha check
X_LadderEnd=ladder_image_X-25
Y_LadderEnd=ladder_image_Y-25+200

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

lifeImg=[]
lifeImg.append(pygame.image.load("life.png"))
lifeImg.append(pygame.image.load("life.png"))
lifeImg.append(pygame.image.load("life.png"))
lifeImg.append(pygame.image.load("life.png"))
lifeImg.append(pygame.image.load("life.png"))


Final_Coin_Y=coin_img_Y

#life_show
def lifeShow():
    for i in range(0,life_count):
        SCREEN.blit(lifeImg[i],(150+ (i * 80),0))

# draw board
def draw_board(x, y):
    SCREEN.blit(board_img, (x, y))


# draw snake
def draw_snake(x, y,rX,rY):
    SCREEN.blit(snake_img, (x, y))
    SCREEN.blit(redSnake_img, (rX, rY))

def draw_ladder(x,y):
    SCREEN.blit(ladder_image,(x,y))


# draw dice
def draw_dice():
    #print("dice = ", player_score)
    SCREEN.blit(diceImg[player_score - 1], (800, 150))


def draw_coin(x, y):
    SCREEN.blit(coin_img, (x, y))

def coin_Stable():
    global Final_Coin_X
    Final_Coin_X = coin_img_X
    global Final_Coin_Y
    Final_Coin_Y= coin_img_Y



clock = pygame.time.Clock()
time_dice_turned = 0
left_to_right = 1
right_to_left=1
coin_moving = False
dice_rolling = False
player_position = player_score
eating=False
redEating=False
coin_stable=1
uthing=False
odd=0
rolling_check=True
dice_checking=0


running = True

while running:
    print(nmbToCo_ladder(12))
    SCREEN.fill((195, 115, 42))
    draw_board(board_img_X, board_img_Y)
    draw_snake(snake_img_X, snake_img_Y,redSnake_img_X,redSnake_img_Y)
    draw_ladder(ladder_image_X,ladder_image_Y)
    lifeShow()
    if player_position==1:
        draw_coin(coin_img_X, coin_img_Y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dice_rolling:
                    dice_rolling = True
            if event.key==pygame.K_o:
                odd=1
            if event.key==pygame.K_e:
                odd=0

    coin_Stable()

    #draw_dice()
    # shap khaile niche namche
    if odd==1:
        if eating:
            life_count-=1
            coin_img_Y += 100
            eating = False
            snake_tail_position=corOrdinateToNmb(snake_img_X,snake_img_Y+100)
            print("downfall")
            player_position =snake_tail_position
            left_to_right *= -1
        if redEating:
            life_count-=1
            coin_img_Y += 100
            redEating = False
            red_snake_tail_position=corOrdinateToNmb(redSnake_img_X,redSnake_img_Y+100)
            print("downfall")
            player_position =red_snake_tail_position
            left_to_right *= -1

        if uthing:
            coin_img_Y -= 100
            uthing = False
            ladder_headPosition=corOrdinateToNmb(ladder_image_X,ladder_image_Y)
            print("Flying")
            player_position=ladder_headPosition
            left_to_right *= -1

        # Coin Moving
        if (coin_moving==True and rolling_check==True):
            print("Check:",rolling_check)
            if (player_position < destination and destination <= 25):
                # print("left to right", left_to_right)

                if player_position % 5 == 0:
                    coin_img_Y -= 100
                    left_to_right *= -1
                else:
                    coin_img_X += left_to_right * 100
                print(coin_img_X, coin_img_Y)
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
                if (X_redSnake_Start < coin_img_X and coin_img_X < X_redSnake_Start + 100):
                    if (Y_redSnake_Start < coin_img_Y and coin_img_Y < Y_redSnake_Start + 100):
                        print("red shap amk khacce")
                        redEating = True

                if (X_LadderEnd < coin_img_X and coin_img_X < X_LadderEnd + 100):
                    if (Y_LadderEnd - 100 < coin_img_Y and coin_img_Y < Y_LadderEnd):
                        print("moi e uthc")
                        uthing = True
                coin_moving = False

        #Snake_Moving
        if(rolling_check==False and dice_checking!=0):
            #snake_img_X=snake_img_X+player_score*100
            print("Shap nore")

            snake_position=corOrdinateToNmb(snake_img_X,snake_img_Y)
            red_snakePosition=corOrdinateToNmb(redSnake_img_X,redSnake_img_Y)
            ladder_head_pos=corOrdinateToNmb(ladder_image_X,ladder_image_Y)
            ladder_tail_pos=corOrdinateToNmb(ladder_image_X,ladder_image_Y+100)
            print("ladderHeadPositon:",ladder_head_pos)
            print("LadderTail Pos",ladder_tail_pos)

            print("snake pos:",snake_position)
            if(snake_position-player_position>6 ):
                if (red_snakePosition - player_position > 6 and red_snakePosition - player_score > 5):
                    if(red_snakePosition>snake_position and snake_position-player_score>5):
                        snake_position-=player_score
                        print("playerScore:",player_score)
                        print("snakeiiiii:",snake_position)

                        (snake_img_X,snake_img_Y)=nmbToCordinate_green(snake_position)
                        print("Snake position:",snake_img_X,snake_img_Y)
                        X_Start = snake_img_X - 10
                        Y_Start = snake_img_Y - 25
                        draw_snake(snake_img_X,snake_img_Y,redSnake_img_X,redSnake_img_Y)
                    elif(red_snakePosition>snake_position and snake_position-player_score<=5):
                        red_snakePosition-= player_score
                        (redSnake_img_X,redSnake_img_Y)=nmbToCordinate_green(red_snakePosition)
                        X_redSnake_Start=redSnake_img_X-10
                        Y_redSnake_Start=redSnake_img_Y-25
                        draw_snake(snake_img_X,snake_img_Y,redSnake_img_X,redSnake_img_Y)
                        print("Red snake nore jao")
                    else:
                        print("moi norbe3")
                        if(ladder_tail_pos>player_position and ladder_head_pos-player_score>5 and ladder_head_pos+player_score<=25):
                            ladder_head_pos+=player_score
                            (ladder_image_X,ladder_image_Y)=nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X,ladder_image_Y)

                        if (ladder_tail_pos < player_position and ladder_head_pos-player_score>5):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y)

            if(snake_position-player_position<=6 and snake_position-player_position>=0 and snake_position-player_score>5):
                if (red_snakePosition - player_position > 6 and red_snakePosition - player_score > 5):
                    print("0 to 6 ")
                    red_snakePosition -= player_score
                    (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                    X_redSnake_Start = redSnake_img_X - 10
                    Y_redSnake_Start = redSnake_img_Y - 25
                    draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y)

                else:
                    print("Moi norbe")
                    if (ladder_tail_pos > player_position and ladder_head_pos-player_score>5 and ladder_head_pos+player_score<=25):
                        ladder_head_pos += player_score
                        (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                        X_LadderEnd = ladder_image_X - 25
                        Y_LadderEnd = ladder_image_Y - 25 + 200
                        draw_ladder(ladder_image_X, ladder_image_Y)

                    if (ladder_tail_pos < player_position and ladder_head_pos-player_score>5):
                        ladder_head_pos -= player_score
                        (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                        X_LadderEnd = ladder_image_X - 25
                        Y_LadderEnd = ladder_image_Y - 25 + 200
                        draw_ladder(ladder_image_X, ladder_image_Y)

            if (snake_position - player_position <0 and snake_position-player_position>-6 and snake_position-player_score>5):
                if (red_snakePosition - player_position > 6 and red_snakePosition - player_score > 5):
                    print(" 0 to -6 green snake")
                    red_snakePosition -= player_score
                    (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                    X_redSnake_Start = redSnake_img_X - 10
                    Y_redSnake_Start = redSnake_img_Y - 25
                    draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y)
                else:
                    snake_position += player_score
                    (snake_img_X, snake_img_Y) = nmbToCordinate_green(snake_position)
                    print("Positionnnnn:",snake_img_X,snake_img_Y)
                    X_Start = snake_img_X - 10
                    Y_Start = snake_img_Y - 25
                    if(snake_position==player_position):
                        eating=True

            if ( snake_position - player_position < -6 and snake_position-player_score>5):
                if (red_snakePosition - player_position > 6 and red_snakePosition - player_score > 5):
                    red_snakePosition -= player_score
                    (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                    X_redSnake_Start = redSnake_img_X - 10
                    Y_redSnake_Start = redSnake_img_Y - 25
                    draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y)
                else:
                    print("moi norbe 2")
                    if (ladder_tail_pos > player_position and ladder_head_pos-player_score>5 and ladder_head_pos+player_score<=25):
                        ladder_head_pos += player_score
                        (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                        X_LadderEnd = ladder_image_X - 25
                        Y_LadderEnd = ladder_image_Y - 25 + 200
                        draw_ladder(ladder_image_X, ladder_image_Y)

                    if (ladder_tail_pos < player_position and ladder_head_pos-player_score>5):
                        ladder_head_pos -= player_score
                        (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                        X_LadderEnd = ladder_image_X - 25
                        Y_LadderEnd = ladder_image_Y - 25 + 200
                        draw_ladder(ladder_image_X, ladder_image_Y)

            dice_checking=0



        # Dice Rolling
        if dice_rolling:
            player_score = random.randint(1, 6)
            #player_score=4
            dice_checking=player_score
            print("Score in dice roll:",player_score)
            dice_rolling = False
            if (player_score % 2 == 0 and dice_checking!=0):
                rolling_check = False
            if(player_score%2==1 and dice_checking!=0):
                rolling_check=True
            coin_moving = True
            #time_dice_turned = 0
            destination = player_score + player_position

        draw_dice()
        draw_coin(coin_img_X, coin_img_Y)
        coin_Stable()

        if life_count==0:
            print("End Game")


    clock.tick(60)
    time.sleep(.05)
    pygame.display.update()


