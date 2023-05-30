import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__()

        pos_x = pos_y = 0
        self.x, self.y = 0, 0
        self.ship_type = "corvette"
        self.width = self.height = 192


        if len(args) == 5:
            self.ship_type = args[0]
            self.width = args[1]
            self.height = args[2]
            pos_x = args[3]
            pos_y = args[4]
        
        elif len(args) == 2:
            pos_x = args[0]
            pos_y = args[1]

        self.set_moving()
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.set_alpha(255)
        self.image.blit(self.ship_img, (self.x, self.y, self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    '''
        Updates the image of the ship.
    '''
    def __update_img__(self):
        self.ship_img = pygame.image.load(f"resources/ships/{self.ship_type}/{self.action}")
    
    def set_idle(self):
        self.action = "Idle.png"
        self.__update_img__()
    
    def set_moving(self):
        self.action = "Move.png"
        self.__update_img__()
    
    def set_shooting(self):
        self.action = "Attack_1.png"
        self.__update_img__()
    
    def set_destroyed(self):
        self.action = "Destroyed.png"
        self.__update_img__()
    
    '''
        Jumps to the next image in the animation.
    '''
    def next_img(self):
        step = 192
        if (self.width >= self.ship_img.get_width()): #End of image animation
            self.x = 0
            self.width = step

            self.ship_img = pygame.transform.scale(self.ship_img, (90, 90))
            self.ship_img = pygame.transform.rotate(self.ship_img, 90)

            self.image.blit(self.ship_img, (self.x, self.y, self.width, self.height))
            return

        self.x += step
        self.width += step
        self.ship_img = pygame.transform.scale(self.ship_img, (90, 90))
        self.ship_img = pygame.transform.rotate(self.ship_img, 90)
        self.image.blit(self.ship_img, (self.x, self.y, self.width, self.height))
    
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
        self.next_img()
    
    def update_pos(self, pos_x, pos_y):
        self.rect.topleft = [pos_x, pos_y]

            
if __name__ == '__main__':
    pass




