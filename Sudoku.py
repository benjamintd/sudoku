#Sudoku.py

###############################################################################
### Sudoku class
###############################################################################


class Sudoku(object):
    """Sudoku class.

    A sudoku is instanciated from a list of lists (9x9 matrix) and
    has a solve method that returns a solved sudoku object.
    """

    SIZE = 9    # Size of the grid.
    SQUARE = 3  # Size of a square.

    def __init__(self, initial_grid):
        """Init method of a sudoku object.

        We assume initial_grid is a 9 x 9 list of lists,
        with only integer values.
        """
        self.grid = copy(initial_grid)
        self.size = self.SIZE
        self.fillable = True

    def row(self, i):
        """Return a list of all non 0 numbers in row i."""
        row = self.grid[i][:]
        row = filter(lambda x: x != 0, row)
        return row

    def column(self, j):
        """Return a list of all non 0 numbers in column j."""
        column = [self.grid[i][j] for i in range(self.size)]
        column = filter(lambda x: x != 0, column)
        return column

    def square(self, k):
        """Return a list of all non 0 numbers in square k."""
        row_indices = map(lambda x: x+self.SQUARE*(k / self.SQUARE),
                          range(self.SQUARE))
        col_indices = map(lambda x: x+self.SQUARE*(k % self.SQUARE),
                          range(self.SQUARE))
        square = [self.grid[i][j] for i in row_indices for j in col_indices]
        square = filter(lambda x: x != 0, square)
        return square

    def check_row(self, i):
        """Check if row i is correct."""
        row = self.row(i)
        return all_different(row)

    def check_column(self, j):
        """Check if column j is correct."""
        column = self.column(j)
        return all_different(column)

    def check_square(self, k):
        """Check if square k is correct."""
        square = self.square(k)
        return all_different(square)

    @property
    def valid(self):
        """Check if a sudoku grid is valid.

        A grid is valid if there is no contradiction within a row,
        column or square.
        """
        valid = True
        for i in range(self.size):
            valid = (valid and
                     self.check_column(i) and
                     self.check_row(i) and
                     self.check_square(i))
        return valid

    @property
    def feasible(self):
        """Check if all empty cells have at least one possible fill."""
        for i in range(self.size):
            for j in range(self.size):
                if self.possible_values(i, j) == []:
                    return False
        return True

    def possible_values(self, i, j):
        """Return a list of possible values a cell can take.

        For coordinates (i,j), return a list of integers that do
        not break validity.
        """
        k = is_in_sq(i, j)
        possible = []
        if self.grid[i][j] != 0:
            return [self.grid[i][j]]
        else:
            for n in range(1, self.size+1):
                if (n not in self.row(i)) and\
                   (n not in self.column(j)) and\
                   (n not in self.square(k)):
                    possible.append(n)
            return possible

    @property
    def possibility_grid(self):
        """Return a matrix of lists of possible values.

        For each cell (i,j), p_grid[i][j] contains the list of all
        possible values that cell (i,j) can take without breaking
        validity."""
        p_grid = empty_grid(self.size)
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] != 0:
                    p_grid[i][j] = [self.grid[i][j]]
                else:
                    p_grid[i][j] = self.possible_values(i, j)
        return p_grid

    def fill(self):
        """Fill the cells that are certain without assumptions.

        If some cells have only one possible value, then we can fill
        them with certainty. This function fills the grid with all
        certain values, and reiterates until the possibility grid does
        not change anymore.
        """
        if not self.fillable:
            return self
        else:
            p_grid = self.possibility_grid
            #fill all certain cells
            for i in range(self.size):
                for j in range(self.size):
                    p_list = p_grid[i][j]
                    if len(p_list) == 1:
                        self.grid[i][j] = p_list[0]
                    else:
                        pass
            #if it is the same, we cannot fill any more cells with certainty.
            if p_grid == self.possibility_grid:
                self.fillable = False
            # otherwise, repeat
            self.fill()

    @property
    def solved(self):
        """Check if a grid is solved (completely full and valid)."""
        all_filled = True
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    all_filled = False
        return all_filled and self.valid

    def find_disjunction(self):
        """Return a disjunction tuple (i, j, values).

        * (i,j) is an empty cell
        * values is the list of possible values of that cell.
        * We do a disjunction on cells with the least possible
        number of hypothetical values, hopefully 2.
        """
        min_l = self.SIZE  # The list cannot be bigger than 9
        values = []
        min_i = -1
        min_j = -1
        for i in range(self.size):
            for j in range(self.size):
                p_list = self.possibility_grid[i][j]
                l = len(p_list)
                if l == 1:
                    pass
                elif l == 2:  # No need to search for a shorter list.
                    return i, j, p_list
                else:  # p_list has length >= 3.
                       # We keep track of the shortest disjunction set so far.
                    if len(p_list) < min_l:
                        min_i = i
                        min_j = j
                        values = p_list
        return min_i, min_j, values

    def sudoku_son(self, i, j, val):
        """Return self's son for the (i, j) disjunction for val."""
        grid = copy(self.grid)
        grid[i][j] = val
        son = type(self)(grid)
        return son

    def solve(self):
        """Recursive function for solving a grid."""
        # if the grid is not feasible or not valid, cut the branch.
        if (not self.feasible) or (not self.valid):
            return None
        else:  # Grid is still valid
            self.fill()
            if self.solved:
                return self
            else:  # Disjunction is needed
                i, j, list = self.find_disjunction()
                # we solve each disjunction case
                for val in list:
                    son = self.sudoku_son(i, j, val)
                    solved_son = son.solve()
                    if solved_son is None:  # Disjunction case is infeasible
                        pass
                    else:
                        return solved_son  # We found the solution!

    def __repr__(self):
        """Print a grid."""
        string = ''
        for i in range(self.size):
            for j in range(self.size):
                val = self.grid[i][j]
                if val == 0:
                    string += '. '
                else:
                    string += str(self.grid[i][j]) + ' '
                if j % self.SQUARE == self.SQUARE - 1:
                    string += ' '
            if i % self.SQUARE == self.SQUARE - 1:
                string += '\n'
            string += '\n'
        return string

###############################################################################
### Utilities
###############################################################################


def all_different(l):
    return not len(l) > len(set(l))


def is_in_sq(i, j):
    k = 3*(i/3) + (j/3)
    return k


def empty_grid(size):
    return [[None for _ in range(size)] for _ in range(size)]


def copy(grid):
    copy = empty_grid(len(grid))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            copy[i][j] = grid[i][j]
    return copy
