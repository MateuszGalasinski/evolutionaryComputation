# from math import sin, cos
from numpy import sum, asarray_chkfinite, arange, prod, sqrt, cos, sin
from functools import reduce
from pso.config.config import configuration as cfg

if cfg.fitness == "sincos":
    def fitness(position):
        return sin(position[0]) + cos(position[1])
elif cfg.fitness == "2":
    def fitness(position):
        return reduce(lambda p,n: p + n**2, position)
elif cfg.fitness == "rosen":
    def fitness(position):
        return sum(100.0*(position[1:]-position[:-1]**2.0)**2.0 + (1-position[:-1])**2.0)
elif cfg.fitness == "griewank":
    def fitness(position, fr=4000):
        n = len(position)
        j = arange( 1., n+1 )
        s = sum( position**2 )
        p = prod( cos( position / sqrt(j) ))
        return s/fr - p + 1
elif cfg.fitness == "3":
    def fitness(position):
        sum = 0
        for x in range(1, len(position)):
            sum = sum + (position[x]-x)**2
        return sum