import geometry

white = (255,255,255)
origin = (0,0)

class optical_map:
    def __init__(self, reflection_map, refraction_map):
        self.reflection_map = reflection_map
        self.refraction_map = refraction_map
    def __contains__(self, coord):
        if coord in self.reflection_map:
            return True
        if coord in refraction_map and (refraction_map[coord][0] != (0,0)):
            return True
    def fill(self, points, n):
        for ((x,y),normal) in points:
            self.refraction_map[round(x),round(y)] = (normal,n)
    def fill_no_normal(self, points, n):
        for((x,y),normal) in points:
            self.refraction_map[round(x),round(y)] = ((0,0),n)

reflection_map = {}
for i in range(0,640):
    reflection_map[i,0] =(0,-1)
    reflection_map[i,480] = (0,1)
for i in range(0,480):
    reflection_map[0,i] = (1,0)
    reflection_map[640,i] = (-1,0)
reflection_map[0,0] = (1,1)
reflection_map[0,480] = (1,-1)
reflection_map[640,0] = (-1,1)
reflection_map[640,480] = (-1,-1)

refraction_map = {}
def make_prism(rm):
    for i in range(0,640):
        rm[i,199] = ((0,1), 1.0)
        rm[i,200] = ((0,1), 1.5)
        rm[i,299] = ((0,1), 1.5)
        rm[i,300] = ((0,1), 1.0)


om = optical_map(reflection_map, refraction_map)
