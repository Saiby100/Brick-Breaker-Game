import pygame
import sys
import os
from pygame.time import Clock
from utils.ship import *
from utils.enemy import *
from utils.bullet import *
import random

'''
    Returns an array for the background frames
'''
def get_bg_array(bg_type):
    global bg_path

    bg_path = f"resources/backgrounds/{bg_type}/frames"
    bg_arr = os.listdir(bg_path)
    bg_arr.sort()

    return bg_arr

#SETTING UP
pygame.init()

width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
clock = Clock()

#BACKGROUND VARS
bg_arr = get_bg_array("galaxy")
i = len(bg_arr)

score = 0
lives = 3

colours = ["blue", "green", "orange", "purple", "red", "yellow"]

colour = colours[random.randint(0, len(colours))]
my_ship = Ship(colour, (width/2, height/4 * 3))
enemy = EnemyShip("Ship2", 120, width/2, 120)

array = [my_ship.get_thrusters(), my_ship]
ally_ships = pygame.sprite.Group(array)
enemy_ships = pygame.sprite.Group(enemy)

ally_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

running = True
bg_anim_speed = 0.5

while running:
    clock.tick(40) #30 FPS

    #Load background
    i = 0 if i >= len(bg_arr) - 1 else i + bg_anim_speed
    bg = pygame.image.load(bg_path+"/"+bg_arr[int(i)])
    bg = pygame.transform.scale(bg, (height, width))
    bg = pygame.transform.rotate(bg, 270)
    screen.blit(bg, (0, 0))

    #Detect keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_ship.shoot()
                bullet = Bullet(my_ship.get_bullet_type(), 
                                my_ship.get_bullet_size(), 
                                my_ship.get_top())
                ally_bullets.add(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        my_ship.move_left()
    if keys[pygame.K_RIGHT]:
        my_ship.move_right()
    if keys[pygame.K_UP]:
        my_ship.move_up()
    if keys[pygame.K_DOWN]:
        my_ship.move_down()
    
    #Draw sprites
    ally_ships.draw(screen)
    ally_bullets.draw(screen)

    enemy_ships.draw(screen)
    enemy_bullets.draw(screen)

    ally_ships.update()
    ally_bullets.update()

    enemy_ships.update()
    enemy_bullets.update()

    #Detect collisions
    pygame.sprite.groupcollide(enemy_ships, ally_bullets, True, True)
    
    pygame.display.flip()
    