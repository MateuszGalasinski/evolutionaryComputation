from pathlib import Path

class Config(object):
    def __init__(self, w, c1, c2, iterations, target_error, n_particles, d_min, d_max):
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.iterations = iterations
        self.target_error = target_error
        self.n_particles = n_particles
        self.d_min = d_min
        self.d_max = d_max
import json

def as_config(dct):
    return Config(
        dct['w'],
        dct['c1'],
        dct['c2'],
        dct['iterations'], 
        dct['target_error'], 
        dct['n_particles'],
        dct['d_min'], 
        dct['d_max']
        )

configuration = json.loads(Path("configuration.json").read_text(), object_hook = as_config)