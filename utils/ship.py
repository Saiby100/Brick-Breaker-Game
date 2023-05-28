import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.sprites = []
        self.cur_sprite = 0
