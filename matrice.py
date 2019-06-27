# coding=utf-8
import unittest
import random
import time
import os
import msvcrt
import math as mt


class Matrix(object):

    def __init__(self, line=1, column=3, fill_motif=".", border=True):
        self.line_num = line
        self.column_num = column
        self.fill_motif = fill_motif
        self.border = border
        self.matrix = []
        self.last_coord = {}

        Matrix._create_matrix(self)

    def _create_matrix(self):

        for _ in range(self.line_num):
            self.matrix.append(list(self.fill_motif * self.column_num))

        if self.border:
            for indice, _ in enumerate(self.matrix):
                self.matrix[indice][0] = "#"
                self.matrix[indice][self.column_num - 1] = "#"
            self.matrix[self.line_num - 1] = list("#" * self.column_num)

    def coordonné_vers_matrice(self, dico_de_coordonné, symbole):

        for x, y_group in dico_de_coordonné.items():
            for _, y in enumerate(y_group):
                self.matrix[x][y] = symbole

    def place_patern(self, pattern):
        """positione un pattern en haut, au centre de la matrice"""

        x_origin = 0  # premiere ligne (en haut) de la matrice
        y_middle = self.column_num // 2  # milieu d'une ligne(si elle est paire ^^).

        for x in pattern.keys():  # on actualise les coordonné des items pour les placer au milieux
            self.last_coord[x_origin + x] = [y_pattern + y_middle for y_pattern in pattern[x]]

        Matrix.coordonné_vers_matrice(self, self.last_coord, "0")

    def _bottom_collision(self):
        collision = False

        for x, value in self.last_coord.items():
            for _, y in enumerate(value):
                if self.matrix[x + 1][y] == "O" or self.matrix[x + 1][y] == "#":
                    collision = True  # le fond de la boite ou le sommet d'une piece posé

        return collision

    #def _complete_line(self):


    def _side_collision(self, direction):
        collision = False

        for x, value in self.last_coord.items():
            for _, y in enumerate(value):
                if direction == "left" and self.matrix[x][y - 1] == "O" or self.matrix[x][y - 1] == "#":
                    collision = True  # coté gauche
                if direction == "right" and self.matrix[x][y + 1] == "O" or self.matrix[x][y + 1] == "#":
                    collision = True  # coté droit
        return collision
    # rotation group ---------------------------------------------------------------------------------------------------
    def _rotation_center(self):
        """return les coordonnés du centre de rotation du motif actuelle"""

        center_x = max(self.last_coord.keys())
        for y in self.last_coord.values():
            center_y = min(y)
        print("center x", center_x,"center y", center_y)
        return center_x, center_y

    def rotate_90degree(self, theta=90):

        #if car == b"z":
            rotated_coordinate = {}
            mini=0
            list_coo=[]
            theta_radians = mt.radians(theta)
            x_prims = []
            y_tourné = []
            center_x, center_y = Matrix._rotation_center(self)

            for x, y_group in self.last_coord.items():
                for y in y_group:
                    print("x, y ", x, y)
                    #x -= center_x methode center defectueuse
                    #y -= center_y

                    x_tourné = round((x * mt.cos(theta_radians)) - (y * mt.sin(theta_radians))) + center_x
                    y_tourné =  round((x * mt.sin(theta_radians)) + (y * mt.cos(theta_radians))) + center_y



                    list_coo.append((x_tourné, y_tourné))

            for couple in list_coo:
                if mini > couple[0]:
                    mini = couple[0]

            for couple in list_coo:
                rotated_coordinate[couple[0]+abs(mini)]=[]


            for couple in list_coo:
                rotated_coordinate[couple[0]+abs(mini)].append(couple[1])

            Matrix.coordonné_vers_matrice(self, self.last_coord, " ")
            self.last_coord = rotated_coordinate

            print("last coord", self.last_coord)
            print('rotated', rotated_coordinate)


    # ------------------------------------------------------------------------------------------------------------------
    def translate(self, car):

        Matrix.coordonné_vers_matrice(self, self.last_coord, " ")  # risque d'effacement du pattern lors de l'appel a translate si on commente la ligne les traces laissé ne constituent pas des points d'arrets ???

        if car == b"q" and not Matrix._side_collision(self, "left"):
            Matrix._deplacement(self, "left")
            return True

        elif car == b"d" and not Matrix._side_collision(self, "right"):
            Matrix._deplacement(self, "right")
            return True

    def _deplacement(self, direction):

        for x, y_group in self.last_coord.items():
            for indice, y in enumerate(y_group):
                if direction == "left":
                    self.last_coord[x][indice] = y - 1
                elif direction == "right":
                    self.last_coord[x][indice] = y + 1

    def down(self, ):

        nouveau_coordonné = {}

        if Matrix._bottom_collision(self):
            Matrix.coordonné_vers_matrice(self, self.last_coord, "O")  # ligne utile ????
            self.last_coord = {}
            return False

        else:
            for x, y in self.last_coord.items():
                nouveau_coordonné[x + 1] = y

            Matrix.coordonné_vers_matrice(self, self.last_coord, " ")
            Matrix.coordonné_vers_matrice(self, nouveau_coordonné, "0")

            self.last_coord = nouveau_coordonné

            return True

    def __repr__(self):

        matrix_display = ""
        for line in range(len(self.matrix)):  # on concatene toute les ligne en y intercalant  un retour chariot
            matrix_display += "".join(self.matrix[line]) + "\n"

        return matrix_display


# -----------------------------------------------------------------------------------------

class pattern(object):

    def __init__(self, choice=1):

        self.coordonné_pour_affichage = {}  # dictionnaire qui contient les coordonés des pattern  0 = 2,3,4 de la forme x = y+2, y+3, y+4
        self.coordonné_pour_collision = {}
        if choice == "random":
            choice = random.randrange(1, 5)

        if choice == 1:  # truc décalé
            self.coordonné_pour_affichage = {0: [1, 2], 1: [0, 1]}

        elif choice == 2:  # T a l'envers
            self.coordonné_pour_affichage = {0: [1], 1: [0, 1, 2]}

        elif choice == 3:  # carre
            self.coordonné_pour_affichage = {0: [0, 1], 1: [0, 1]}
        elif choice == 4:  # l
            self.coordonné_pour_affichage = {0: [2], 1: [0, 1, 2]}

        # elif choice == 5:
        # elif choice == 6:
        # elif choice == 7:
        else:
            print("error")

    def __repr__(self):
        return self.coordonné_pour_affichage


# -----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    play_ground = Matrix(20, 40)

    # ---------<<<pour test a supprimer des que possible
    piece_en_cours = pattern(1)
    play_ground.place_patern(piece_en_cours.coordonné_pour_affichage)
    print(play_ground)
    play_ground.rotate_90degree()
    """

# ----------pour test a supprimer des que possible>>>

    def keyboard_input():
        car = "0"
        check = msvcrt.kbhit()
        if check:
            car = msvcrt.getch()
        return  car




    while True:
        piece_en_cours = pattern("random")
        play_ground.place_patern(piece_en_cours.coordonné_pour_affichage)




        continu = True
        while continu:
            start_time = time.time()
            end_time = 0
            print(play_ground)

            while end_time - start_time < 0.5:
                end_time = time.time()

                command_carachters = keyboard_input()
                if command_carachters != 0:
                    play_ground.translate(command_carachters)
                    play_ground.rotate_90degree(command_carachters)
                    #play_ground.anticip_down(command_carachters)
            continu = play_ground.down()

            os.system('cls')
            """
