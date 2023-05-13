row0 = ["0"," 1"," 2"," 3"]
row1 = ["1","⬜️","️⬜️","⬜️"]
row2 = ["2","⬜️","⬜️","️⬜️"]
row3 = ["3","⬜️️","⬜️️","⬜️"]
map = [row1, row2, row3]
print(f"{row0}\n{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? [column:row]")

#grabs individual characters of input and turns them into int
horizontal = int(position[0])
vertical = int(position[1])

#locates horizontal position within the row, changes value to X
#no need for [horizontal - 1] index moves 1 position because of coords
map[vertical - 1][horizontal] = "X"

#prints marked map
print(f"{row0}\n{row1}\n{row2}\n{row3}") 