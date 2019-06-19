# coding=utf-8
import unittest
import random
import time


class Matrix(object):


    def __init__(self, line=1, column=3, fill_motif=" ", border=True):


        self.line_num = line
        self.column_num = column
        self.fill_motif = fill_motif
        self.border = border
        #self.matrix_col = []
        self.matrix = []
        self.last_coord = {}


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



        for x,value in pattern.items(): # on actualise les coordonné des items pour les placer au milieus
            self.last_coord[X +x] = [a + Y for a in pattern[x]]

        print (self.last_coord)
        for x, value in self.last_coord.items():
            for _, y in enumerate(value):


                self.matrix[x][y] =  "O"


    """def down(self):
        print (self.last_coord)
        for coo in self.last_coord:
            print(coo)


            print("coo[0]:{}, coo[1]:{}".format(coo[0], coo[1]))
            #if self.matrix [coo[0]+1][coo[1]] != " ":
                #return -1"""




    def __repr__(self):


        matrix_display = ""
        for line in range(len(self.matrix)): # on concatene toute les ligne en y intercalant  un retour chariot
            matrix_display += "".join(self.matrix[line]) + "\n"

        return matrix_display






#-----------------------------------------------------------------------------------------

class pattern(object):


    def __init__(self, choice=1):


        self.coord = {} # dictionnaire qui contient la description des pattern  0 = 2,3,4 ou de la forme x = y+2, y+3, y+4

        if choice == "random":
            choice = random.randrange(5)
            print( choice)



        if choice == 1: #truc décalé
            self.coord = {0: [1, 2], 1: [0,1] }

        elif choice == 2: # T a l'envers
            self.coord = {0: [1], 1: [0, 1, 2]}

        elif choice == 3: # carre
            self.coord = {0: [0, 1], 1: [0, 1]}
        elif choice == 4: # l
            self.coord = {0: [2], 1: [0, 1, 2]}

        #elif choice == 5:
        #elif choice == 6:
        #elif choice == 7:
        else:
            print("error")

    def __repr__(self):
        return self.coord
#-----------------------------------------------------------------------------------------------------------


play_ground = Matrix(20, 40)


play_ground.place_patern(pattern(2).coord)

#play_ground.down()
print(play_ground)
