# script.py

import time
from argparse import ArgumentParser
from Sudoku import Sudoku

def parse_grid(s):
    """Parse a grid from a string.

    Assumes the string reads the grid line by line,
    and contains 81 numerical characters.
    """
    s = s.strip()
    if not (len(s) == 81 and s.isdigit()):
        raise Exception("The grid does not have the right length or contains" +
                        " non-number characters.")
    return [map(int, list(s[i:i+9])) for i in range(0, len(s), 9)]

if __name__ == '__main__':
    parser = ArgumentParser(description="Solve a Sudoku.")
    parser.add_argument('grid',
                        help="The grid, read line by line as a string of 81 " +
                             "numerical characters. Zeroes represent empty '" +
                             "cells.")
    grid = parse_grid(parser.parse_args().grid)
    sdk = Sudoku(grid)
    print "\n-- original grid -- \n"
    print sdk
    print "-- solved grid -- \n"
    t_ini = time.time()
    solved = sdk.solve()
    t_end = time.time()

    print solved
    print "solved in %.2f sec." % (t_end - t_ini)
