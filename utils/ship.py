import pygame
import json
import os

class _Thrusters(pygame.sprite.Sprite):
    '''
        Represents the thrusters component for the Ship sprite
    '''
    def __init__(self, colour,  size, pos, anim_speed):
        super().__init__()

        frames_path = f"resources/ships/{colour}/thrusters/"

        self.anim_speed = anim_speed
        self.frame = 0
        self.frames = []
        self.width, self.height = size

        frame_images = os.listdir(frames_path)
        frame_images.sort()
        
        for frame_img in frame_images:
            image = pygame.image.load(frames_path + frame_img)
            image = pygame.transform.scale(image, (self.width, self.height))

            self.frames.append(image)
        
        self.max_frames = len(self.frames)
        self.frame = 0

        self.image = self.frames[self.frame]

        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.top = pos[1]
    
    def update_frame(self):
        self.image = self.frames[int(self.frame)]
    
    def update(self):
        if self.frame >= self.max_frames - 1: 
            self.frame = 0
        
        else:
            self.frame += self.anim_speed

        self.update_frame()
    
    def update_pos(self, pos):
        self.rect.centerx = pos[0]
        self.rect.top = pos[1]

class Ship(pygame.sprite.Sprite):
    '''
        Represents a ship sprite.
    '''
    def __init__(self, colour, pos):
        super().__init__()

        self.colour = colour
        self.mov_dist = 15
        self.width, self.height = 80, 85
        self.animate = False

        self.init_bullet_params(colour)
        
        self.ship_body = pygame.image.load(f"resources/ships/ship.png")
        self.ship_body = pygame.transform.scale(self.ship_body, (self.width, self.height))

        self.image = self.ship_body

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.init_thrusters()
    
    '''Gets the required frames for the state of the ship'''
    def update_frames(self, state):
        path = f"resources/ships/{self.colour}/{state}/"
        frame_images = os.listdir(path)
        frame_images.sort()

        self.frames = []

        for frame in frame_images:
            img = pygame.image.load(path+frame)
            img = pygame.transform.scale(img, (self.width, self.height))

            self.frames.append(img)
        
        self.max_frames = len(self.frames)
        self.frame = 0
    
    '''Initialises thrusters for this ship colour'''
    def init_thrusters(self):
        thrust_size = (self.width / 2 - 5, 25)
        thrust_anim_speed = 0.15
        thrust_pos = self.get_thrust_pos()

        self.thrusters = _Thrusters(self.colour, 
                                    thrust_size,
                                    thrust_pos,
                                    thrust_anim_speed)

    def get_thrusters(self):
        return self.thrusters 
    
    '''Returns the ship colour'''
    def get_colour(self):
        return self.colour

    '''Sets the ship body to default'''
    def set_idle(self):
        self.frame = 0
        self.image = self.ship_body
        self.animate = False

    '''Start shoot animation'''
    def shoot(self): 
        self.update_frames("shoot")
        self.frame = 0
        self.anim_speed = 1 #Increase animation speed
        self.animate = True
        self.shot = True
    
    '''Start explode animation'''
    def explode(self):
        #TODO
        pass
    
    '''Updates ship frame'''
    def update_frame(self):
        self.image = self.frames[int(self.frame)]

    def update(self):
        if self.animate:
            if (self.frame >= self.max_frames - 1):
                self.frame = 0

                if (self.shot):
                    self.shot = False
                    self.set_idle()
                    return

            else:
                self.frame += self.anim_speed

            self.update_frame()

    '''Gets the position for the thrusters relative to the ship position'''
    def get_thrust_pos(self):
        return (self.rect.centerx, self.rect.bottom - 5)
    
    '''Ship moves left by a factor of mov_dist'''
    def move_left(self):
        self.rect = self.rect.move(-self.mov_dist, 0)
        self.thrusters.update_pos(self.get_thrust_pos())

    '''Ship moves right by a factor of mov_dist'''
    def move_right(self):
        self.rect = self.rect.move(self.mov_dist, 0)
        self.thrusters.update_pos(self.get_thrust_pos())
    
    '''Ship moves up by a factor of mov_dist'''
    def move_up(self):
        self.rect = self.rect.move(0, -self.mov_dist)
        self.thrusters.update_pos(self.get_thrust_pos())

    '''Ship moves down by a factor of mov_dist'''
    def move_down(self):
        self.rect = self.rect.move(0, self.mov_dist)
        self.thrusters.update_pos(self.get_thrust_pos())
    
    '''Gets the cordinates for the top of this ship'''
    def get_top(self):
        return (self.rect.centerx, self.rect.top)
    
    '''Returns the bullet type for this ship'''
    def get_bullet_type(self):
        return self.bullet_type
    
    '''Returns the bullet size of this ship'''
    def get_bullet_size(self):
        return self.bullet_size
    
    '''Initialises bullet parameters for ship colour'''
    def init_bullet_params(self, ship_type):
        try:
            with open(f"resources/ships/{ship_type}/params.json") as file:
                params = json.load(file)
            
            self.bullet_type = params["bullet_type"]
            self.bullet_size = params["bullet_size"]

        except (FileNotFoundError):
            print(f"No parameters found for ship {ship_type}")
            exit(-1)
            