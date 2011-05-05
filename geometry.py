import math

def line(start, end):
    (x0,y0) = start
    (x1,y1) = end
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0 = y0, x0  
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    if y0 < y1: 
        ystep = 1
    else:
        ystep = -1

    deltax = x1 - x0
    deltay = abs(y1 - y0)
    error = -deltax / 2
    y = y0

    for x in range(x0, x1 + 1): # We add 1 to x1 so that the range includes x1
        if steep:
            yield(y,x)
        else:
            yield(x,y)
            
        error = error + deltay
        if error > 0:
            y = y + ystep
            error = error - deltax
            
def circle(center, r):
    (x,y) = center
    dtheta = 0.1/r
    theta = 0
    while theta < 2*math.pi:
        yield((x+r*math.cos(theta), y+r*math.sin(theta)), (math.cos(theta), math.sin(theta)))
        theta += dtheta
