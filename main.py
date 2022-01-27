import pygame, sys
import time
import os
from pygame.time import Clock

pygame.init()

class Brick(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(path, 'resources/brick.png'))
        self.rect = self.image.get_rect()

def set_brick_amount(amount):
    x, y = 0, 80
    a, b = 8, 8
    for i in range(0, amount):  # Organizes bricks on the screen
        if i == a:
            y += 80
            x = bricks.sprites()[i - b].rect.centerx
            b -= 1
            a += b
        brick = Brick()
        brick.rect.left = x
        brick.rect.top = y
        bricks.add(brick)
        x += 190

def detect_collision(obj):
    if ball_rect.colliderect(obj):
        if abs(obj.bottom - ball_rect.top) < 10:
            speed[1] *= -1
        elif abs(obj.top - ball_rect.bottom) < 10:
            speed[1] *= -1
        elif abs(obj.right - ball_rect.left) < 10 or abs(obj.left - ball_rect.right) < 10:
            speed[0] *= -1

        if ball_rect.collidepoint(obj.topright):
            speed[0] = speed_x
            speed[1] *= -1
        elif ball_rect.collidepoint(obj.topleft):
            speed[0] = -speed_x
            speed[1] *= -1

        if ball_rect.collidepoint(obj.bottomright):
            speed[0] = speed_x
            speed[1] = speed_y
        if ball_rect.collidepoint(obj.bottomleft):
            speed[0] = -speed_x
            speed[1] = speed_y

        return True

def pause(display_text, key):
    text = font.render(display_text, True, (0, 255, 0))
    text_rect = text.get_rect()
    text_rect.center = width / 2, height / 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True

        screen.fill((0, 0, 51))
        screen.blit(text, text_rect)
        screen.blit(score_text, score_text_rect)
        screen.blit(lives_text, lives_text_rect)
        screen.blit(high_score_text, high_score_text_rect)
        pygame.display.flip()

def set_highscore(score):
    with open(os.path.join(path, 'resources/Highscores.txt'), 'r') as file:
        if int(file.readline()) < score:
            with open(os.path.join(path, 'resources/Highscores.txt'), 'w') as score_file:
                score_file.write(str(score))

def get_highscore():
    with open(os.path.join(path, 'resources/Highscores.txt'), 'r') as file:
        return file.readline()

#LOADING IMAGES
path = os.path.dirname(__file__)
brick = pygame.image.load(os.path.join(path, 'resources/brick.png'))
bar = pygame.image.load(os.path.join(path, 'resources/bar.png'))
ball = pygame.image.load(os.path.join(path, 'resources/main_ball.png'))
icon = pygame.image.load(os.path.join(path, 'resources/main_ball.png'))

#SETTING UP DISPLAY
width, height = 1520, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Brick Breaker')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)

#INITIALIZING OBJECTS AND VARIABLES
clock = Clock()
bar_rect = bar.get_rect()
ball_rect = ball.get_rect()

bricks = pygame.sprite.Group()
set_brick_amount(36)

score_count = 0
score_text = font.render('Score: '+str(score_count), True, (0, 255, 0))
score_text_rect = score_text.get_rect()

life_count = 3
lives_text = font.render('Lives: '+str(life_count), True, (0, 255, 0))
lives_text_rect = lives_text.get_rect()


high_score_text = font.render('Current Highest Score: ' + get_highscore(), True, (0, 255, 0))
high_score_text_rect = high_score_text.get_rect()

#VARIABLE MODIFICATION
move = False
speed_x, speed_y = 5, 5
speed = [speed_x, speed_y]
bar_rect.center = width/2, 0
bar_rect.bottom = height
x = 0
score_text_rect.left = 0 + 10
score_text_rect.top = 0 + 10
lives_text_rect.right = width -10
lives_text_rect.top = 0 + 10
high_score_text_rect.centerx = width/2
high_score_text_rect.top = 0 + 10

print('Press Space to Start')
pause('Brick Breaker!!', pygame.K_SPACE)

while True:
    # Background
    screen.fill((0, 0, 51))
    # clock.tick(250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        # Launch line key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and x > -50:
                x -= 50
            if event.key == pygame.K_d and x < 50:
                x += 50
            if event.key == pygame.K_SPACE and not move:
                if x == -50:
                    speed[0] = -abs(speed_x)
                    speed[1] = -abs(speed[1])
                elif x == 0:
                    speed[0] = 0
                    speed[1] = -abs(speed[1])
                else:
                    speed[0] = abs(speed_x)
                    speed[1] = -abs(speed[1])
                move = True
            if event.key == pygame.K_RETURN:
                pause('Press Enter To Continue', pygame.K_RETURN)

    # Bar movement key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if bar_rect.left >= 0:
            bar_rect = bar_rect.move([-4, 0])
    if keys[pygame.K_RIGHT]:
        if bar_rect.right <= width:
            bar_rect = bar_rect.move([4, 0])

    # Detects if ball is stationary or moving
    if move:
        ball_rect = ball_rect.move(speed)
    else:
        ball_rect.bottom = bar_rect.top - 10
        ball_rect.centerx = bar_rect.centerx
        # Launch line
        line_cords = [(bar_rect.centerx, ball_rect.top - 10), (ball_rect.centerx + x, ball_rect.top - 60)]
        pygame.draw.line(screen, (255, 255, 255), line_cords[0], line_cords[1])

    # Ball collision with border (window)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] *= -1
    if ball_rect.top < 0:
        speed[1] *= -1
    if ball_rect.centery > height:
        move = False
        x = 0
        #Life is lost when going below border floor
        life_count -= 1

    # Ball collision with bar
    detect_collision(bar_rect)

    #Removes brick when collision occurs
    for brick in bricks.sprites():
        if detect_collision(brick.rect):
            score_count += 1
            bricks.remove(brick)

    #If out of lives
    if life_count < 0:
        if pause('Game over...Press Enter to Play Again', pygame.K_RETURN):
            set_highscore(score_count)
            high_score_text = font.render('Current Highest Score: ' + get_highscore(), True, (0, 255, 0))

            move = False
            life_count = 3
            score_count = 0
            bricks.empty()
            set_brick_amount(36)
            bar_rect.centerx = width/2

    #If all blocks are broken
    if bricks.__len__() == 0:
        if pause('Press Enter To Play Again', pygame.K_RETURN):
            move = False
            set_brick_amount(36)

    #Score and Lives text are updated after each loop
    score_text = font.render('Score: ' + str(score_count), True, (0, 255, 0))
    lives_text = font.render('Lives: ' + str(life_count), True, (0, 255, 0))

    #Draw all objects onto screen
    bricks.draw(screen)
    bricks.update()
    screen.blit(high_score_text, high_score_text_rect)
    screen.blit(lives_text, lives_text_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(ball, ball_rect)
    screen.blit(bar, bar_rect)

    pygame.display.flip()

