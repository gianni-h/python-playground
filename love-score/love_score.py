print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
score = 0
#turns input into lower case
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
#checks input name1 for 'true'
t_count_name1 = lower_case_name1.count("t")
r_count_name1 = lower_case_name1.count("r")
u_count_name1 = lower_case_name1.count("u")
e_count_name1 = lower_case_name1.count("e")
#checks input name2 for true
t_count_name2 = lower_case_name2.count("t")
r_count_name2 = lower_case_name2.count("r")
u_count_name2 = lower_case_name2.count("u")
e_count_name2 = lower_case_name2.count("e")
#checks input name1 for 'true'
l_count_name1 = lower_case_name1.count("l")
o_count_name1 = lower_case_name1.count("o")
v_count_name1 = lower_case_name1.count("v")
e_count_name1 = lower_case_name1.count("e")
#checks input name2 for love
l_count_name2 = lower_case_name2.count("l")
o_count_name2 = lower_case_name2.count("o")
v_count_name2 = lower_case_name2.count("v")
love_e_count_name2 = lower_case_name2.count("e")
#combines true count for name1 and name2
true_count_name1 = t_count_name1 + r_count_name1 + u_count_name1 + e_count_name1 
true_count_name2 = t_count_name2 + r_count_name2 + u_count_name2 + e_count_name2
true_count = true_count_name1 + true_count_name2
#combines love count for name1 and name2
love_count_name1 = l_count_name1 + o_count_name1 + v_count_name1 + e_count_name1
love_count_name2 = l_count_name2 + o_count_name2 + v_count_name2 +love_e_count_name2
love_count = love_count_name1 + love_count_name2
#converts two digits from true_count and love_count to string
#puts them together for the final score
true_count_as_string = str(true_count)
love_count_as_string = str(love_count)
score = true_count_as_string + love_count_as_string
#turns score into int
score_as_int = int(score)

if score_as_int < 10 or score_as_int > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score_as_int >= 40 and score_as_int <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}.")