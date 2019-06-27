# coding=utf-8
import unittest
import random
import time
import os
import msvcrt
import math as mt


class Matrix(object):
    """
        Cette classe permet la cretion d'un tableau a la taille de la grille de jeu.elle fournit des methodes pour
         l'initialisation d'un motif sur cette grille ainsi que pour sont deplacement lateral, verticale , sa rotation.
         todo scinder en deux classe pattern_operation et matrix
    """

    def __init__(self, line=1, column=3, fill_motif=" ", border=True):
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

    def _coordinate_to_matrix(self, coordinate_dictionary, symbole):

        for x, y_group in coordinate_dictionary.items():
            for _, y in enumerate(y_group):
                self.matrix[x][y] = symbole

    def draw_vertival(self, y):
        for line in self.matrix:
            line[y] = "#"

    def draw_message(self, mess="default message", x=10, y=6):

        for indice, _ in enumerate(self.matrix[x]):
            if y <= indice < len(mess) + y:
                self.matrix[x][indice] = mess[indice - y]

    def place_mobile_patern(self, pattern, y):
        """positione un pattern en haut, au centre de la matrice"""

        x_origin = 0  # premiere ligne (en haut) de la matrice
        # y_middle = self.column_num // 2  # milieu d'une ligne(si elle est paire ^^).
        y_middle = y
        for x in pattern.keys():  # on actualise les coordonné des items pour les placer au milieux
            self.last_coord[x_origin + x] = [y_pattern + y_middle for y_pattern in pattern[x]]

        Matrix._coordinate_to_matrix(self, self.last_coord, "0")

    def place_patern(self, pattern, motif, x, y):

        coordone = {}
        x_origin = x  # premiere ligne (en haut) de la matrice

        y_middle = y
        for x in pattern.keys():  # on actualise les coordonné des items pour les placer au milieux
            coordone[x_origin + x] = [y_pattern + y_middle for y_pattern in pattern[x]]

        Matrix._coordinate_to_matrix(self, coordone, motif)

    def _bottom_collision(self):
        collision = False

        for x, value in self.last_coord.items():
            for _, y in enumerate(value):
                if self.matrix[x + 1][y] == "O" or self.matrix[x + 1][y] == "#":
                    collision = True  # le fond de la boite ou le sommet d'une piece posé

        return collision

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

        center_x = max(self.last_coord.keys()) - 1
        for y in self.last_coord.values():
            center_y = (min(y) + ((max(y) - min(y)) // 2))

        return center_x, center_y

    def rotate(self, theta=90):

        rotated_coordinate = {}
        list_coo = []
        theta_radians = mt.radians(theta)

        center_x, center_y = Matrix._rotation_center(self)

        for x, y_group in self.last_coord.items():
            for y in y_group:
                rotated_x = round(
                    ((x - center_x) * mt.cos(theta_radians)) - ((y - center_y) * mt.sin(theta_radians))) + center_x
                rotated_y = round(
                    ((x - center_x) * mt.sin(theta_radians)) + ((y - center_y) * mt.cos(theta_radians))) + center_y
                list_coo.append((rotated_x, rotated_y))

        for couple in list_coo:
            rotated_coordinate[couple[0]] = []

        for couple in list_coo:
            rotated_coordinate[couple[0]].append(couple[1])

        if min(rotated_coordinate.keys()) > 0:  # on empeche x negatif = pas de rotation sur les premiere lignes
            Matrix._coordinate_to_matrix(self, self.last_coord, " ")
            self.last_coord = rotated_coordinate

    # --------------------------------------------------------------------------------------------------------------
    def translate(self, direction):

        Matrix._coordinate_to_matrix(self, self.last_coord, " ")  # risque d'effacement du pattern lors de l'appel a
        # translate si on commente la ligne les traces laissé ne constituent pas des points d'arrets ???

        if direction == "left" and not Matrix._side_collision(self, "left"):
            Matrix._deplacement(self, "left")
            return True

        elif direction == "right" and not Matrix._side_collision(self, "right"):
            Matrix._deplacement(self, "right")
            return True

    def _deplacement(self, direction):

        for x, y_group in self.last_coord.items():
            for indice, y in enumerate(y_group):
                if direction == "left":
                    self.last_coord[x][indice] = y - 1
                elif direction == "right":
                    self.last_coord[x][indice] = y + 1

    def down(self):

        new_coordinate = {}

        if Matrix._bottom_collision(self):
            Matrix._coordinate_to_matrix(self, self.last_coord, "O")  # ligne utile ????
            self.last_coord = {}
            return False

        else:
            for x, y in self.last_coord.items():
                new_coordinate[x + 1] = y

            Matrix._coordinate_to_matrix(self, self.last_coord, " ")
            Matrix._coordinate_to_matrix(self, new_coordinate, "0")

            self.last_coord = new_coordinate

            return True

    def __repr__(self):

        matrix_display = ""
        for line in range(len(self.matrix)):  # on concatene toute les ligne en y intercalant  un retour chariot
            matrix_display += "".join(self.matrix[line]) + "\n"

        return matrix_display


# -----------------------------------------------------------------------------------------

class Pattern(object):

    def __init__(self, choice=1):

        self.coordinate_for_display = {}  # dictionnaire qui contient les coordonés des pattern  0 = 2,3,4 de la forme
        # x = y+2, y+3, y+4

        if choice == "random":
            choice = random.randrange(1, 7)

        if choice == 1:  # truc décalé
            self.coordinate_for_display = {0: [1, 2], 1: [0, 1]}

        elif choice == 2:  # T a l'envers
            self.coordinate_for_display = {0: [1], 1: [0, 1, 2]}

        elif choice == 3:  # carre
            self.coordinate_for_display = {0: [0, 1], 1: [0, 1]}
        elif choice == 4:  # l
            self.coordinate_for_display = {0: [2], 1: [0, 1, 2]}

        elif choice == 5:  # L'autre l
            self.coordinate_for_display = {0: [0], 1: [0, 1, 2]}

        elif choice == 6:  # baton
            self.coordinate_for_display = {0: [0, 1, 2, 3]}

        else:
            print("error")

    def __repr__(self):
        return self.coordinate_for_display


# -----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    #  bugs le carré ne descensd pas si on le tourne en continue,
    #  les piece peuvent s'attacher au mur lors d'une rotation, les piece se magnetisent au mur
    line = 20
    column = 40
    level = 0.5
    play_ground = Matrix(line, column)
    score = 0


    def display_score(score):

        play_ground.draw_message("************", 5, 27)
        play_ground.draw_message(" YOUR SCORE:", 6, 27)
        play_ground.draw_message("     %s" % score, 7, 27)
        play_ground.draw_message("************", 8, 27)


    def game_over():
        continu_play_loop = True

        for column in play_ground.matrix[0]:
            if "O" in column:
                continu_play_loop = False

                play_ground.draw_message("************************", 9)
                play_ground.draw_message("*     game over        *", 10)
                play_ground.draw_message("* hit enter to quit    *", 11)
                play_ground.draw_message("************************", 12)
                print(play_ground)
                input("")

        return continu_play_loop


    def line_completed(score=0):

        for indice, line in enumerate(play_ground.matrix):
            if line[1:score_line_y] == ["O"] * (score_line_y - 1):
                del (play_ground.matrix[indice])
                # play_ground.matrix.insert(0, play_ground.matrix[0])
                score += 100
        return score


    def keyboard_input():
        car = "0"
        check = msvcrt.kbhit()
        if check:
            car = msvcrt.getch()
        return car


    score_line_y = 2 * column // 3
    play_ground.draw_vertival(score_line_y)

    display_score(score)

    play_loop = True
    piece_suivante = Pattern("random")
    while play_loop:
        play_ground.place_patern(piece_suivante.coordinate_for_display, " ", 2, 32)
        piece_en_cours = piece_suivante
        piece_suivante = Pattern("random")

        play_ground.place_patern(piece_suivante.coordinate_for_display, "0", 2, 32)
        play_ground.place_mobile_patern(piece_en_cours.coordinate_for_display, score_line_y // 2)

        continu = True
        while continu:
            start_time = time.time()
            end_time = 0
            print(play_ground)

            while end_time - start_time < level:
                end_time = time.time()

                command_carachters = keyboard_input()
                if command_carachters != 0:
                    if command_carachters == b"z":
                        play_ground.rotate()
                        break

                    elif command_carachters == b"s":
                        break

                    elif command_carachters == b"q":
                        play_ground.translate("left")

                    elif command_carachters == b"d":
                        play_ground.translate("right")

            continu = play_ground.down()
            os.system('cls')

        play_loop = game_over()
        display_score(score)
        score += line_completed()
