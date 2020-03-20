from pso.config.config import configuration as cfg
from pso.fitness.fitness import fitness
import numpy as np 
from random import random

class Space():
    def __init__(self, target):
        self.target = target
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([x * random()*cfg.d_max for x in range(cfg.arguments_dimensions)])

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate:float = fitness(particle.position)
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position
            

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = fitness(particle.position)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for particle in self.particles:
            new_velocity = (cfg.w*particle.velocity) + (cfg.c1*random()) * (particle.pbest_position - particle.position) + \
                            (random()*cfg.c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
