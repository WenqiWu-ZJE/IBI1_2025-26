import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/mac/Desktop/IBI1/IBI1_2025-26/IBI1_2025-26/Practical 10")
print(os.getcwd())
print(os.listdir())

# 1. Import the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())

# 2. Show the 3rd and 4th columns (Year and DALYs) for the first 10 rows
first_10 = dalys_data.iloc[0:10, 2:4]
print(first_10)
# The maximum DALYs across the first 10 years for Afghanistan is in 1998 (DALYs = 86656.29)

# 3. Use a Boolean to show all years for which DALYs were recorded in Zimbabwe
is_zimbabwe = dalys_data.Entity == "Zimbabwe"
zimbabwe_years = dalys_data.loc[is_zimbabwe, "Year"]
print(zimbabwe_years)
# The first year recorded for Zimbabwe is 1990, the last year is 2019

# 4. Find the countries with the maximum and minimum DALYs in 2019
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_idx = recent_data["DALYs"].idxmax()
max_country = recent_data.loc[max_idx, "Entity"]
max_dalys = recent_data.loc[max_idx, "DALYs"]
print("Country with max DALYs in 2019:", max_country, max_dalys)
min_idx = recent_data["DALYs"].idxmin()
min_country = recent_data.loc[min_idx, "Entity"]
min_dalys = recent_data.loc[min_idx, "DALYs"]
print("Country with min DALYs in 2019:", min_country, min_dalys)
# The country with the maximum DALYs in 2019 is Lesotho (90771.64)
# The country with the minimum DALYs in 2019 is Singapore (15045.11)

# 5. Plot DALYs over time for Lesotho (the country with the max DALYs in 2019)
lesotho = dalys_data.loc[dalys_data.Entity == "Lesotho", ["Year", "DALYs"]]

plt.figure()
plt.plot(lesotho.Year, lesotho.DALYs, "b+")
plt.xticks(lesotho.Year, rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs (rate per 100,000)")
plt.title("DALYs over time in Lesotho")
plt.tight_layout()
plt.show()

# 6. Custom question: How has the relationship between the DALYs in China and the UK changed over time?
#    (see question.txt for details)
china = dalys_data.loc[dalys_data.Entity == "China", ["Year", "DALYs"]]
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]

plt.figure()
plt.plot(china.Year.values, china.DALYs.values, "r+-", label="China")
plt.plot(uk.Year.values, uk.DALYs.values, "bo-", label="United Kingdom")
plt.xticks(china.Year, rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs (rate per 100,000)")
plt.title("DALYs over time: China vs United Kingdom")
plt.legend()
plt.tight_layout()
plt.show()

difference = china.DALYs.values - uk.DALYs.values
print("DALYs difference (China - UK) in 1990:", round(difference[0], 2))
print("DALYs difference (China - UK) in 2019:", round(difference[-1], 2))
