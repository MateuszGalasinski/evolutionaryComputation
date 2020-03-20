from numpy import exp,array,zeros
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from pso.fitness.fitness import fitness
import k3d

def plot_particles(particles):
    if len(particles) == 0:
        print("No particles to visualize !")
        return
    if len(particles[0].position) != 2:
        print("I can only visualize three dimensional function !")
        return
    # points[len(particles[0].position), len(particles[0].position), len(particles[0].position)]
    # 
    x = random.randn(1000,3).astype(float32)x = list(map(lambda p: (p.position[0], p.position[1], fitness(p.position)), particles)) #arange(-3.0,3.0,0.1)
    print(x)
    # y = list(map(lambda p: p.position[1], particles)) #arange(-3.0,3.0,0.1)
    # X,Y = meshgrid(x, y) # grid of point
    # Z = map(lambda p: fitness(p.position), particles) # evaluation of the function on the grid
    point_size = 0.2
    plot = k3d.plot(name='points')
    plt_points = k3d.points(positions=x, point_size=0.2)
    plot += plt_points
    plt_points.shader='3d'
    plot.display()
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # # surf = ax.scatter(X, Y, Z, rstride=1, cstride=1, 
    # ax.scatter(x, y, Z)

    # # ax.zaxis.set_major_locator(LinearLocator(10))
    # # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # # fig.colorbar(surf, shrink=0.5, aspect=5)
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')

    # plt.draw()
    # plt.pause(0.001)