import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship_type, bullet_type, pos):
        super().__init__()

        size = 25
        self.mov_dist = 8

        path = f"resources/ships/{ship_type}/Charge_{bullet_type}.png"

        self.bullet_img = pygame.image.load(path)
        self.bullet_img = pygame.transform.scale(self.bullet_img, (size, size))
        self.bullet_img = pygame.transform.rotate(self.bullet_img, 90)



        self.image = pygame.Surface((80, size), pygame.SRCALPHA)
        # self.image = pygame.Surface((80, size))
        # self.image.fill((0, 255, 0))
        self.image.blit(self.bullet_img, (0, 0))
        self.image.blit(self.bullet_img, (0.75 * 80, 0))

        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def update(self):
        if (self.rect.bottom < 0):
            self.kill()

        self.rect = self.rect.move(0, -self.mov_dist)


