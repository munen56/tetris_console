# coding=utf-8
import unittest
import random
import time
import os


class Matrix(object):


    def __init__(self, line=1, column=3, fill_motif=" ", border=True):


        self.line_num = line
        self.column_num = column
        self.fill_motif = fill_motif
        self.border = border
        self.matrix = []
        self.last_coord = {}



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
        Y = self.column_num // 2 #milieu d'une ligne(si elle est paire ^^).



        for x,value in pattern.items(): # on actualise les coordonné des items pour les placer au milieus
            self.last_coord[X + x] = [a + Y for a in pattern[x]]

        for x, value in self.last_coord.items():
            for _, y in enumerate(value):
                self.matrix[x][y] =  "O"


    def down(self):


        nouveau_coordonné = {}

        for x, y in self.last_coord.items():
                nouveau_coordonné[x+1] = y

        for x, value in self.last_coord.items():
            for _, y in enumerate(value):
                self.matrix[x][y] =  " "

        for x, value in nouveau_coordonné.items():
            for _, y in enumerate(value):
                self.matrix[x][y] =  "O"
        self.last_coord = nouveau_coordonné





    def __repr__(self):


        matrix_display = ""
        for line in range(len(self.matrix)): # on concatene toute les ligne en y intercalant  un retour chariot
            matrix_display += "".join(self.matrix[line]) + "\n"

        return matrix_display






#-----------------------------------------------------------------------------------------

class pattern(object):


    def __init__(self, choice=1):


        self.coordonné_pour_affichage = {} # dictionnaire qui contient les coordonés des pattern  0 = 2,3,4 de la forme x = y+2, y+3, y+4
        self.coordonné_pour_collision = {}
        if choice == "random":
            choice = random.randrange(5)

        if choice == 1: #truc décalé
            self.coordonné_pour_affichage = {0: [1, 2], 1: [0, 1]}
            self.coordonné_pour_collision = {0: [2], 1: [0, 1]}

        elif choice == 2: # T a l'envers
            self.coordonné_pour_affichage = {0: [1], 1: [0, 1, 2]}
            self.coordonné_pour_collision = { 1: [0, 1, 2]}

        elif choice == 3: # carre
            self.coordonné_pour_affichage = {0: [0, 1], 1: [0, 1]}
        elif choice == 4: # l
            self.coordonné_pour_affichage = {0: [2], 1: [0, 1, 2]}

        #elif choice == 5:
        #elif choice == 6:
        #elif choice == 7:
        else:
            print("error")

    def __repr__(self):
        return self.coordonné_pour_affichage
#-----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    play_ground = Matrix(20, 40)


    piece_en_cours = pattern(2)
    play_ground.place_patern(piece_en_cours.coordonné_pour_affichage)

    print(play_ground.down())

    while 1:
        print(play_ground)
        play_ground.down()
        time.sleep(0.5)
        os.system('cls')
