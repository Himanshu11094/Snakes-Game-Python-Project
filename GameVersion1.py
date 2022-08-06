import pygame
import random
import os

pygame.mixer.init()         # to initialize music in the code




pygame.init()

#Colors: having RGB values from 0(dark) to 255(light)
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
random_color = (50,80,110)

screen_width = 900
screen_height = 600

#Creating Game window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Background Image

bgimg1 = pygame.image.load("firstbg.jpg")                                     # convert alpha helps for the smooth function of game when we blit it again and again
bgimg1 = pygame.transform.scale(bgimg1,(screen_width,screen_height)).convert_alpha()

bgimg2 = pygame.image.load("download.jpg")
bgimg2 = pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha()

#GAME title
pygame.display.set_caption("SNAKE")
pygame.display.update()      # everytime we make changes on display we have to update using this function



# Game specific variables


clock = pygame.time.Clock()                      # this is to define the clock in code

font = pygame.font.SysFont(None, 55)             # font variable

def text_screen(text,color, x, y):               #(what text to print, color, x-coord, y-coord)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])                   #updating the screen(screen text, list-coordinates)


def plot_snake(gameWindow, color, snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gameWindow.fill((210,140,190))
        gameWindow.blit(bgimg1, (0, 0))
        text_screen("Welcome to Snakes", black,200,100)
        text_screen("Press SPACE to Play", black, 200, 200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()






        pygame.display.update()
        clock.tick(60)

# game Loop

def gameloop():

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 15
    fps = 30  # frames per second
    offset = 15
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    food_size = 7
    score = 0
    snake_list = []
    snake_length = 1

    # check if hiscore file exists
    if (not os.path.exists("hi_score.txt")):
        with open("hi_score.txt", "w") as f:
            f.write("0")

    with open("hi_score.txt","r") as f:  # reading data from text file, using "with" so that we don't have to close the file
        hiscore = f.read()  # this reads the file as string


    while not exit_game:

        if game_over:
            gameWindow.blit(bgimg1, (0, 0))


            with open("hi_score.txt", "w") as f:
              f.write(str(hiscore))                              #writing the file as string


            text_screen("GAME OVER!!!", red, 200, 100)
            text_screen("Press ENTER to Continue", red, 200, 200)
            text_screen("q to QUIT", red, 200, 300)
            for event in pygame.event.get():

                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                         welcome()
                    if event.key == pygame.K_q:
                        exit_game = True

        else:

            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0


                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0


                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -5


                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = 5

                    if event.key == pygame.K_q:
                        exit_game = True

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                score+=1
                snake_length +=5
                if score>int(hiscore):
                    hiscore = score
                    with open("hi_score.txt", "w") as f:
                        f.write(str(score))






            gameWindow.fill(white)
            gameWindow.blit(bgimg2,(0,0))
            text_screen("Score: " + str(score) + "  HiScore: "+ str(hiscore)+"    Press q to QUIT", red, 5, 5)  # calling function here
            pygame.draw.rect(gameWindow, random_color, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:                  # to delete previous positions
                del snake_list[0]

            if head in snake_list[:-1]:                        # makes game over if snake collides with himself
                pygame.mixer.music.load('Blast.mp3')
                pygame.mixer.music.play()
                game_over= True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load('Blast.mp3')
                pygame.mixer.music.play()
                game_over = True
               # print("Game Over")


            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y,snake_size, snake_size])  #previously we were making snake directly here
            plot_snake(gameWindow, black, snake_list,snake_size )       # now we've defined a function


        pygame.display.update()
        clock.tick(fps)               # this clock works as per fps passed how many ticks we want every second

    pygame.quit()
    quit()

welcome()