#!/usr/bin/python

import sys
import pygame
import math
import geometry

from constants import *
from photon import *

def draw(p, scale, colour = white):
    pygame.draw.line(window, colour, p.r*scale, p.run_until_reflect(om).r*scale)
    
def drawpoint(point, scale, colour = white):
    pygame.draw.line(window, colour, list(x*scale for x in point), list(x*scale for x in point)) #pygame can't accept generator expressions

pygame.init()

window = pygame.display.set_mode((700, 500))
    
r = array([1,100])
v = array([.1,.1])

for (x,y) in reflection_map:
    drawpoint((x,y), 0.5, (0,0,255))

for (x,y) in refraction_map:
    if refraction_map[x,y][1] != 1.0:
        drawpoint((x,y), 0.5, (0,0,255))
    
for (x,y) in refraction_map:
    if refraction_map[x,y][0] != (0,0):
        drawpoint((x,y), 0.5, (0,255,0))
    
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            p = photon(r,v,1.0,None)
            colour = white
            while True:
                draw(p,0.5,colour)
                pygame.display.flip()

