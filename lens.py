#!/usr/bin/python

import sys
import pygame
import math
import geometry

from constants import *
from photon import *

scale = 1

def draw(p, colour = white):
    pygame.draw.line(window, colour, p.r*scale, p.run_once_and_reflect(om).r*scale)
    
def drawpoint(point, colour = white):
    pygame.draw.line(window, colour, list(x*scale for x in point), list(x*scale for x in point)) #pygame can't accept generator expressions

pygame.init()

window = pygame.display.set_mode((700, 500))
    
r1 = array([1,70])
r2 = array([1,71])
v = array([.1,0])

for (x,y) in reflection_map:
    drawpoint((x,y), (0,0,255))

for (x,y) in refraction_map:
    if refraction_map[x,y][1] != 1.0:
        drawpoint((x,y), (0,0,255))
    
for (x,y) in refraction_map:
    if refraction_map[x,y][0] != (0,0):
        drawpoint((x,y), (0,255,0))
    
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            p1 = photon(r1,v,1.0,None)
            p2 = photon(r2,v,1.0,None)
            colour = white
            while True:
                draw(p1,colour)
                #draw(p2,colour)
                pygame.display.flip()
