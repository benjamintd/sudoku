# script.py
from Sudoku import *
import time
                 
test_grid =[[8, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 6, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 7, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8],
                [0, 0, 8, 5, 0, 0, 0, 1, 0],
                [0, 9, 0, 0, 0, 0, 4, 0, 0]]
                 
sdk = Sudoku(test_grid)
print "\n-- original grid -- \n"
print sdk 
print "-- solved grid -- \n"
t_ini = time.time()
solved = sdk.solve()
t_end = time.time()

print solved
print "solved in %.2f sec." % (t_end - t_ini)
