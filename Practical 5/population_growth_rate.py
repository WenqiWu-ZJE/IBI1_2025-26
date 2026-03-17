import matplotlib.pyplot as plt
country_data = {'UK': [66.7, 69.2],'China': [1426.0, 1410.0],'Italy': [59.4, 58.9],'Brazil': [208.6, 212.0],'USA': [331.6, 340.1]}
population_changes = []
for country, populations in country_data.items():
    pop_2020 = populations[0]
    pop_2024 = populations[1]
    percent_change = ((pop_2024 - pop_2020) / pop_2020) * 100
    print("The percentage population change for " + country + " is " + str(percent_change) + "%")
    population_changes.append([country, percent_change])
print()
def getchange(i):
    return i[1]
population_changes.sort(key=getchange, reverse=True)
print("Population changes sorted from largest increase to largest decrease:")
for country, change in population_changes:
    print(country + ": " + str(change) + "%")
print()
largest_increase = population_changes[0]
largest_decrease = population_changes[4]
print("The country with the largest increase in population is " + largest_increase[0] + " (" + str(largest_increase[1]) + ").")
print("The country with the largest decrease in population is " + largest_decrease[0] + " (" + str(largest_decrease[1]) + ").")
print()
countries = []
changes = []
for country, change in population_changes:
    countries.append(country)
    changes.append(change)
colors = []
for i in range(len(changes)):
    if changes[i] > 0:
        colors.append('green')
    else:
        colors.append('red')
plt.figure(figsize=(8, 6))
plt.bar(countries, changes, color=colors)
bar = plt.bar(countries, changes, color=colors)
plt.bar_label(bar, padding=3, fmt='%1.1f%%')
plt.title('Population Percentage Change (2020-2024)')
plt.xlabel('Country')
plt.ylabel('Percentage Change (%)')
plt.axhline(0, color='black', linewidth=1)
plt.show()