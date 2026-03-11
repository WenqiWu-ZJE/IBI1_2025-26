# 1. Define the total number of students in the IBI1 class (n = 91).
# 2. Set the initial number of infected students and the 24-hour growth rate.
# 3. Initialize a counter to track the number of days.
# 4. Create a loop that runs until the number of infected students reaches or exceeds 91.
# 5. Inside the loop:
#    a. Print the current day and the current number of infected students.
#    b. Calculate the new number of infected students by applying the growth rate.
#    c. Increment the day counter by one.
# 6. After the loop finishes, display the final day and the total time taken.


# Initialize starting variables
total_students = 91 
infected = 5
growth_rate = 0.4
days = 1

# Loop until everyone is infected
while infected < total_students:
    # Display the progress for each day 
    print("Day " + str(days) + ": " + str(infected) + " students are currently infected.")
    # Calculate the number of students for the next day
    infected = infected * (1 + growth_rate)
    # Increment the day counter
    days += 1

# Report the final day when the whole class is infected
print("Day " + str(days) + ": " + str(infected) + " students are currently infected.")
print("Total days taken to infect everyone: " + str(days))