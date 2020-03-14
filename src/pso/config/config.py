from pathlib import Path

class Config(object):
    def __init__(self, algorithmType, w, c1, c2, iterations, target_error, n_particles, arguments_dimensions, d_min, d_max):
        self.algorithmType = algorithmType
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.iterations = iterations
        self.target_error = target_error
        self.n_particles = n_particles
        self.arguments_dimensions = arguments_dimensions
        self.d_min = d_min
        self.d_max = d_max
import json

def as_config(dct):
    return Config(
        dct['algorithmType'],
        dct['w'],
        dct['c1'],
        dct['c2'],
        dct['iterations'], 
        dct['target_error'], 
        dct['n_particles'],
        dct['arguments_dimensions'],
        dct['d_min'], 
        dct['d_max']
        )

configuration = json.loads(Path("configuration.json").read_text(), object_hook = as_config)