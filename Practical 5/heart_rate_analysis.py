import matplotlib.pyplot as plt
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rates)
total_bpm = sum(heart_rates)
mean_heart_rate = total_bpm / num_patients
print("There are " + str(num_patients) + " patients in the dataset and the mean heart rate is " + str(mean_heart_rate) + " bpm.")
low = normal = high = 0
for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:
        high += 1
print("Number of patients with Low heart rate (< 60 bpm): " + str(low))
print("Number of patients with Normal heart rate (60-120 bpm): " + str(normal))
print("Number of patients with High heart rate (> 120 bpm): " + str(high))
categories = {'Low': low, 'Normal': normal, 'High': high}
largest_category = max(categories, key=categories.get)
print("The category with the largest number of patients is " + largest_category + ".")
labels = ['Low (< 60 bpm)', 'Normal (60-120 bpm)', 'High (> 120 bpm)']
sizes = [low, normal, high]
colors = ['lightblue', 'lightgreen', 'red']
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=160)
plt.title('Distribution of Heart Rate Categories')
plt.axis('equal')
plt.show()