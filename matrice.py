import unittest


class Matrix(object):


    def __init__(self, line=1, column=3, **border=bottom, left, right):
        self.line = line
        self.column = column
        self.border = **border
        self.matrix = []



        for i in range(self.column + 1): # on cree les colonne
            self.matrix.append(" ")



    def __repr__(self):

        #2) on affiche toute la grille
        for x in range(len(grid)):
            return   print("".join(grid[x]))






Matrix(5, 5)