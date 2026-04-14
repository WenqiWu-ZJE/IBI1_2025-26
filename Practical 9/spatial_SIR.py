"""
Pseudocode:
Set up a 100 by 100 population grid.
Use 0 for susceptible, 1 for infected, and 2 for recovered.
Choose one random grid position as the first infected person.
Set beta, gamma, and the number of time points.
Save the starting population for plotting.
For each time point from 1 to 100:
    Find all currently infected cells.
    For each infected cell:
        Check the 8 neighbouring cells around it.
        Skip the infected cell itself.
        Check that the neighbour is not outside the grid.
        If the neighbour is susceptible, infect it with probability beta.
        Let the infected cell recover with probability gamma.
    If this is time 10, 50, or 100, save a copy of the population.
Plot the saved populations for time 0, 10, 50, and 100 as heat maps.
"""

import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3
gamma = 0.05
time_points = 100
plot_times = [0, 10, 50, 100]
saved_populations = {0: population.copy()}

for time in range(1, time_points + 1):
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in range(x - 1, x + 2):
            for yNeighbour in range(y - 1, y + 2):
                if (xNeighbour, yNeighbour) != (x, y):
                    inside_x = xNeighbour != -1 and xNeighbour != 100
                    inside_y = yNeighbour != -1 and yNeighbour != 100
                    if inside_x and inside_y:
                        if population[xNeighbour, yNeighbour] == 0:
                            infection_result = np.random.choice([0, 1], p=[1 - beta, beta])
                            population[xNeighbour, yNeighbour] = infection_result
        recovery_result = np.random.choice([0, 2], p=[1 - gamma, gamma])
        if recovery_result == 2:
            population[x, y] = 2
    if time in plot_times:
        saved_populations[time] = population.copy()

plt.figure(figsize=(8, 6), dpi=150)

for i in range(len(plot_times)):
    time = plot_times[i]
    plt.subplot(2, 2, i + 1)
    plt.imshow(saved_populations[time], cmap="viridis", interpolation="nearest", vmin=0, vmax=2)
    plt.title("time " + str(time))
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()
