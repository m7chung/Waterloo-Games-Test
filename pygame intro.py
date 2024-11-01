# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:45:29 2024

@author: msmad, cvanderz
"""
import pygame
#need to import so exit is supported --> doesn't run error
from sys import exit

#STARTING VARIABLES -----------------------------------------------------------------------------
pygame.init()
#gathers the users screen size
infoObject = pygame.display.Info()
#establishes the size of the game (display screen)
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption('The Waterloo Games')
clock = pygame.time.Clock()
#Font(font type,font size)
test_font = pygame.font.Font('cmtt10.ttf', 50)


#SURFACES------------------------------------------------------------------------------
#sizes are always (width,height)
ANANA_surf = pygame.image.load('ANANA.png').convert_alpha()
#test_surf = pygame.Surface((100,200))
#test_surf.fill('cadetblue3')
cursedcat_surf = pygame.image.load('cursed cat.JPG').convert_alpha()
# render(text_surf, anti-aliase, color)
score_surf = test_font.render('Baddies', False, (0,255,0))
score_rect = score_surf.get_rect(center = (500, 50))

bibble_surf = pygame.image.load('bibble.png').convert_alpha()
bibble_rect = bibble_surf.get_rect(bottomright = (2000,750))

#go to the-image-editor.com/image/resize to change the dimension of a image if too large
tikka_surf = pygame.image.load('tikka.JPG').convert_alpha()
#Rect(left,top,width,height) --> rectangle in same place as tikka
tikka_rect = tikka_surf.get_rect(bottomright = (200,400))
tikka_gravity = 0

you_lost_surf = pygame.image.load('bibble_got_you.jpg').convert_alpha()
you_lost_rect = you_lost_surf.get_rect(center=(500, 400))

#bibble_rect = bibble_surf.get_rect(midtop = (bibble_x_pos,500))


#EVENT LOOP-------------------------------------------------------------------------------------
#the loop that keeps the screen open --> need quit function so that you can exit the loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and tikka_rect.bottom >= 750:
                tikka_gravity = -15
                

                
#MOUSE MOTION or MOUSEUP / MOUSEDOWN to detect when mouse button clicked(down)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tikka_rect.collidepoint(event.pos) and tikka_rect.bottom >= 750:
                tikka_gravity =-5
#blit = block image transfer --> put on surface on another surface --> (200,100) means we want our display surface 200 from left 100 from top
 # Fill the screen with a background color or image
    screen.fill((0, 0, 0))  # Fill the screen with black color, alternatively you can blit a background image
    
    screen.blit(ANANA_surf,(0,0))
    screen.blit(cursedcat_surf,(600,200))
    pygame.draw.rect(screen,"Pink", score_rect,10)
    pygame.draw.rect(screen,"Pink", score_rect,)
    screen.blit(score_surf, score_rect)
    #bibble will move 60 pixels per second
   
    pygame.draw.line(screen,"Silver",(0,0),pygame.mouse.get_pos(),10)
    pygame.draw.ellipse(screen,'Turquoise',pygame.Rect(50,400,100,100))
    
    bibble_rect.x -= 12  
    if bibble_rect.right <= 0:
        bibble_rect.left = 1000
    
    screen.blit(bibble_surf,(bibble_rect))
    
    tikka_gravity += 0.4
    tikka_rect.y += tikka_gravity
    if tikka_rect.bottom >= 750:
        tikka_rect.bottom = 750
        
    if tikka_rect.top <= 50:
        tikka_rect.top = 50
    screen.blit(tikka_surf,tikka_rect)
    
    
#    keys = pygame.key.get_pressed() 
#    if keys[pygame.K_SPACE]:
#        print('jump')



#COLLISION --------------------------------------------------

    if bibble_rect.colliderect(tikka_rect):
       # pygame.quit()
       # exit()
        screen.blit(you_lost_surf, you_lost_rect)
        pygame.display.update()
        pygame.time.wait(2000)  # Wait for 2 seconds before closing
        pygame.quit()
        exit()
        
    


# draw all our elements
# update everything
    pygame.display.update()
# sets our frame rate --> should not run faster than 60 frames per second
    clock.tick(60)
    
#if tikka_rect.colliderect(bibble_rect):
    
#mouse_pos = pygame.mouse.get_pos()
#if tikka_rect.collidepoint(mouse_pos):
#    pygame.mouse.get_pressed()
