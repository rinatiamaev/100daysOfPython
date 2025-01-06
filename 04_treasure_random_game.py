import random
print("Hello in Treasure Hunting Game!")
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want a pick a treasure? Tupe row and column with comma and space: ")
choice_pos = position.split(", ")
row_choice = int(choice_pos[0]) - 1
col_choice = int(choice_pos[1]) - 1
treasure_pos = map[random.randint(0, 2)][random.randint(0, 2)]
if treasure_pos == choice_pos:
    map[choice_pos[0]][choice_pos[1]] = "💰"
    print(f"{row1}\n{row2}\n{row3}")
    print("Congratulations! You found a treasure!")
else:
    map[row_choice][col_choice] = "X"
    print(f"{row1}\n{row2}\n{row3}")
    print("Sorry, you didn't find a treasure. Try again.")