# Viscek-2D-flocking
Implementation of Viscek 2D simulation model in [Python3](https://www.python.org/).  
## Background  
The simulation is carried out in a square shaped cell of size $L$ with periodic boundary conditions. An interaction radius of $r=1$ is used with a time step of $\Delta t=1$.  
### Initial conditions:  
- At time $t=0$, $N$ particles were randomly distributed in the cell, with randomly distributed directions $\theta$  
- Each particle has the same absolute velocity $\mathcal{v}$.  
### Trajectory propagation:  
The position of the *i*th particle is updated according to,  
$$\mathbf{x}_i(t+1) = \mathbf{x}_i(t) + \mathbf{v}_i(t)\Delta t$$  
the velocity of a particle $\mathbf{v}_i(t)$ is constructed simultaneously at each time step to have an absolute value $\mathcal{v}$ and a direction given by the angle $\theta_i(t)$  
## Result  
<p align="center">
  <img src="https://github.com/abirm766/Viscek-2D-flocking/blob/main/simulation.gif">
</p>
