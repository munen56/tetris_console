import os
import time
import random as rd


line_num=30
col_num=20
level=0.2 #vitesse de chute

pos = ()
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

grid[len(grid)-1 ]= "*"*line_num

#grid[3]=["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]
#grid[2]=["O","","","","","","","","O","O","O"]



def init_symbol_t(grid):#return grid mais ca marche pas alors
   #il faut la transformer pour qu'elle retourne simplement la description (position et longeur par ligne) pour chaque motif

    mid_pos = int(len(grid[0]) / 2)
    mot = rd.randint(5,7)


    if mot == 1:
         return   mid_pos,4 #le baton
    elif mot == 2:
         return   mid_pos,1, mid_pos,3 #le L
    elif mot == 3:
         return   mid_pos+3,1, mid_pos,3 #l'autre L
    elif mot == 4:
        return   mid_pos,2, mid_pos-1,2 #truc decalé
    elif mot == 5:
         return   mid_pos-1,2, mid_pos,2 #truc décalé l'autre
    elif mot == 6:
         return   mid_pos,2, mid_pos,2 #carré
    elif mot == 7:
         return   mid_pos,1, mid_pos-1,3 #la grille, la position du 1 char de la premiere ligne, sa longueur, laposition du 1ER char de la 2EME etc




def chute(grid):
    #descente des motif au coup par coup, en boucle , par motif(meilleur solution\
    #on fait dessendre un motif en entier avec ses deplacemet et son integration a la ligne pui la fct s'arrete (et on verifi si une ligne a été coplété
    pos_1, len_1, pos_2, len_2 = init_symbol_t(grid) #on recupere les coordonées du motif
    for i in range(len(grid)-1):

        #1) on positionne le motif
        grid[i][pos_1:pos_1+len_1] = "O" * len_1
        grid[i+1][pos_2:pos_2 + len_2] = "O" * len_2

        #2) on affiche toute la grille
        for x in range(len(grid)):
            print("".join(grid[x]))

        #3) on delay l'affichage
        time.sleep(level)

        #4) on verifie si le dessous est libre si non: on quitte la boucle break (ou encore mieu return); si oui: on poursuit
        if grid[i+3][pos_2] != " " : #pourquoi un coup i+2 et l'autre i+3
            break

        #5) on efface l'ancienne position
        grid[i][pos_1:pos_1+len_1] = "" * len_1
        grid[i + 1][pos_2:pos_2 + len_2] = "" * len_2

        #6) on efface la console
        os.system('cls')
i=0
while i<10:

    chute(grid)
    os.system('cls')
    i+=1


#pause=input("fin")

"""
exemple insere 3 o consecutif dans une liste
liste=["","","",""]
liste[0:3]="o"*3
print(liste)
"""

"""
fais chuter un "o" dans une colonne simple de ""

#chute
line[0]="O"
print(line[0])
time.sleep(1)
os.system('cls')

for i in range(1,11):
    line[i-1] = " "
    line[i]="O"
    for x in range(11):
        print(line[x])
    time.sleep(1)
    os.system('cls')

"""