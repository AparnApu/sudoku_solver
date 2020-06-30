import numpy as np
import sys

###############################################################
# function craetes a sudoku board (9*9)
# sudoku board is a 2D numpy array
###############################################################

def create_board():
    
    '''
    Function to create a sudoku board (9*9).
    Either as a directly inputed string, or as a text file read.

            Parameters:
                    none

            Returns:
                    Sudoku board (2D numpy array /numpy.ndarray)
    '''
    
    pref = input('Enter 0 for built in puzzle or 1 for puzzle to be read from default text file > ')
    
    if(pref == '0'):
        sud_string = "000260701 680070090 190004500 820100040 004602900 050003028 009300074 040050036 703018000"
    
    elif(pref == '1'):
        f = open(r'.\puzzles\default_board2.txt', 'r')
    
        sud_string= f.read()
    
        f.close()
    
    else:
        print('Invalid option selected. Try again')
        sys.exit()
        
    
    board = [[0 for i in range(9)] for j in range(9)]
    
    sud_string = "".join(sud_string.split())
    
    slice_loc = np.arange(0,len(sud_string)+1,9)
    
    for i in range(9):
        row = sud_string[slice_loc[i]:slice_loc[i+1]]
        for j in range(9):
           board[i][j] = int(row[j])
     
    board = np.array(board)
    
    print()
    print("Your unsolved board:")
    print()
    
    print_board(board)
    print()
    print()
    
    return board

###############################################################
# function prints the sudoku board
###############################################################
    
def print_board(board):
    
    '''
    Prints the sudoku board.

            Parameters:
                    board (numpy.ndarray)

            Returns:
                    none
    '''
    
    for i in range(9):
        
        for j in range(9):
        
            print(board[i][j], end = ' ')
            
            if(j ==  2 or j == 5):
                 print('|', end = " ")
            
        if(i == 2 or i == 5):
            print()
            print('-'*21, end = " ")
        
        print()
        
###############################################################
# function to find an unassigned location in the board (marked with 0)
# if empty location is found, the coordinates of the cell are returned as tuple
###############################################################

def find_empty(board):
    
    '''
    Finds any empty (unassigned locations on the board, i.e, marked with zero)

            Parameters:
                    board (numpy.ndarray)

            Returns:
                    none
    '''
    
    for i in range(9):
        
        for j in range(9):
            
            if(board[i][j] == 0):
                return(i, j)       # row, col of empty location
            
    return None

###############################################################
# function to check if the assigned number is valid
# checks in the row, col and 3*3 subgrid
###############################################################
    
def if_valid(board, num, pos):
    
    '''
    Function to check if assigned number (1-9) is valid in that row, col or 3*3 subgrid.

            Parameters:
                    board (numpy.ndarray), num (int), pos (tuple)

            Returns:
                    none
    '''
    
    row, col = pos               # row, col are location of unassigned cell
    
    for i in range(9):
        if(board[row][i] == num):
            return False
    
    for i in range(9):
        if(board[i][col] == num):
            return False
        
    row_start = (row//3) * 3       # starting location of the 3*3 subgrid to which unassigned cell belongs to
    col_start = (col//3) * 3
    
    for i in range(3):
        for j in range(3):
            if(board[row_start + i][col_start + j] == num):
                return False
    
    return True

###############################################################
# function that solves the sudoku
    # Step 1: find if an empty location exits (if no, then the sudoku board is solved. Print the board)
    # Step 2: fill the empty location (found above) with a digit from 1-9
    # Step 3: Then check whether that digit is valid in that location. If yes, a tentative assignment is made.
# with these steps complete, the rest of the board is tried, if a solution is found, return true.
# else, we reassign the digit
###############################################################
    
def solve_sudoku(board):
    
    '''
    Recursive function to solve sudoku board.

            Parameters:
                    board (numpy.ndarray)

            Returns:
                    True/False (boolean)
    '''
    
    empty = find_empty(board)
    
    if not empty:
        return True
    else:
        row, col = empty
        
    for i in range(1, 10):
        if(if_valid(board, i, (row, col))):
            board[row][col] = i
            
            if(solve_sudoku(board)):
                return True
            
            board[row][col] = 0
            
    return False

###############################################################
# main function
###############################################################
    
def main():
    
    '''
    Main function.
    
            Parameters:
                    none

            Returns:
                    none
    '''
    
    board = create_board()
    print("Your puzzle is being solved...")
    print("Your solved board is:")
    solve_sudoku(board)
    print_board(board)
    
main()