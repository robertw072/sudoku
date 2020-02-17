# backtracking program to solve Sudoku puzzles
# programmed by Robert Williamson on 1/21/2020

# functions:

# function to print the Sudoku board
def print_board(board):
    for i in range(9):
        for j in range(9):
            print (board[i][j],) 
        print('n')

# function to find an empty cell on the board
# curr is a list variable that keeps a record of the current row and col
def find_empty(board, curr):
    for i in range(9):
        for j in range(9): 
            if (board[i][j] == 0):
                curr[0] = i
                curr[1] = j
                return True             # returns true if there is an empty cell
    return False                        # returns false if no empty cells, means we're done
            
# function to check if the number being tried is already in the current row
def in_row(board, row, num):
    for j in range(9):
        if (board[row][j] == num):
            return True                 # if this returns true, try a different number
    return False

# function to check if the number being tried is already in the current col
def in_col(board, col, num):
    for i in range(9):
        if (board[i][col] == num):
            return True
    return False

# function to check if the number is already in the current 3x3 box
def in_box(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if (board[i + row][j + col] == num):
                return True
    return False

# function the uses the previously defined functions to check if the number works in all 3
def check_safe(board, row, col, num):
    return not in_row(board, row, num) and not in_col(board, col, num) and not in_box(board, row, col, num)

# function to solve the board with backtracking!
def solve_board(board):
    # curr is the list mentioned earlier that keeps track of current row and col
    curr = [0, 0]

    # if find_empty returns false, board is solved and we are done
    if (not find_empty(board, curr)):
        return True
    
    # assign row and col from find_empty
    row = curr[0]
    col = curr[1]

    for num in range(1, 10):
        if(check_safe(board, row, col, num)):
            # make assignment if true
            board[row][col] = num

             # recurisvely return, if we're successful then good
            if (solve_board(board)):
                return True

            # if recurision not successful, make cell 0 and try again
            board[row][col] = 0

    # backtrack
    return False

# now for the main. . .

# make 2d array for board
board = [[0 for i in range(9)]for j in range(9)]

# assign vals to board
board =[[3,0,6,5,0,8,4,0,0], 
        [5,2,0,0,0,0,0,0,0], 
        [0,8,7,0,0,0,0,3,1], 
        [0,0,3,0,1,0,0,8,0], 
        [9,0,0,8,6,3,0,0,5], 
        [0,5,0,0,9,0,6,0,0], 
        [1,3,0,0,0,0,2,5,0], 
        [0,0,0,0,0,0,0,7,4], 
        [0,0,5,2,0,6,3,0,0]] 

if (solve_board(board)):
    print_board(board)
else:
    print ("No solution.\n")
