import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__()
        self.x, self.y = 0, 0
        self.set_moving()

        ship_type = "corvette"
        self.width = self.height = 192
        pos_x = pos_y = 0

        if len(args) == 5:
            ship_type = args[0]
            self.width = args[1]
            self.height = args[2]
            pos_x = args[3]
            pos_y = args[4]
        
        elif len(args) == 2:
            pos_x = args[0]
            pos_y = args[1]

        self.ship_img = self.__get_img__(ship_type)
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.set_alpha(255)
        self.image.blit(self.ship_img, (self.x, self.y, self.width, self.height))

        self.rect = self.ship_img.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def __get_img__(self, ship_type):
        return pygame.image.load(f"resources/ships/{ship_type}/{self.action}")
    
    def set_idle(self):
        self.action = "Idle.png"
    
    def set_moving(self):
        self.action = "Move.png"
    
    def set_shooting(self):
        self.action = "Attack_1.png"
    
    def set_destroyed(self):
        self.action = "Destroyed.png"
    
    def next_img(self):
        if (self.x + self.width >= self.ship_img.get_width()):
            self.x = 0
            return

        self.x += self.width
    
    '''
        Scales the image to the desired size.
    '''
    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
    
    '''
        Rotate the image by the specified angle.
    '''
    def rotate(self, degrees):
        self.image = pygame.transform.rotate(self.image, degrees)
    
    def update(self):
        pass

            
if __name__ == '__main__':
    pass




