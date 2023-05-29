import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_type="corvette", width=192, height=192):
        super().__init__()
        self.x, self.y = 0, 0
        self.set_idle()


        self.ship_img = self.__get_img__(ship_type)
        
        self.image = pygame.Surface((height, height))
        self.image.blit(self.ship_img, (self.x, self.y, width, height))
        self.resize_img(width, height)

        self.rect = self.image.get_rect()


    def __get_img__(self, ship_type):
        return pygame.image.load(f"resources/ships/{ship_type}/{self.action}")
    
    def set_idle(self):
        self.action = "Idle.png"
    
    def set_moving(self):
        self.action == "Move.png"
    
    def set_shooting(self):
        self.action = "Attack_1.png"
    
    def set_destroyed(self):
        self.action = "Destroyed.png"
    
    '''
        Scales the image to the desired size.
    '''
    def resize_img(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
    
    def update(self):
        pass

            




