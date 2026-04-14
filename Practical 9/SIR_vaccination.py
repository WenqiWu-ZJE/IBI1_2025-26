import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05
time_points = 1000
vaccination_percentages = range(0, 101, 10)

def run_sir(vaccination_percent):
    infected_start = 1
    vaccinated = round(N * vaccination_percent / 100)

    if vaccinated > N - infected_start:
        vaccinated = N - infected_start

    S = N - vaccinated - infected_start
    I = infected_start
    R = 0

    I_list = [I]

    for time in range(time_points):
        infection_prob = beta * (I / N)

        if infection_prob > 1:
            infection_prob = 1

        if S > 0 and I > 0:
            infection_choices = np.random.choice(
                [0, 1],
                size=S,
                p=[1 - infection_prob, infection_prob],
            )
            new_infections = sum(infection_choices)
        else:
            new_infections = 0

        if I > 0:
            recovery_choices = np.random.choice(
                [0, 1],
                size=I,
                p=[1 - gamma, gamma],
            )
            new_recoveries = sum(recovery_choices)
        else:
            new_recoveries = 0

        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries

        I_list.append(I)

    return I_list


plt.figure(figsize=(6, 4), dpi=150)

for percent in vaccination_percentages:
    infected_numbers = run_sir(percent)
    line_color = cm.viridis(percent / 100)
    plt.plot(infected_numbers, color=line_color, label=str(percent) + "% vaccinated")

plt.xlabel("time")
plt.ylabel("number of infected people")
plt.title("SIR model with vaccination")
plt.legend()
plt.show()
