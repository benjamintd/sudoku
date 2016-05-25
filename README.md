## Sudoku

This is a simple python script for Sudoku solving from command line.

#### Usage

`python solve_sudoku.py grid`

where `grid` is a string of 81 numerical characters representing the initial, unsolved grid. Empty cells are filled with zeros.
Your solved grid will print on the console.

#### Example

```
$ python solve_sudoku.py 000010020000000609600802310800200000007060000020004050000700804130000090050000000

-- original grid -- 

. . .  . 1 .  . 2 .  
. . .  . . .  6 . 9  
6 . .  8 . 2  3 1 .  

8 . .  2 . .  . . .  
. . 7  . 6 .  . . .  
. 2 .  . . 4  . 5 .  

. . .  7 . .  8 . 4  
1 3 .  . . .  . 9 .  
. 5 .  . . .  . . .  


-- solved grid -- 

5 7 3  6 1 9  4 2 8  
2 8 1  5 4 3  6 7 9  
6 4 9  8 7 2  3 1 5  

8 1 5  2 3 7  9 4 6  
4 9 7  1 6 5  2 8 3  
3 2 6  9 8 4  7 5 1  

9 6 2  7 5 1  8 3 4  
1 3 8  4 2 6  5 9 7  
7 5 4  3 9 8  1 6 2  


solved in 1.55 sec.
```
