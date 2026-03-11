# 1. Prompt user to input:
#   - Age (integer, less than 100)
#   - Weight (integer, between 20 and 80)
#   - Gender (string, "male" or "female")
#   - Creatinine concentration (integer, between 0 and 100)
# 2. Initialize an empty list ”errors“.
# 3. Validate inputs:
#   - If age is 100 or more, add "age" to “errors”.
#   - If weight is less than or equal to 20 or greater than or equal to 80, add "weight" to “errors”.
#   - If creatinine concentration is less than or equal to 0 or greater than or equal to 100, add "creatine concentration" to “errors”.
#   - If gender is not "male" or "female", add "gender" to “errors”.
# 4. If ”errors“ is not empty:
#   - Print a message indicating the calculation has stopped.
#    - Print the list of invalid input variables.
#    - Exit the program.
# 5. If all inputs are valid:
#    - Calculate creatinine clearance (CrCl) using the formula:
#      CrCl = ((140 - age) * weight) / (72 * creatinine concentration)
#    - If gender is "female", multiply CrCl by 0.85.
# 6. Print the calculated CrCl value.


age = int(input("Enter the age of the patient in years (less than 100): "))
weight = int(input("Enter the weight of the patient in kg (between 20 and 80): "))
gender = input("Enter the gender of the patient (male or female): ")
cr = int(input("Enter the creatinine concentration of the patient in umol/l (between 0 and 100): "))

errors = []

if age >= 100:
    errors.append("age")

if weight <= 20 or weight >= 80:
    errors.append("weight")

if cr <= 0 or cr >= 100:
    errors.append("creatine concentration")

if gender != "male" and gender != "female":
    errors.append("gender")

if len(errors) > 0:
    print("The calculation has stopped. The following input variables need to be corrected：")
    for item in errors:
        print(item)
else:
    crcl = ((140 - age) * weight) / (72 * cr)
    
    if gender == "female":
        crcl = crcl * 0.85
    
    print("The calculated creatinine clearance (CrCl) is: " + str(crcl))
