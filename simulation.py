### Module Import Section ###
import numpy as np
from math import sin, cos, atan2, pi, floor
import matplotlib.pyplot as plt
#############################


def get_initial_coordinates():
  """generates random positions 
  (x, y) for each particle"""
  x_coord = [np.random.random()*box_width for i in range(n_particles)]
  y_coord = [np.random.random()*box_width for i in range(n_particles)]
  
  return x_coord, y_coord


def get_initial_theta():
  """generates random directions 
  for velocities of each particle"""
  theta = [np.random.random()*360 for i in range(n_particles)]   # angle ranges from 0 to 360 (degree)
  return theta


def get_initial_velocities(theta):
  """generates velocites for each particle 
  corresponding to theta and given speed"""
  x_vel = [(vel*cos(i*pi/180)) for i in theta]
  y_vel = [(vel*sin(i*pi/180)) for i in theta]
  
  return x_vel, y_vel


def get_theta_avg(x, y, x_coord, y_coord, theta):
  """calculates avg. theta for each 
  particle and its surrounding unit radius"""
  circ = []
  for i, j, k in zip(x_coord, y_coord, theta):
    diff_x = x-i
    diff_y = y-j
    
    diff_x = diff_x-box_width*floor(diff_x/box_width)
    diff_y = diff_y-box_width*floor(diff_y/box_width)
    
    if (diff_x)**2+(diff_y)**2 < 1:
      circ.append(k*pi/180)

  avgtheta = (atan2(np.mean(np.sin(circ)), np.mean(np.cos(circ))))*180/pi
  
  if avgtheta < 0:
    return 360+avgtheta
  else:
    return avgtheta


def noise():
  """geneartes noise randomely 
  within the range (-eta/2, eta/2)"""
  nse = np.random.uniform(low = -eta/2, high = eta/2)

  return nse


def take_step(x_coord, y_coord, x_vel, y_vel, theta):
  """updates positions and velocites in each steps"""
  for i in range(n_particles):
    theta[i] = get_theta_avg(x_coord[i], y_coord[i], x_coord, y_coord, theta) + noise()   # updating theta according to the given expression
    x_vel[i] = vel*cos(theta[i]*pi/180)   # updating the direction of velocity
    y_vel[i] = vel*sin(theta[i]*pi/180)   # keeping speed constant
    x_coord[i] += x_vel[i]*dt   # updating x coordinate
    y_coord[i] += y_vel[i]*dt   # updating y coordinate
    
    # periodic boundary conditions
    x_coord[i] = x_coord[i]-box_width*floor(x_coord[i]/box_width)
    y_coord[i] = y_coord[i]-box_width*floor(y_coord[i]/box_width)
    
  return x_coord, y_coord, x_vel, y_vel, theta
    


# assigning values to varibles
n_particles = 300   # total no. of particles
box_width = 25     # edge length of the simulation cell
n_steps = 500     # number of iterating steps
dt = 1.0         # step length
eta = 0.1            # noise range
vel = 0.03          # absolute velocity/speed

x_coord, y_coord = get_initial_coordinates()

theta = get_initial_theta()

x_vel, y_vel = get_initial_velocities(theta)


# writing file header and 0th step
trajectory0 = ''
for x, y, v_x, v_y in zip(x_coord, y_coord, x_vel, y_vel):
  trajectory0 += f"{x} {y} {v_x} {v_y}" + '\n'
with open('data.txt', 'w') as file:
  file.write("n_particles box_width n_steps dt eta vel" + '\n')
  file.write(f"{n_particles} {box_width} {n_steps} {dt} {eta} {vel}" + '\n')
  file.write("x_coord y_coord x_vel y_vel" + '\n')
  file.write(trajectory0)


# for loop to iterate untill n_steps
for i in range(n_steps):

  trajectory1 = ''
  x_coord, y_coord, x_vel, y_vel, theta = take_step(x_coord, y_coord, x_vel, y_vel, theta)
  
  for x, y, v_x, v_y in zip(x_coord, y_coord, x_vel, y_vel):
    trajectory1 += f"{x} {y} {v_x} {v_y}" + '\n'

  # writing to file
  with open('data.txt', 'a') as file:
    file.write(trajectory1)
