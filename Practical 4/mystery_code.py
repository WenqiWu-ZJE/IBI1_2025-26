# What does this piece of code do?
# Answer: This code calculates and prints the sum of 11 random integers, each ranging from 1 to 10.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5

# Note: This function is imported but not actually used in the code below.
from math import ceil
# Note: Initializes a variable to store the cumulative sum of the random numbers.
total_rand = 0
# Note: Initializes a counter variable to track the number of loops executed.
progress=0
# Note: A loop that repeats as long as 'progress' is 10 or less (running a total of 11 times).
while progress<=10:
	# Note: Increments the counter by 1 during each execution to eventually end the loop.
	progress+=1
	# Note: Draws a random integer between 1 and 10 and adds it to the cumulative total.
	n = randint(1,10)
	# Note: Adds the drawn random number to the cumulative total.
	total_rand+=n
# Note: After the loop finishes, it prints the final cumulative total of the random numbers drawn.
print(total_rand)