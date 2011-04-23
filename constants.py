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
        if coord in refraction_map and refraction_map[coord][0]:
            return True

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
for i in range(0,640):
    for j in range(0,200):
        refraction_map[i,j] = ((0,0), 1.0)   
    for j in range(200,300):
        refraction_map[i,j] = ((0,0), 1.5)
    refraction_map[i,199] = ((0,1), 1.0)
    refraction_map[i,200] = ((0,1), 1.5)
    refraction_map[i,299] = ((0,1), 1.5)
    refraction_map[i,300] = ((0,1), 1.0)

"""        
for radius in range(1,50):    
    for ((x,y),n) in geometry.circle((120,100), radius):
        refraction_map[round(x),round(y)] = ((0,1),1.5)

for ((x,y),n) in geometry.circle((120,100), 50):
    refraction_map[round(x),round(y)] = ((0,1),1.5)
"""        
om = optical_map(reflection_map, refraction_map)
