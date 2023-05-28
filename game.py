import pygame
import sys
import time
import os
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

ship_path = "resources/Idle.png"
ship = pygame.image.load(ship_path)
ship = pygame.transform.scale(ship, (130, 130))
ship = pygame.transform.rotate(ship, 90)
ship_px = width / 2 - 65
ship_py = height*3 / 4

running = True

while running:
    clock.tick(25) #30 FPS

    #Load background
    i = 0 if i >= len(bg_arr) - 1 else i + 1
    bg = pygame.image.load(bg_path+"/"+bg_arr[i])
    bg = pygame.transform.scale(bg, (height, width))
    bg = pygame.transform.rotate(bg, 270)
    screen.blit(bg, (0, 0))

    #Detect keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #
    screen.blit(ship, (ship_px, ship_py))
    
    pygame.display.flip()
    

    

    
    
