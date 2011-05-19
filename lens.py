#!/usr/bin/python

import sys
import pygame
import math
import geometry

from constants import *
from photon import *

scale = 1

def draw(p, om, colour = white):
    pygame.draw.line(window, colour, p.r*scale, p.run_until_reflect(om).r*scale)
    
def drawpoint(point, colour = white):
    pygame.draw.line(window, colour, list(x*scale for x in point), list(x*scale for x in point)) #pygame can't accept generator expressions

pygame.init()

window = pygame.display.set_mode((700, 500))
    
r1 = array([1,70])
r2 = array([1,71])
v = array([.1,.1])
        
center = (120, 100)

while True:
    
    r1[0] = r1[0] + 1

    refraction_map.clear()
    print "filling"
    make_prism(refraction_map)
    om.fill(geometry.circle(center,50), 1.5)
    om.fill(geometry.circle(center,51), 1.0)
    window.fill((0,0,0))
    print "drawing"
    for (x,y) in reflection_map:
        drawpoint((x,y), (0,0,255))

    for (x,y) in refraction_map:
        if refraction_map[x,y][1] == 1.0:
            drawpoint((x,y), (0,255,255))
        else:
            drawpoint((x,y), (0,255,0))
        if refraction_map[x,y][0] == (0,0):
            drawpoint((x,y), (255,0,0))
    print "rendering"        
    p1 = photon(r1,v,1.0,None)
    for i in range(20):
        draw(p1,om,white)
    print "done"
    
    pygame.display.flip()
