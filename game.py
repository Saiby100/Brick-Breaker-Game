import pygame
import sys
import time
import os
from pygame.time import Clock


pygame.init()

width, height = 498, 574
screen = pygame.display.set_mode((width, height))
clock = Clock()

bg_type = "galaxy"
bg_path = f"resources/backgrounds/{bg_type}/frames"
bg_arr = os.listdir(bg_path)
i = len(bg_arr)

running = True

while running:
    clock.tick(10) #60 FPS

    if i >= len(bg_arr) - 1: 
        i = 0
    else: 
        i+=1

    bg = pygame.image.load(bg_path+"/"+bg_arr[i])
    screen.blit(bg, (0, 0))


    #Detect keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    

    pygame.display.flip()
    

    
    
