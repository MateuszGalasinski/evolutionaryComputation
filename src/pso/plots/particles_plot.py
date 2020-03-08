from numpy import exp,array
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from pso.fitness.fitness import fitness
 
def plot_particles(particles):        
    x = list(map(lambda p: p.position[0], particles)) #arange(-3.0,3.0,0.1)
    y = list(map(lambda p: p.position[1], particles)) #arange(-3.0,3.0,0.1)
    # X,Y = meshgrid(x, y) # grid of point
    Z = list(map(lambda p: fitness(p), particles)) # evaluation of the function on the grid
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # surf = ax.scatter(X, Y, Z, rstride=1, cstride=1, 
    ax.scatter(x, y, Z)

    # ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.draw()
    plt.pause(0.001)