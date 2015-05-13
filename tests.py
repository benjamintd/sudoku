# tests.py

import unittest
from Sudoku import *


test_grid = [[0, 0, 0, 0, 1, 0, 0, 2, 0],
                 [0, 0, 0, 0, 0, 0, 6, 0, 9],
                 [6, 0, 0, 8, 0, 2, 3, 1, 0],
                 [8, 0, 0, 2, 0, 0, 0, 0, 0],
                 [0, 0, 7, 0, 6, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 4, 0, 5, 0],
                 [0, 0, 0, 7, 0, 0, 8, 0, 4],
                 [1, 3, 0, 0, 0, 0, 0, 9, 0],
                 [0, 5, 0, 0, 0, 0, 0, 0, 0]]
                
invalid_grid = [[0, 0, 0, 0, 1, 0, 0, 2, 0],
                   [0, 0, 0, 0, 0, 0, 6, 0, 9],
                   [6, 0, 0, 8, 0, 2, 3, 1, 0],
                   [8, 0, 0, 2, 0, 0, 0, 0, 0],
                   [0, 0, 7, 0, 6, 0, 0, 0, 0],
                   [0, 2, 0, 0, 0, 4, 0, 5, 0],
                   [0, 0, 0, 7, 0, 0, 8, 0, 4],
                   [1, 3, 0, 0, 0, 0, 0, 9, 0],
                   [0, 5, 0, 0, 0, 7, 0, 0, 0]]
                   
infeasible_grid = [[0, 9, 0, 0, 1, 3, 0, 2, 0],
                       [7, 0, 0, 0, 0, 0, 6, 0, 9],
                       [6, 4, 5, 8, 0, 2, 3, 1, 0],
                       [8, 0, 0, 2, 0, 0, 0, 0, 0],
                       [0, 0, 7, 0, 6, 0, 0, 0, 0],
                       [0, 2, 0, 0, 0, 4, 0, 5, 0],
                       [0, 0, 0, 7, 0, 0, 8, 0, 4],
                       [1, 3, 0, 0, 0, 0, 0, 9, 0],
                       [0, 5, 0, 0, 0, 7, 0, 0, 0]]

solved_grid = [[5, 7, 3, 6, 1, 9, 4, 2, 8],
                    [2, 8, 1, 5, 4, 3, 6, 7, 9],
                    [6, 4, 9, 8, 7, 2, 3, 1, 5],
                    [8, 1, 5, 2, 3, 7, 9, 4, 6],
                    [4, 9, 7, 1, 6, 5, 2, 8, 3],
                    [3, 2, 6, 9, 8, 4, 7, 5, 1],
                    [9, 6, 2, 7, 5, 1, 8, 3, 4],
                    [1, 3, 8, 4, 2, 6, 5, 9, 7],
                    [7, 5, 4, 3, 9, 8, 1, 6, 2]]

easy_grid = [[0, 4, 0, 9, 0, 5, 0, 8, 0],
                 [6, 0, 1, 0, 4, 0, 3, 0, 2],
                 [0, 5, 0, 0, 0, 0, 0, 7, 0],
                 [7, 0, 0, 4, 0, 2, 0, 0, 1],
                 [0, 3, 0, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 3, 0, 6, 0, 0, 7],
                 [0, 8, 0, 0, 0, 0, 0, 2, 0],
                 [9, 0, 5, 0, 3, 0, 6, 0, 4],
                 [0, 2, 0, 7, 0, 1, 0, 9, 0]]
                    
class TestSudoku(unittest.TestCase):
        
    def test_check_row(self):
        sudoku = Sudoku(test_grid)
        for i in range(sudoku.size):
            self.assertEqual(sudoku.check_row(i), True)
            
    def test_check_column(self):
        sudoku = Sudoku(test_grid)
        for i in range(sudoku.size):
            self.assertEqual(sudoku.check_column(i), True)
            
    def test_check_square(self):
        sudoku = Sudoku(test_grid)
        for i in range(sudoku.size):
            self.assertEqual(sudoku.check_square(i), True)
            
    def test_is_valid(self):
        true_grid = Sudoku(test_grid)
        false_grid = Sudoku(invalid_grid)
        self.assertEqual(true_grid.is_valid(), True)
        self.assertEqual(false_grid.is_valid(), False)
        
    def test_possible_values(self):
        sudoku = Sudoku(test_grid)
        self.assertEqual(sudoku.possible_values(0,0), [3,4,5,7,9])
        
    def test_is_feasible(self):
        true_grid = Sudoku(test_grid)
        false_grid = Sudoku(infeasible_grid)
        self.assertEqual(true_grid.is_feasible(), True)
        self.assertEqual(false_grid.is_feasible(), False)
    
    def test_possibility_grid(self):
        sudoku = Sudoku(test_grid)
        p_grid = sudoku.possibility_grid()
        self.assertEqual(p_grid[0][0], [3,4,5,7,9])
        self.assertEqual(p_grid[0][4], [1])
        
    def test_is_solved(self):
        true_grid = Sudoku(solved_grid)
        false_grid = Sudoku(test_grid)
        self.assertEqual(true_grid.is_solved(), True)
        self.assertEqual(false_grid.is_solved(), False)
        
    def test_fill(self):
        sudoku = Sudoku(easy_grid)
        sudoku.fill()
        self.assertEqual(sudoku.is_solved(), True)
        self.assertEqual(sudoku.is_feasible(), True)
        original_values = True
        for i in range(sudoku.size):
            for j in range(sudoku.size):
                val = easy_grid[i][j]
                equal = (val == 0 or val == sudoku.grid[i][j])
                original_values = original_values and equal
        self.assertEqual(original_values, True)
        
    def test_find_disjunction(self):
        sudoku = Sudoku(test_grid)
        i, j, list = sudoku.find_disjunction()
        self.assertEqual(i, 2)
        self.assertEqual(j, 8)
        self.assertEqual(list, [5,7])
        
    def test_solve(self):
        sudoku = Sudoku(test_grid)
        solved = sudoku.solve()
        self.assertEqual(solved.is_valid(), True)
        self.assertEqual(solved.is_feasible(), True)
        self.assertEqual(solved.is_solved(), True)
        original_values = True
        for i in range(sudoku.size):
            for j in range(sudoku.size):
                val = test_grid[i][j]
                equal = (val == 0 or val == solved.grid[i][j])
                original_values = original_values and equal
        self.assertEqual(original_values, True)
       
class TestSubroutines(unittest.TestCase):        
    def test_all_different(self):
        all_diff = [1,2,3,4,5,6,7,8,9]
        not_diff = [1,1,3,4,5,6,7,8,9]
        self.assertEqual(all_different(all_diff), True)
        self.assertEqual(all_different(not_diff), False)
        
    def test_is_in_sq(self):
        self.assertEqual(is_in_sq(4,3), 4)
        self.assertEqual(is_in_sq(6,0), 6)
        
    def test_sudoku_son(self):
        sudoku = Sudoku(test_grid)
        son = sudoku_son(sudoku, 1, 2, 3)
        self.assertEqual(son.grid[1][2], 3)
        
if __name__ == '__main__':
    unittest.main()
    