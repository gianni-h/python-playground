year = int(input("Which year do you want to check? "))

#is the year divisible by 4? yes: leap year EXCEPT divisble by 100. no: not leap year
if year % 4 == 0:
    #is the year also divisible by 100? yes: not leap year UNLESS divisble by 400. no: Leap year.
    if year % 100 == 0:
        #divisble by 4 AND 100 AND divisible by 400? yes: leap year.
        if year % 400 == 0:
            result = "Leap  year."
        #divisible by 4 AND 100 but NOT divisble by 400? no: not leap year
        else:
            result = "Not leap year."
    #divisble by 4 but NOT by 100: Leap year
    else:
        result = "Leap year."
#not divisible by 4: not leap yaer
else:
    result = "Not leap year."

print(result)