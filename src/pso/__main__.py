from pso.config.config import configuration
from pso.models.particle import Particle
from pso.models.space import Space
from pso.plots.particles_plot import plot_particles
from pso.config.config import configuration as cfg
from pso.genetic.genetic import genetic
import numpy as np

class App():
    def run(self):
        if(cfg.algorithmType == "pso"):
            search_space = Space(1)
            particles_vector = [Particle() for _ in range(configuration.n_particles)]
            search_space.particles = particles_vector
            plot_particles(search_space.particles)
            # search_space.print_particles()
            iteration = 0
            while iteration < configuration.iterations:
                search_space.set_pbest()
                search_space.set_gbest()

                if abs(search_space.gbest_value - search_space.target) <= configuration.target_error:
                    break

                search_space.move_particles()
                iteration += 1
            print("The best solution is: ", search_space.gbest_position, " in n_iterations: ", iteration)
            plot_particles(search_space.particles)
        elif(cfg.algorithmType == "ga"):
            genetic()

        else:
            print(f"Unknown algorithm type: {cfg.algorithmType}")
        input("Press Enter to exit...")

if __name__ == '__main__':
    np.set_printoptions(precision=2, floatmode='fixed', sign=' ', )
    App().run()
