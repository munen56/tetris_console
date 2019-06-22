# coding=utf-8
import unittest
import random
import time
import os
import msvcrt


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

    def coordonné_vers_matrice(self, dico_de_coordonné, symbole):

        for x, value in dico_de_coordonné.items():
            for _, y in enumerate(value):
                self.matrix[x][y] = symbole

    def place_patern(self, pattern):
        """positionne un pattern en haut, au centre de la matrice"""


        X = 0 #premiere ligne (en haut) de la matrice
        Y = self.column_num // 2 #milieu d'une ligne(si elle est paire ^^).



        for x,value in pattern.items(): # on actualise les coordonné des items pour les placer au milieus
            self.last_coord[X + x] = [a + Y for a in pattern[x]]

        Matrix.coordonné_vers_matrice(self, self.last_coord, "0")



    def is_there_collision(self):
        collision = False

        for x, value in self.last_coord.items():
            for _, y in enumerate(value):
                if self.matrix[x+1][y] == "O" or self.matrix[x+1][y] == "#":
                    collision = True

        return collision

    def slide(self):
        while :




            car = "0"
            check = msvcrt.kbhit()
            if check:
                car = msvcrt.getch()

            if car == b"q":
                y -= 1

    def down(self, ):

        nouveau_coordonné = {}


        if Matrix.is_there_collision(self):
            Matrix.coordonné_vers_matrice(self, self.last_coord, "O")
            self.last_coord = {}
            return False
        else:

            for x, y in self.last_coord.items():
                    nouveau_coordonné[x+1] = y

            Matrix.coordonné_vers_matrice(self, self.last_coord, " ")
            Matrix.coordonné_vers_matrice(self, nouveau_coordonné, "0")

            self.last_coord = nouveau_coordonné
            return True

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


        elif choice == 2: # T a l'envers
            self.coordonné_pour_affichage = {0: [1], 1: [0, 1, 2]}


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


    continu = True
    while continu:
        print(play_ground)
        continu = play_ground.down()
        time.sleep(0.2)
        os.system('cls')

    piece_en_cours = pattern(2)
    play_ground.place_patern(piece_en_cours.coordonné_pour_affichage)

    continu = True
    while continu:
        print(play_ground)
        continu = play_ground.down()
        time.sleep(0.2)
        os.system('cls')
    piece_en_cours = pattern(3)
    play_ground.place_patern(piece_en_cours.coordonné_pour_affichage)

    continu = True
    while continu:
        print(play_ground)
        continu = play_ground.down()
        time.sleep(0.2)
        os.system('cls')
    piece_en_cours = pattern(1)
    play_ground.place_patern(piece_en_cours.coordonné_pour_affichage)

    continu = True
    while continu:
        print(play_ground)
        continu = play_ground.down()
        time.sleep(0.2)
        os.system('cls')
