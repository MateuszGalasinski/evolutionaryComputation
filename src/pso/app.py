class App():

    def __init__(self):
        self.w = 0.5
        self.c1 = 0.8
        self.c2 = 0.9
        self.n_iterations = 100
        self.target_error = 1e-8
        self.n_particles = 50

    def console_read_parameters(self):
        self.n_iterations = int(input("Number of iterations: "))
        self.target_error = float(input("Target error: "))
        self.n_particles = int(input("Number of particles: "))

    def run(self):
        search_space = Space(1, target_error, n_particles)
        particles_vector = [Particle() for _ in range(search_space.n_particles)]
        search_space.particles = particles_vector
        search_space.print_particles()
        iteration = 0
        while(iteration < n_iterations):
            search_space.set_pbest()    
            search_space.set_gbest()

            if(abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
                break

            search_space.move_particles()
            iteration += 1
        print("The best solution is: ", search_space.gbest_position, " in n_iterations: ", iteration)