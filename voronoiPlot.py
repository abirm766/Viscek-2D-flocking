### Module Import Section ###
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import imageio
import os
#############################

paraMeters = []
with open('data.txt','r') as file:
  for j, line in enumerate(file):
    if j == 1:
      paraMeters=line.strip().split(" ")
    
n_particles = eval(paraMeters[0])   # total no. of particles
box_width = eval(paraMeters[1])     # edge length of the simulation cell
n_steps = eval(paraMeters[2])       # number of iterating steps
dt = eval(paraMeters[3])            # step length
eta = eval(paraMeters[4])           # noise range
vel = eval(paraMeters[5])           # absolute velocity/speed

filenames=[]
images = []

axrange = [0, box_width, 0, box_width]

for i in range(1, n_steps+2):
  plt.clf()
  step=i
  coord_x=[]
  coord_y=[]
  vel_x=[]
  vel_y=[]
  points_list = []
  lines=[]
  
  with open('data.txt','r') as file:
    for j, line in enumerate(file):
      if j in range(((step*n_particles)-n_particles)+3,(step*n_particles)+3):
        lines.append(line.strip())
  for line in lines:
    data = line.split(" ")
    points_list.append([eval(data[0]), eval(data[1])])
    coord_x.append(eval(data[0]))   # storing x coordinates
    coord_y.append(eval(data[1]))   # storing y coordinates
    vel_x.append(eval(data[2]))     # storing x velocity
    vel_y.append(eval(data[3]))     # storing y velocity
  
  
  points = np.array(points_list)
  vor = Voronoi(points)
  
  voronoi_plot_2d(vor, show_vertices=False)
  plt.axis(axrange)
  plt.title('Voronoi plot, $\eta=$'+str(eta)+'    step='+str(i).rjust(3,'0'))
  plt.tight_layout()
  plt.gca().set_aspect('equal', 'box')
  
  fname='frame_'+str(i).rjust(3,'0')+'.png'
  plt.savefig(fname)
  filenames.append(fname)   # saving plots at each time as a frame
  plt.close()

for filename in filenames:
    images.append(imageio.v3.imread(filename))
imageio.mimsave('simVoronoi.gif', images, duration=0.01)   # combining all frame to make gif
for filename in filenames:
    os.remove(filename)   # deletes the .png frames
