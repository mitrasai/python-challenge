"""
program which will automatically place the golden star in a map and we will 
find it by marking a spot with an X.
"""
import random

def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) 
    for item in row]) for row in p_map]))
    
map1 = [["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"]]
print("This is our initial map...")
print_map(map1)

row = random.randint(0, 2)
col = random.randint(0, 2)

# print(row, col)
map1[row][col] = "⭐"
# print_map(map1)

gold_position = str(row+1) + str(col+1)
# print(gold_position)

user_position = input("What do you think: where is the Golden star in the map? ")
if gold_position == user_position:
    print("Congratulations!! You have foun the Golden star!!")
else:
    row_num = int(user_position[0])
    col_num = int(user_position[1])
    map1[row_num-1][col_num-1] = "❎"
    print("Unfortunatly you couldn't find it ☹️")

print_map(map1)