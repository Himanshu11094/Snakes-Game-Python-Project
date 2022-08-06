import pygame
import random
pygame.init()

#Colors: having RGB values from 0(dark) to 255(light)
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 600
screen_height = 600

#Creating Game window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#GAME title
pygame.display.set_caption("SNAKE")
pygame.display.update()      # everytime we make changes on display we have to update using this function

# Game specific variables
exit_game = False
game_over = False
snake_x =45
snake_y= 55
snake_size = 15
fps = 30                               #frames per second
offset = 15
velocity_x = 0
velocity_y = 0
food_x= random.randint(0,screen_width)
food_y= random.randint(0,screen_height)
food_size = 7
score = 0

clock = pygame.time.Clock()                      # this is to define the clock in code

font = pygame.font.SysFont(None, 55)             # font variable

def text_screen(text,color, x, y):               #(what text to print, color, x-coord, y-coord)
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])                   #updating the screen(screen text, list-coordinates)


def plot_snake(gameWindow, color, snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snake_list = []
snake_length = 1

# game Loop

while not exit_game:
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


    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        food_x = random.randint(0, screen_width)
        food_y = random.randint(0, screen_height)
        score+=1
        snake_length +=5






    gameWindow.fill(white)
    text_screen("Score: " + str(score), red, 5, 5)  # calling function here
    pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len(snake_list)>snake_length:
        del snake_list[0]

    #pygame.draw.rect(gameWindow, black, [snake_x, snake_y,snake_size, snake_size])  #previously we were making snake directly here
    plot_snake(gameWindow, black, snake_list,snake_size )       # now we've defined a function


    pygame.display.update()
    clock.tick(fps)               # this clock works as per fps passed how many ticks we want every second

pygame.quit()
quit()