import pygame
from pygame.sprite import Sprite

class Tank():
    def __init__(self, screen):
        #initialize the tank and its starting position
        super().__init__()
        self.screen = screen
       
        #load the ship and get its rect
        self.image = pygame.image.load("Final Project/Images/tank1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start the tank at the bottom center each time
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #movement flag
        self.moving_right = False
        self.moving_left = False




    def update(self):
        #update tank postion based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.centerx:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1


    def blitMe(self):
        #draw the tank at its current location
        self.screen.blit(self.image, self.rect)

#create the second tank
class Tank2():
    def __init__(self, screen):
        #initialize the tank and its starting position
        self.screen = screen
       
        #load the ship and get its rect
        self.image = pygame.image.load('Final Project/Images/tank2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start the tank at the bottom center each time
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update tank postion based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > self.screen_rect.centerx:
            self.rect.centerx -= 1



    def blitMe(self):
        #draw the tank at its current location
        self.screen.blit(self.image, self.rect)