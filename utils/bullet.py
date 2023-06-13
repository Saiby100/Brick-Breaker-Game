import pygame
import os

class Bullet(pygame.sprite.Sprite):
    def __init__(self, shot_type, size, pos):
        super().__init__()

        self.anim_complete = False
        self.anim_speed = 0.2
        self.size = size
        self.mov_dist = 8

        path = f"resources/Shots/{shot_type}/"
        frame_images = os.listdir(path)
        frame_images.sort()

        self.frames = []
        self.max_frames = len(frame_images)
        self.frame = 0

        for frame in frame_images:
            img = pygame.image.load(path+frame)
            img = pygame.transform.scale(img, (self.size, self.size))
            img = pygame.transform.rotate(img, 90)
            self.frames.append(img)

        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.image.blit(self.frames[self.frame], (0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def update(self):
        if (self.rect.bottom < 0 or self.frame >= self.max_frames - 1):
            self.kill()
            return
        
        else:
            self.frame += self.anim_speed

        self.next_frame()
        self.rect = self.rect.move(0, -self.mov_dist)

    def clear_surface(self):
        clear = pygame.Color(0, 0, 0, 0)
        self.image.fill(clear)
    
    def next_frame(self):
        self.clear_surface()
        self.image.blit(self.frames[int(self.frame)], (0, 0))


