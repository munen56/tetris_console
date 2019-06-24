# -*-coding:Latin-1 -*

import math as mt
import os, time

line = 30
column = 90
matrix = []

for j in range(line):
    matrix.append(list(" " * column))

def matrix_display(matrix=matrix):
    matrix_display = ""
    for line in range(len(matrix)):  # on concatene toute les ligne en y intercalant  un retour chariot
        matrix_display += "".join(matrix[line]) + "\n"
    print(matrix_display)




def rotate(x, y, theta):

    theta_radians = mt.radians(theta)
    x_prim = round((x*mt.cos(theta_radians)) - (y*mt.sin(theta_radians)))
    y_prim = round((x*mt.sin(theta_radians)) + (y*mt.cos(theta_radians)))

    return x_prim, y_prim


mess =  "Ludivine"
x_coo = [15, 15, 15, 15, 15, 15, 15, 15]
y_coo = [45, 46, 47, 48, 49, 50, 51, 52]



tet=0
while tet<361:
    x_temp = []
    y_temp = []

    for i in range(len(x_coo)): #line
        x,y = rotate(x_coo[i]-14, y_coo[i]-45, tet)
        x_temp.append(x+14)
        y_temp.append(y+45)

    for i in range(len(x_coo)):  # line
        matrix[x_temp[i]][y_temp[i]] = mess[i]

    matrix_display()

    for i in range(len(x_coo)):  # line
        matrix[x_temp[i]][y_temp[i]] = " "

    time.sleep(2)
    os.system('cls')

    if tet < 360:
        tet += 90
    else:
        tet = 0

