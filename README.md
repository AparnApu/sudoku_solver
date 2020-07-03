# Sudoku Solver

## Table of Contents
- [Introduction](#Introduction)
- [Motivation](#Motivation)
- [Working](#Working)
- [Contributions](#Contributions)

<!-- toc -->

## Introduction
This program solves a sudoku board using the backtracking algorithm.

## Motivation
Sudoku has a been a puzzle I have seen and solved a lot, but only manually - in school newspapers and puzzle books. So the idea of getting the computer to solve it for me was very exciting. Working with recursion is always very frustrating - but I enjoyed writing this code beacuse the result was very satisfying. I could solve something that took me hours in a couple of seconds now!

## Working
This code uses the backtracking algorithm to solve the sudoku board recursively. Backtracking is simply returning to the previous step or solution as soon as we find that current solution cannot be used to solve the problem.
  
**The basic algorithm is as follows:**  
  
Starting off with an incomplete board (empty spaces represented by zeroes),  
 
 1.  Find an empty/ unassigned space (marked with 0)
 2.  Attempt to place digits from 1-9 in that space
 3.  Check if that digit is valid in that space (i.e, it should not recur in that column, row or 3×3 subgrid)  
 4. Next,  
    a. If that digit is valid, we recursively try to solve the entire board using steps 1-3  
    b. Else, we reset that space we just filled with the next digit and return to step 3  
 5. Once the board has been fully filled (no unassigned/ empty space), we have found our solution!  
   
  
  
 **To run the code:**    
   
  1. You can either input your own sudoku board as a string.   
    
      Like this: "000260701 680070090 190004500 820100040 004602900 050003028 009300074 040050036 703018000"  
      The code accepts your input with spaces/ without spaces.  
      
  2. You can also input the unsolved sudoku board as a textfile.   
     Two default text files have been provided under the puzzled folder (default_board1 and default_board2).  
     
The code asks you which one you would rather prefer, and based on your input, it will run on the default inputs I have built in. To change the inputs, these are the code snippets to modify (lines 24 - 32):    

### Code snippet to modify:

```
    if pref == '0':
        sud_string = "000260701 680070090 190004500 820100040 004602900 050003028 009300074 040050036 703018000"
    
    elif pref == '1':
        f = open(r'.\puzzles\default_board2.txt', 'r')
        sud_string = f.read()
        f.close()
    
    else:
        print('Invalid option selected. Try again')
        sys.exit()
```
    
 ## Contributions
Open to contributions! Fork the repo, edit it and commit your change.
