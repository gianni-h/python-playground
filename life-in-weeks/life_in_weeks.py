age = input("What is your current age? ")
ageInt = int(age)
daysToNinety = 90 * 365 - ageInt * 365
weeksToNinety = 90 * 52 - ageInt * 52
monthsToNinety = 90 * 12 - ageInt * 12

message = f"You have {daysToNinety} days or {weeksToNinety} weeks or {monthsToNinety} months left" 
print(message)

