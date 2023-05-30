import pygame
import sys
import time
import os
from utils.ship import Ship
from pygame.time import Clock

'''
    Returns an array for the background frames
'''
def get_bg_array(bg_type):
    global bg_path

    bg_path = f"resources/backgrounds/{bg_type}/frames"
    bg_arr = os.listdir(bg_path)
    bg_arr.sort()

    return bg_arr


pygame.init()

width, height = 800, 500
screen = pygame.display.set_mode((width, height))
clock = Clock()

bg_arr = get_bg_array("galaxy")
i = len(bg_arr)

ship_px = width / 2 - 45
ship_py = height*3 / 4

main_group = pygame.sprite.Group()
my_ship = Ship(ship_px, ship_py)
my_ship.resize(90, 90)
my_ship.rotate(90)
main_group.add(my_ship)

running = True

while running:
    clock.tick(25) #30 FPS

    #Load background
    i = 0 if i >= len(bg_arr) - 1 else i + 1
    bg = pygame.image.load(bg_path+"/"+bg_arr[i])
    # bg = pygame.transform.scale(bg, (width, height))
    bg = pygame.transform.scale(bg, (height, width))
    bg = pygame.transform.rotate(bg, 270)
    screen.blit(bg, (0, 0))

    #Detect keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #Draw sprites
    main_group.draw(screen)
    main_group.update()
    
    pygame.display.flip()
    

    

    
    
