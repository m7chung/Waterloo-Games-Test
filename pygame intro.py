# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:45:29 2024

@author: msmad
"""

import pygame
#need to iimport so exit is supported --> doesn't run error
from sys import exit

pygame.init()
#establishes the size of the game (display screen)
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('The Waterloo Games')
clock = pygame.time.Clock()

#sizes are always (width,height)
ANANA_surface = pygame.image.load('Downloads/Waterloo 1A/ANANA.png')
#test_surface = pygame.Surface((100,200))
#test_surface.fill('cadetblue3')

cursedcat_surface = pygame.image.load('Downloads/Waterloo 1A/cursed cat.JPG')

#the loop that keeps the screen open --> need quit function so that you can exit the loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#blit = block image transfer --> put on surface on another surface --> (200,100) means we want our display surface 200 from left 100 from top
    screen.blit(ANANA_surface,(0,0))
    screen.blit(cursedcat_surface,(600,200))
# draw all our elements
# update everything
    pygame.display.update()
# sets our frame rate --> should not run faster than 60 frames per second
    clock.tick(60)
#can you see this comment
