import math
from numpy import array, dot, cross

"""

(0,0) -----> x
|
|
|
|
v

y

+ theta = clockwise


"""

def norm(n):      #euclidean norm
    return math.sqrt(dot(n,n))

def unit(n):      #unit vector
    return n / norm(n)

def reflect(v,n):   #actually reflects and inverts
    print math.atan(v[1]/v[0])
    u = unit(n)
    return v - 2*dot(v,u)*u
    
def rotate(v,dh):
    r = norm(v)
    h = math.atan2(v[1], v[0])
    h = h + dh
    
    return r * array([math.cos(h), math.sin(h)])

def refract(v, normal, n, np):
    cp = cross(unit(v), unit(normal))
    dp = dot(unit(v), unit(normal))
    theta = math.acos(abs(dp))
    thetap = math.asin(n * math.sin(theta) / np)
    if abs(theta-thetap) > 1e-9:
        print theta, thetap, dp, cp
    if dp > 0 and cp > 0:
        return rotate(v, theta-thetap)
    if dp > 0 and cp < 0:
        return rotate(v, thetap-theta)
    if dp < 0 and cp > 0:
        return rotate(v, thetap-theta)
    if dp < 0 and cp < 0:
        return rotate(v, theta-thetap)



class photon:
    def __init__(self, r, v, n, last_hit):
        self.r = r
        self.v = v
        self.last_hit = last_hit
        self.n = n
    def __repr__(self):
        return str(self.r) + str(self.v) + str(self.last_hit)
    def run_once_and_reflect(self, om):
        x = round(self.r[0])
        y = round(self.r[1])
        lm = om.reflection_map
        rm = om.refraction_map
        if ((x,y) in om and self.last_hit != (x,y)):
            if (x,y) in lm:
                self.v = reflect(self.v, array(lm[x,y]))
                self.last_hit = (x,y)
            if (x,y) in rm:
                self.v = refract(self.v, array(rm[x,y][0]), self.n, rm[x,y][1])
                self.last_hit = (x,y)
        self.r = self.r + self.v
        if (x,y) in rm:
            self.n = rm[x,y][1]
    def run_until_reflect(self,om):
        l = self.last_hit
        while (self.last_hit == l):
            self.run_once_and_reflect(om)
        return self
