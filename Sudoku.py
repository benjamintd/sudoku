#sudoku solver

class Sudoku(object):
    
    def __init__(self, initial_grid):
        '''initiates a sudoku object. 
        We assume initial_grid is a 9 x 9 list of lists,
        with only integer values'''
        self.grid = copy(initial_grid)
        self.size = 9
        self.p_grid = self.possibility_grid()
        self.valid = self.is_valid()
        self.feasible = self.is_feasible()
        self.solved = self.is_solved()
        self.fillable = True
     
    def __str__(self):
        '''Allows for printing a grid'''
        string = ''
        for i in range(self.size):
            for j in range(self.size):
                val = self.grid[i][j]
                if val == 0:
                    string += '. '
                else: 
                    string += str(self.grid[i][j]) + ' '
            string += '\n'
        return string
        
    def row(self, i):
        '''returns a list of all non 0 numbers in row i'''
        row = self.grid[i][:]
        row = filter(lambda x: x!=0, row)
        return row
        
    def column(self, j):
        '''returns a list of all non 0 numbers in column j'''
        column = [self.grid[i][j] for i in range(self.size)]
        column = filter(lambda x: x!=0, column)
        return column
        
    def square(self, k):
        '''returns a list of all non 0 numbers in square k'''
        row_indices = map(lambda x: x+3*(k/3), [0,1,2])
        col_indices = map(lambda x: x+3*(k%3), [0,1,2])
        square = [self.grid[i][j] for i in row_indices for j in col_indices]
        square = filter(lambda x: x!=0, square)
        return square
        
    def check_row(self, i):
        '''checks if row i is correct'''
        row = self.row(i)
        return all_different(row)     

    def check_column(self, j):
        '''checks if column j is correct'''
        column = self.column(j)
        return all_different(column)
    
    def check_square(self, k):
        '''checks if square k is correct'''
        square = self.square(k)
        return all_different(square)
        
    def is_valid(self):
        '''checks if a sudoku grid is valid, meaning there
        exists no contradiction in a row, column or square'''
        valid = True
        for i in range(self.size):
            valid = valid and\
                      self.check_column(i) and\
                      self.check_row(i) and\
                      self.check_square(i)
        return valid
    
    def is_feasible(self):
        '''if there exists a cell with zero possible values, then 
        the grid is infeasible.'''
        for i in range(self.size):
            for j in range(self.size):
                if self.possible_values(i,j) == []:
                    return False
        return True   
        
    def possible_values(self, i, j):
        '''for coordinates (i,j), returns a list of possible values
        the cell can take, without breaking validity'''
        k = is_in_sq(i,j)
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

    def possibility_grid(self):
        '''Returns a matrix of lists p_grid built in the following way:
        for each cell (i,j), p_grid[i][j] contains the list of all possible values
        that cell (i,j) can take without breaking validity'''
        p_grid = empty_grid(self.size)
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] != 0:
                    p_grid[i][j] = [self.grid[i][j]]
                else:
                    p_grid[i][j] = self.possible_values(i,j)
        return p_grid

    def fill(self):
        '''If some cells have only one possible value, then we can fill
        them with certainty. This function fills the grid with all
        certain values, and reiterates until the possibility grid does 
        not change anymore.'''
        if self.fillable == False:
            return None
        else: 
            #fill all certain cells
            for i in range(self.size):
                for j in range(self.size):
                    p_list = self.p_grid[i][j]
                    if len(p_list)==1:
                        self.grid[i][j] = p_list[0]
                    else:
                        pass
            #compute an updated possibility grid
            new_p_grid = self.possibility_grid()
            #if it is the same, we cannot fill any more cells with certainty. 
            if new_p_grid == self.p_grid:
                self.fillable = False
            self.p_grid = new_p_grid
            # otherwise, repeat
            self.fill()
    
    def is_solved(self):
        '''checks if a grid is solved (completely
        full and valid)'''
        all_filled = True
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    all_filled = False
        return all_filled and self.is_valid()
     
    def find_disjunction(self):
        '''returns a tuple (i, j, list) such that:
        (i,j) is an empty cell
        list is the list of possible values of that cell. 
        We do a disjunction on cells with the least possible
        number of hypothetical values, hopefully 2.'''
        min_l = 9 #the list cannot be bigger than 9
        list = []
        min_i = -1
        min_j = -1
        for i in range(self.size):
            for j in range(self.size):
                p_list = self.p_grid[i][j]
                l = len(p_list)
                if l == 1:
                    pass
                elif l == 2: #no need to search for a shorter list
                    return i, j, p_list
                else: # p_list has length >= 3. 
                    #We keep track of the shortest disjunction set so far
                    if len(p_list) < min_l:
                        min_i = i
                        min_j = j
                        list = p_list
        return min_i, min_j, list      
        
    def solve(self):
        '''Recursive function for solving a grid'''
        # if the grid is not feasible or not valid, cut the branch. 
        if (not self.feasible) or (not self.valid):
            return None
        else: #grid is still valid
            self.fill()
            if self.is_solved():
                return self
            else: #disjunction is needed
                i, j, list = self.find_disjunction()
                # we solve each disjunction case
                for val in list:
                    son = sudoku_son(self, i, j, val)
                    solved_son = son.solve()
                    if solved_son == None: #disjunction case is infeasible
                        pass
                    else:
                        return solved_son #we found the solution!

             
###########
# SUBROUTINES
###########
    
def all_different(list):
        return not len(list) > len(set(list))

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
    
def sudoku_son(sudoku, i, j, val):
    grid = copy(sudoku.grid)
    grid[i][j] = val
    son = Sudoku(grid)
    return son