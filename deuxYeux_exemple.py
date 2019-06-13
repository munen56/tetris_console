# -*-coding:Latin-1 -*

import msvcrt
import time
import os
import winsound

#os.system("color 9f")
#winsound.Beep(3500, 300)

"""
i = 1
while i:
    car = "0"
    check =  msvcrt.kbhit()
    if check:
        car = msvcrt.getch()
    print(car)
    time.sleep(1)
"""

#-----------------------------------------------------------------------
line_num=50
col_num=30

def line(line_num):

    line = []

    for i in range(line_num+1):
        line.append(" ")
    return line

def col(col_num, line_num):


    col = []

    for i in range(col_num+1):
        col.append(line(line_num))
    return col


grid = (col(col_num, line_num))

grid[10][10] = "OO"

for h in range(len(grid)):
    print("".join(grid[h]))


z = 1
x=10 #ligne
y=10 #colonne
while z:
    grid[x][y] = "OO"
    for h in range(len(grid)):
        print("".join(grid[h]))

    car = "0"
    check =  msvcrt.kbhit()
    if check:
        car = msvcrt.getch()

    if car == b"q":
        y -= 1
    elif car == b"d":
        y += 1
    elif car == b"z":
        x -= 1
    elif car == b"s":
        x += 1

    time.sleep(0.2)
    os.system('cls')
    grid = (col(col_num, line_num))




time.sleep(2)
os.system('cls')
#-------------------------------------------------