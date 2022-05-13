import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
green = (50, 111, 50)
blue = (0, 0, 255)
 
width = 600
height = 400
 
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_Block = 10
snake_Speed = 15
 
font_Style = pygame.font.SysFont("Verdana", 25)
score_Font = pygame.font.SysFont("Verdana", 35)
 
 
def your_Score(score):
    value = score_Font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_Snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        
 
def message(msg, color):
    mesg = font_Style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])
 
 
def game_Loop():
    game_over = False
    game_close = False
 
    x1 = width / 2
    y1 = height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, width - snake_Block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_Block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_Score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_Loop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_Block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_Block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_Block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_Block
                    x1_change = 0
 
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_Block, snake_Block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_Snake(snake_Block, snake_List)
        your_Score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_Block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_Block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_Speed)
 
    pygame.quit()
    quit()
 
 
game_Loop()