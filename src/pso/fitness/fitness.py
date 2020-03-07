from math import sin, cos

def fitness(particle):
    return sin(particle.position[0]) + cos(particle.position[1])