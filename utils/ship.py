import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, ship_type, size, pos_x, pos_y):
        super().__init__()

        self.x, self.y = 0, 0
        self.SHIP_TYPE = ship_type
        self.SIZE = size
        self.max_frames = 0
        self.frame = 0
        self.anim_speed = 0.25
        self.shot = False
        self.mov_dist = 15

        self.set_moving()
        
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.next_frame()

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def get_type(self):
        return self.SHIP_TYPE

    '''
        Updates the image of the ship and scales it to appropriate size.  '''
    def __update_img__(self):
        self.ship_img = pygame.image.load(f"resources/ships/{self.SHIP_TYPE}/{self.action}")

        frames = self.ship_img.get_width() / 192
        img_width = frames * self.SIZE

        self.max_frames = frames

        self.ship_img = pygame.transform.scale(self.ship_img, (img_width, self.SIZE))
        self.ship_img = pygame.transform.rotate(self.ship_img, 90)
    
    def set_moving(self):
        self.action = "Move.png"
        self.__update_img__()
        self.frame = 0
    
    def set_shooting(self):
        self.action = "Attack_1.png"
        self.__update_img__()
        self.frame = 0
    
    def set_destroyed(self):
        self.action = "Destroyed.png"
        self.__update_img__()
        self.frame = 0
    
    '''
        Jumps to the next image in the animation.
    '''
    def next_frame(self):
        start_y = self.SIZE * int(self.frame)
        end_y = self.SIZE * (int(self.frame) + 1)

        start_x = 0
        end_x = self.SIZE

        self.image.blit(self.ship_img, (0, 0), (start_x, start_y, end_x, end_y))
    
    def update(self):
        if (self.frame >= self.max_frames - 1):
            self.frame = 0
            self.clear_surface()

            if (self.shot):
                self.shot = False
                self.set_moving()

        else:
            self.frame += self.anim_speed

        self.next_frame()
    
    def clear_surface(self):
        clear = pygame.Color(0, 0, 0, 0)
        self.image.fill(clear)
        
    def shoot(self):
        self.shot = True
        self.set_shooting()
    
    def move_left(self):
        self.rect = self.rect.move(-self.mov_dist, 0)

    def move_right(self):
        self.rect = self.rect.move(self.mov_dist, 0)
    
    def move_up(self):
        self.rect = self.rect.move(0, -self.mov_dist)

    def move_down(self):
        self.rect = self.rect.move(0, self.mov_dist)
    
    def get_top(self):
        return (self.rect.centerx, self.rect.top)

            
if __name__ == '__main__':
    pass




