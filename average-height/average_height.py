#ask input
heights = input("Input a list of heights ").split()

#declare variables
average_height = 0
height_count = 0
sum_height = 0

#run for loop. This loop will run as many times as there are items in the list.
for n in heights:
    #turns input into int
    heights[n] = int(heights[n])
    #makes sum of all heights
    sum_height += heights[n]
    #count how many times for loop is ran: counts how many height inputs have been given
    height_count += 1

#calculate average and rounds the number
average_height = round(sum_height / height_count)

#prints result
print(average_height)
