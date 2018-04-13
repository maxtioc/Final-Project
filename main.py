#basic tank fighting game
#base code for movement and image generation is taken and based on crash course alien invasion
#week 1: generated two tanks on the screen that can each move
#week 2: created specific bounds for each tank
#week 3: created a better tank that will have an independent turret that can rotate (that will be week 4 goal)
#week 3 continued: now able to toggle between which tank is controlled by pressing the space key
import pygame
import os
import sys
import gameFunctions as gf 
from settings import Settings
from tank import Tank
from tank import Tank2

#set up the basic python window; from textbook
def runGame():
    #initialize the game and create a screen object
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption("Tank Battle")
    
    #make the tank
    tank = Tank(screen)
    tank2 = Tank2(screen)
    #start the main game loop
    Running = True

    while Running == True:
        #watch for keyboard and mouse events
        #redraw the screen during each pass through the loop
        gf.updateScreen(aiSettings, screen, tank, tank2)
        gf.checkEvents(tank)
        gf.checkEvents(tank2)
        tank.update()
        tank2.update()
        # if fight == True:
        #     print(fight)
        #     gf.checkEvents(tank)
        #     tank.update()
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_SPACE:
        #     #             fight = False
        # elif fight == False:
        #     gf.checkEvents(tank2)
        #     tank2.update()
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_SPACE:
            #             fight = True

runGame()