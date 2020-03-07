from pso.config.config import configuration
from pso.fitness.fitness import fitness
import numpy as np 
import random

class Space():
    def __init__(self, target):
        self.target = target
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random()*10, random.random()*10])

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = fitness(particle)
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position
            

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for particle in self.particles:
            new_velocity = (configuration.w*particle.velocity) + (configuration.c1*random.random()) * (particle.pbest_position - particle.position) + \
                            (random.random()*configuration.c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
