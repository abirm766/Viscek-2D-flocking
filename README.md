# Viscek-2D-flocking
Implementation of Viscek 2D simulation model in [Python3](https://www.python.org/).  
## Background  
The simulation is carried out in a square shaped cell of size $L$ with periodic boundary conditions. An interaction radius of $r=1$ is used with a time step of $\Delta t=1$.  
### Initial conditions:  
- At time $t=0$, $N$ particles were randomly distributed in the cell, with randomly distributed directions $\theta$  
- Each particle has the same absolute velocity $\mathcal{v}$.  
### Trajectory propagation:  
The position of the *i*th particle is updated according to,  
$$\mathbf{x}_i(t+1) = \mathbf{x}_i(t) + \mathbf{v}_i(t)\Delta t \quad (1)$$  
the velocity of a particle $\mathbf{v}_i(t)$ is constructed simultaneously at each time step to have an absolute value $\mathcal{v}$ and a direction given by the angle $\theta(t)$ which obeys the following propagation formula,
$$\theta(t+1) = \langle \theta(t)\rangle_r + \Delta \theta \quad (2)$$  
Where $\langle \theta(t)\rangle_r$ denotes the average direction of the
velocities of particles (including particle i) being
within a circle of radius $r$ surrounding the given particle, given by the following formula,
$$\langle \theta(t)\rangle_r = \arctan{\left[\frac{\langle \sin(\theta(t))\rangle_r}{\langle \cos(\theta(t))\rangle_r}\right]} \quad (3)$$  
The $\Delta \theta$ term in Eq. (2) represents noise, and is chosen randomly with a uniform probability from the interval $[-\eta/2, \eta/2]$. It can be interpreted as a temperatrure-like variable.  
### Parameters:  
There are three free parameters for a given system size, $\eta,$ $\rho,$ and $\mathcal{v}$. Here, $\mathcal{v}=0.03$ (in suitable unit) is used in the simulation. The density $\rho$ is given by, $\rho=N/L^2$. The number of particles $N$ is set at 300. The cell size $L$ and $\eta$ can be varied accordingly to get different interaction behaviours.  
## Usage  
Run in terminal: ```python3 example.py```  
The ```simulation.py``` script generates simulation data named as ```data.txt```. The pictorial representation of the dynamics can be observed by further using the script ```visualize.py```, which generates an animated gif named as ```simulation.gif```. ```voronoiPlot.py``` script can be used to get the corresponding [Voronoi](https://en.wikipedia.org/wiki/Voronoi_diagram#:~:text=In%20mathematics%2C%20a%20Voronoi%20diagram,%2C%20sites%2C%20or%20generators) diagrams.  
the ```box_width``` and ```eta``` variables in ```simulation.py``` script can be varied accordingly to get different interaction dynamics.  
## Source Meterial  
Vicsek, T., Czirok, A., Ben-Jacob, E., Cohen, I., & Shochet, O. (1995). Novel Type of Phase Transition in a System of Self-Driven Particles. *Physical Review Letters, 75*(6), 1226–1229. https://doi.org/10.1103/physrevlett.75.1226
## Result  
<p align="center">
  <img src="https://github.com/abirm766/Viscek-2D-flocking/blob/main/simulation.gif">
</p>
