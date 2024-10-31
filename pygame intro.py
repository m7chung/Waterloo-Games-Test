# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:45:29 2024

@author: msmad
"""

import pygame
#need to import so exit is supported --> doesn't run error
from sys import exit

#STARTING VARIABLES -----------------------------------------------------------------------------
pygame.init()
#gathers the users screen size
infoObject = pygame.display.Info()
#establishes the size of the game (display screen)
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('The Waterloo Games')
clock = pygame.time.Clock()
#Font(font type,font size)
test_font = pygame.font.Font('cmtt10.ttf', 50)


#SURFACES------------------------------------------------------------------------------
#sizes are always (width,height)
ANANA_surface = pygame.image.load('ANANA.png')
#test_surface = pygame.Surface((100,200))
#test_surface.fill('cadetblue3')
cursedcat_surface = pygame.image.load('cursed cat.JPG')
# render(text_surface, anti-aliase, color)
text_surface = test_font.render('Baddies', False, 'chartreuse1')

bibble_surface = pygame.image.load('bibble.png')
bibble_x_pos = 600
#the loop that keeps the screen open --> need quit function so that you can exit the loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#blit = block image transfer --> put on surface on another surface --> (200,100) means we want our display surface 200 from left 100 from top
    screen.blit(ANANA_surface,(0,0))
    screen.blit(cursedcat_surface,(600,200))
    screen.blit(text_surface,(300,50))
    #bibble will move 60 pixels per second

    bibble_x_pos -= 40
    if bibble_x_pos < -100:
        bibble_x_pos = 800
    screen.blit(bibble_surface,(bibble_x_pos,450))
# draw all our elements
# update everything
    pygame.display.update()
# sets our frame rate --> should not run faster than 60 frames per second
    clock.tick(60)
