# coding=utf-8
import unittest
import random


class Matrix(object):


    def __init__(self, line=1, column=3, fill_motif=" ", border=True):


        self.line_num = line
        self.column_num = column
        self.fill_motif = fill_motif
        self.border = border
        #self.matrix_col = []
        self.matrix = []



        #matrix_col = list(self.fill_motif * self.column_num) # on créé une ligne contenant le nombre de colonne désiré ( column_num)
        #self.matrix =  self.matrix_col * self.line_num # on repete la ligne de matrix_col autant de fois qu'il nous faut de ligne (line_num)
        for j in range(self.line_num):
            self.matrix.append( list(self.fill_motif * self.column_num))

        if self.border :
            for ind, val in enumerate(self.matrix):
                self.matrix[ind][0] = "#"
                self.matrix[ind][self.column_num -1] =  "#"
            self.matrix[self.line_num - 1] = list("#" * self.column_num)


    def place_patern(self, pattern):
        """positionne un pattern en haut, au centre de la matrice"""


        X = 0 #premiere ligne (en haut) de la matrice
        Y = round(self.column_num / 2) #milieu d'une ligne(si elle est paire ^^).

        for x, value in pattern.items():
            for _, y in enumerate(value):
                self.matrix[X+x][Y+y] =  "O"


    def __repr__(self):


        matrix_display = ""
        for line in range(len(self.matrix)): # on concatene toute les ligne en y intercalant  un retour chariot
            matrix_display += "".join(self.matrix[line]) + "\n"

        return matrix_display






#-----------------------------------------------------------------------------------------

class pattern(object):


    def __init__(self, choice=1):

        self.choice = choice
        self.coord = {} # dictionnaire qui contient la description des pattern  0 = 2,3,4 ou de la forme x = y+2, y+3, y+4

        if choice == "random":
            random.choice(range(8))

        if choice == 1: #truc décalé
            self.coord = {0: [1, 2], 1: [0,1] }



        #elif choice == 2:
        #elif choice == 3:
        #elif choice == 4:
        #elif choice == 5:
        #elif choice == 6:
        #elif choice == 7:

    def __repr__(self):
        return self.coord
#-----------------------------------------------------------------------------------------------------------


play_ground = Matrix(40, 80)



play_ground.place_patern(pattern(1).coord)
print(play_ground)
