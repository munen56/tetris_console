# coding=utf-8

import os
import time
import msvcrt
import pickle

from matrice import *

#  bugs le carré ne descensd pas si on le tourne en continue,
#  les piece peuvent s'attacher au mur lors d'une rotation, les piece se magnetisent au mur

number_of_line = 20
number_of_column = 40
level = 0.5
play_ground = Matrix(number_of_line, number_of_column)
zone_de_score_y = 2 * number_of_column // 3
score = 0

#  ---------------------------------------------------------------------------------------------------------------------


def front_page():

    front_matrix = Matrix(number_of_line, number_of_column)


#  ---------------------------------------------------------------------------------------------------------------------

def display_score(score_disp):

    play_ground.draw_message("*" * (number_of_column-zone_de_score_y-2), 5, zone_de_score_y + 1)
    play_ground.draw_message(" YOUR SCORE:", 6, zone_de_score_y + 1)
    play_ground.draw_message("     %s" % score_disp, 7, zone_de_score_y + 1)
    play_ground.draw_message("*" * (number_of_column-zone_de_score_y-2), 8, zone_de_score_y + 1)

#  ---------------------------------------------------------------------------------------------------------------------


def game_over():

    continu_play_loop = True

    for column in play_ground.matrix[0]:
        if "O" in column:
            continu_play_loop = False

            play_ground.draw_message("************************", 9, 6)
            play_ground.draw_message("*     game over        *", 10, 6)
            play_ground.draw_message("* hit enter to quit    *", 11, 6)
            play_ground.draw_message("************************", 12, 6)
            print(play_ground)
            input("")

    return continu_play_loop

#  ---------------------------------------------------------------------------------------------------------------------


def line_completed(next_score):

    for indice, line in enumerate(play_ground.matrix):

        if line[1:zone_de_score_y] == ["O"] * (zone_de_score_y - 1):

            slide_down_playground(indice)
            next_score += 100

    return next_score

#  ---------------------------------------------------------------------------------------------------------------------
def slide_down_playground(start_index):

    start_index
    for index in reversed(range(1, start_index + 1)):
        play_ground.matrix[index][1:zone_de_score_y] = play_ground.matrix[index-1][1:zone_de_score_y]


#  ---------------------------------------------------------------------------------------------------------------------

def keyboard_input():

    input_character = "0"
    is_character_in_buffer = msvcrt.kbhit()
    if is_character_in_buffer:
        input_character = msvcrt.getch()

    return input_character

#  ---------------------------------------------------------------------------------------------------------------------

def load_previous_score():

    previous_score = pickle.load(open('score_log', 'rb'))
    print("score :", previous_score)

def save_new_score(current_score):
    save_list = []
    player_name = input("JOUEUR !...Quel est ton nom ?")


    save_list.append((player_name, current_score))

    pickle.dump(save_list, open('score_log', 'wb'))

#  ---------------------------------------------------------------------------------------------------------------------



play_ground.draw_vertival(zone_de_score_y)

display_score(score)

play_loop = True
piece_suivante = Pattern("random")
while play_loop:
    play_ground.place_patern(piece_suivante.coordinate_for_display, " ", 2, zone_de_score_y + 3)
    piece_en_cours = piece_suivante
    piece_suivante = Pattern("random")

    play_ground.place_patern(piece_suivante.coordinate_for_display, "0", 2, zone_de_score_y + 3)
    play_ground.place_mobile_patern(piece_en_cours.coordinate_for_display, zone_de_score_y // 2)

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
    score = line_completed(score) # why not score en variable global ?
    display_score(score)

#save_new_score(score)
#load_previous_score()


