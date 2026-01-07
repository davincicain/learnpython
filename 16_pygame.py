"""
install: pip install pygame-ce
"""

import pygame
import sys
import time
from pygame.locals import * #detect events

def main():
    #create a new window
    screen_1=pygame.display.set_mode((500,500))

    #read the materials
    img_1=pygame.image.load("starry_sky_1.jpg")
    img_2=pygame.image.load("airplane_1.jpg")

    x_axis_position=0
    y_axis_position=200
    direction='right'

    while True:

        #add objects to the screen
        screen_1.blit(img_1,(0,0))
        screen_1.blit(img_2,(x_axis_position,y_axis_position)) #The origin is at the upper left corner of the screen and moving right or down is considered positive

        #refresh window: display all objects
        pygame.display.update()

        #judge the direction
        if x_axis_position<=0:
            direction='right'
        if x_axis_position>=400:
            direction='left'

        #move
        if direction=='right':
            x_axis_position=x_axis_position+10
        else:
            x_axis_position=x_axis_position-10

        time.sleep(0.1)

        #exit
        for event in pygame.event.get(): #get all user event
            if event.type==QUIT:
                sys.exit()

if __name__ == '__main__':
    main()