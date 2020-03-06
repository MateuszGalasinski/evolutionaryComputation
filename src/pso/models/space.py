import numpy as np 
import random
from math import sin, cos

class Space():
    def __init__(self, target, target_error, n_particles):
        self.w = 0.5
        self.c1 = 0.55
        self.c2 = 0.7
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random()*10, random.random()*10])

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()
   
    def fitness(self, particle):
        return sin(particle.position[0]) + cos(particle.position[1])

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position
            

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for particle in self.particles:
            new_velocity = (self.w*particle.velocity) + (self.c1*random.random()) * (particle.pbest_position - particle.position) + \
                            (random.random()*self.c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
