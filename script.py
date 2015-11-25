# script.py

from Sudoku import Sudoku
import time

grid = [[0, 0, 0, 0, 1, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 9],
        [6, 0, 0, 8, 0, 2, 3, 1, 0],
        [8, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 6, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 4, 0, 5, 0],
        [0, 0, 0, 7, 0, 0, 8, 0, 4],
        [1, 3, 0, 0, 0, 0, 0, 9, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0]]


if __name__ == '__main__':
    sdk = Sudoku(grid)
    print "\n-- original grid -- \n"
    print sdk
    print "-- solved grid -- \n"
    t_ini = time.time()
    solved = sdk.solve()
    t_end = time.time()

    print solved
    print "solved in %.2f sec." % (t_end - t_ini)
