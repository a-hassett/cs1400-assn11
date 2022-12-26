# Alexandra Hassett, CS 1400

import random
import time


class Life:
    def __init__(self):
        self.__col = []  # set up a 22 x 22 array for the game board
        self.__row = []
        self.__nextCol = []  # set up a second 22 x 22 array
        self.__nextRow = []
        for i in range(22):
            self.__row.append([])
            self.__nextRow.append([])
            for j in range(22):
                self.__col.append(" ")
                self.__row[i].append(self.__col[i])
                self.__nextCol.append(" ")
                self.__nextRow[i].append(self.__col[i])
        self.__generations = 1

    def initialize(self):
        # set up first grid with each square having a 33% chance to be alive
        for i in range(22):
            for j in range(22):
                probability = random.randint(1, 3)
                if probability == 1:
                    active = True
                else:
                    active = False
                if active:
                    self.__row[i][j] = "X"  # alive cell
                else:
                    self.__row[i][j] = " "  # dead cell

    def nextGen(self):
        for i in range(1, 21):
            for j in range(1, 21):
                numNeighbors = 0
                # check to see if the cell's neighbors are alive and count them
                if self.__row[i-1][j-1] == "X":
                    numNeighbors += 1
                if self.__row[i][j-1] == "X":
                    numNeighbors += 1
                if self.__row[i+1][j-1] == "X":
                    numNeighbors += 1
                if self.__row[i-1][j] == "X":
                    numNeighbors += 1
                if self.__row[i+1][j] == "X":
                    numNeighbors += 1
                if self.__row[i-1][j+1] == "X":
                    numNeighbors += 1
                if self.__row[i][j+1] == "X":
                    numNeighbors += 1
                if self.__row[i+1][j+1] == "X":
                    numNeighbors += 1
                # check if the conditions for a cell to stay alive are true
                if (1 < numNeighbors < 4) and self.__row[i][j] == "X":
                    self.__nextRow[i][j] = "X"
                elif numNeighbors == 3 and self.__row[i][j] == " ":
                    self.__nextRow[i][j] = "X"
                else:
                    self.__nextRow[i][j] = " "
        # set the generation array that will be printed using the next generation array you just reset
        for i in range(22):
            for j in range(22):
                self.__row[i][j] = self.__nextRow[i][j]
        self.__generations += 1

    def printGrid(self):
        print("\n\n\n\n")
        for i in range(22):
            for j in range(22):
                print(format(self.__row[i][j], ">3s"), end="")
            print()
        print(format("Generation: ", ">35s"), end="")
        print(self.__generations)
        # pause in between generations
        time.sleep(0.3)


def main():
    game = Life()
    game.initialize()
    game.printGrid()
    for i in range(49):
        game.nextGen()
        game.printGrid()


main()
