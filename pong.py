import pygame
import pygame.freetype
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()



#INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")
run = True
direction = [0, 1]
angle = [0, 1, 2]
left_score = 0
right_score = 0

my_font = pygame.font.SysFont('Comic Sans MS', 30)
font = pygame.font.Font(pygame.font.get_default_font(), 36)



#colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.2, 0.2

#for the paddle
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0


#MAIN LOOP
while run: 
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9

        if i.type == pygame.KEYUP:
            right_paddle_vel, left_paddle_vel = 0, 0

    text_surface = font.render(str(left_score) + " : " + str(right_score), True, (255, 255, 255))
    wn.blit(text_surface, dest=(WIDTH/2,HEIGHT/2))

    #BALL MOVEMENT CONTROLS
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
        pygame.mixer.Sound("sound assets/pongbassplip.mp3").play()
        #hit top/bottom

    if ball_x >= WIDTH - radius: #right side
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.4, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.2, 0.2
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.2, 0.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.4, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.2, 0.2
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.2, 0.4

        ball_vel_x *= -1
        pygame.mixer.Sound("sound assets/gameover.mp3").play()
        left_score += 1


    if ball_x <= 0 + radius: #left side
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -0.4, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.2, 0.2
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.2, 0.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 0.4, 0.2
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.2, 0.2
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.2, 0.4
        pygame.mixer.Sound("sound assets/gameover.mp3").play()
        right_score += 1

    #paddle movement controls
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <=0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <=0:
        right_paddle_y = 0   

    #paddle collisions
    #left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
            pygame.mixer.Sound("sound assets/pongblip.mp3").play()

    #right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1
            pygame.mixer.Sound("sound assets/pongblip.mp3").play()

    #MOVEMENTS
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

     

    #OBJECTS
    pygame.draw.circle(wn, RED, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, WHITE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, WHITE, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()
    

