from math import sin, cos

def fitness(position):
    return sin(position[0]) + cos(position[1])