import sys
import pygame

global fight
fight = False

def checkEvents(tank):
    #respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, tank)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, tank)
def checkKeydownEvents(event, tank):
    #respond to keypresses
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        tank.moving_right = True
    elif event.key == pygame.K_LEFT:
        tank.moving_left =  True
    elif event.type == pygame.K_SPACE:
        fight = False
    elif event.type == pygame.K_f:
        fight = True
def checkKeyupEvents(event, tank):
    #respond to key releases
    if event.key == pygame.K_RIGHT:
        tank.moving_right = False
    elif event.key == pygame.K_LEFT:
        tank.moving_left = False
def updateScreen(aiSettings, screen, tank, tank2):
    #update images on screen and flip to new screen
    screen.fill(aiSettings.bgColor)
    tank.blitMe()
    tank2.blitMe()
    #make the screen visible
    pygame.display.flip()

