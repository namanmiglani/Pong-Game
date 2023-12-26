#importing pygame, sys, and random
import pygame
import sys
import random

#setup
pygame.init() 
time = pygame.time.Clock()

#window setup
windowWidth = 1280
windowHeight = 720
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pong Game')

ball = pygame.Rect(windowWidth/2 - 15, windowHeight/2 - 15,30,30) 
user = pygame.Rect(windowWidth - 20, windowHeight/2 - 70,10,140)
cpu = pygame.Rect(10, windowHeight/2 - 70,10,140)
#hex codes for colors (red, green, blue)
backroundColor = (64, 64, 64) 
lightGrey = (200, 200, 200)
gold = (255,215,0)

#font for score
font_Style = pygame.font.SysFont("Times New Roman", 25)
score_Font = pygame.font.SysFont("Times New Roman", 35)

#constants and some variables that change to adjust game
randomNumber=random.randint(3,21)
hits=0
ballSpeedX= 7 * random.choice((1,-1)) 
ballSpeedY= 7 * random.choice((1,-1)) 
userSpeed = 0
cpuSpeed = 7
score = 0

#ball movement and bouncing off walls and cpu/user paddle also adds to the score and hits
def ball_movement():
    global ballSpeedX, ballSpeedY, score, hits, randomNumber
    ball.x += ballSpeedX
    ball.y += ballSpeedY
    
    if ball.top <=0 or ball.bottom >= windowHeight:
        ballSpeedY *= -1
    if ball.left <= 0 or ball.right >= windowWidth:
        ball_restart()
        
    if ball.colliderect(user) or ball.colliderect(cpu):
        ballSpeedX *= -1
        score+=1
        hits+=1
#after cpu or user loses ball resets at the center and goes a random direction 
def ball_restart():
    global ballSpeedX, ballSpeedY,score
    ball.center = (windowWidth/2, windowHeight/2)
    ballSpeedY *= random.choice((1,-1))
    ballSpeedX *= random.choice((1,-1))
    score=0
    
    
#checks user input for moving up and down with the paddle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                userSpeed += 7
            if event.key == pygame.K_UP:
                userSpeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                userSpeed -= 7
            if event.key == pygame.K_UP:
                userSpeed += 7
            
    
    ball_movement()
    user.y += userSpeed
    #makes the paddles stay on the screen 
    if user.top <= 0:
        user.top = 0
    if user.bottom >= windowHeight:
        user.bottom = windowHeight
    #makes it impossible to beat cpu for a random number of hits based of the randon generated number
    if hits<= randomNumber:
        if cpu.top < ball.y:
            cpu.top += cpuSpeed
        if cpu.bottom > ball.y:
            cpu.bottom -= cpuSpeed*2
        cpu.y=ball.y
        if cpu.top <= 0:
            cpu.top = 0
        if cpu.bottom >= windowHeight:
            cpu.bottom = windowHeight
    #once that random number is passed cpu is easier to beat since it it not equal to the balls y coordinate
    else:
        if cpu.top < ball.y:
            cpu.top += cpuSpeed
        if cpu.bottom > ball.y:
            cpu.bottom -= cpuSpeed
        if cpu.top <= 0:
            cpu.top = 0
        if cpu.bottom >= windowHeight:
            cpu.bottom = windowHeight
   
    #making the backround, line down the middle, ball, and paddles
    window.fill(backroundColor)       
    pygame.draw.rect(window, lightGrey, user)
    pygame.draw.rect(window, lightGrey, cpu)
    pygame.draw.ellipse(window, lightGrey, ball)
    pygame.draw.aaline(window, lightGrey, (windowWidth/2,0), (windowWidth/2,windowHeight))
    
    #score at the top corner
    player_text = font_Style.render(f'Score= {score}',False,gold)
    window.blit(player_text,(20,20))


    #updates the window
    pygame.display.flip()
    time.tick(60) #refresh rate (adjustable if monitor screen doesn't support frame rate)
