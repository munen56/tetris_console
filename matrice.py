# coding=utf-8
import unittest


class Matrix(object):


    def __init__(self, line=1, column=3, fill_motif="O", border=True):


        self.line_num = line
        self.column_num = column
        self.fill_motif = fill_motif
        self.border = border
        self.matrix_col = []
        self.matrix = []



        self.matrix_col = list(self.fill_motif * self.column_num) # on créé une ligne contenant le nombre de colonne désiré ( column_num)
        self.matrix = [self.matrix_col for j in range(self.line_num)] # on repete la ligne de matrix_col autant de fois qu'il nous faut de ligne (line_num)

        if self.border :
            for ind, val in enumerate(self.matrix):
                self.matrix[ind][0] = "#"
                self.matrix[ind][self.column_num -1] =  "#"
            self.matrix[self.line_num - 1] = list("#" * self.column_num)


    def __repr__(self):


        matrix_display = ""
        for line in range(len(self.matrix)): # on concatene toute les ligne en y intercalant  un retour chariot
            matrix_display += "".join(self.matrix[line]) + "\n"

        return matrix_display





play_ground = Matrix(40, 80)
print(play_ground)