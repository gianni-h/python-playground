height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))

#calculates BMI and turns it into int
bmi = weight / (height / 100) ** 2 
#rounds to nearest whole number
bmi_rounded = round(bmi)

#checks if bmi is smaller than 18.5
if bmi_rounded < 18.5:
    result = f"Your BMI is {bmi_rounded}, you are underweight."

#if NOT smaller than or equal to 18.5 -> check if smaller or equal to 25
elif bmi_rounded <= 25:
    result = f"Your BMI is {bmi_rounded}, you have a normal weight."

#if NOT smaller than or equal to 25 -> check if smaller or equal to 30
elif bmi_rounded <= 30:
    result = f"Your BMI is {bmi_rounded}, you are slightly overweight."

#if NOT smaller than or equal to 30 -> check if smaller or equal to 35
elif bmi_rounded <= 35:
    result = f"Your BMI is {bmi_rounded}, you are obese."
#if NOT smaller than or equal to 35 -> clinically obese
else :
    result = f"Your BMI is {bmi_rounded}, you are clinically obese."


#turns bmi into int and prints result
print(result)
