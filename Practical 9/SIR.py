import numpy as np
import matplotlib.pyplot as plt

N = 10000
S = 9999
I = 1
R = 0
beta = 0.3
gamma = 0.05
time_points = 1000
S_list = [S]
I_list = [I]
R_list = [R]

for time in range(time_points):
    infection_prob = beta * (I / N)

    if infection_prob > 1:
        infection_prob = 1

    if S > 0 and I > 0:
        infection_choices = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob])
        new_infections = sum(infection_choices)
    else:
        new_infections = 0

    if I > 0:
        recovery_choices = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])
        new_recoveries = sum(recovery_choices)
    else:
        new_recoveries = 0

    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label="susceptible")
plt.plot(I_list, label="infected")
plt.plot(R_list, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend()
plt.show()
