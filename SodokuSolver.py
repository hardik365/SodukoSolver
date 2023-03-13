import numpy as np

#Feel free to change these numbers to your liking!
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]



print("This is how the board looks at the start!:\n")
print(np.matrix(grid))
print("\n")

#This fuction will check if the numnber repeats
def possible(row, column, number):
    global grid

    #Checks if the number is already in the given row
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Checks if the number is already in the given column
    for i in range(0,9):
        if grid[i][column] == number:
            return False
            
    #Checks if the number is already in the given square
    xx = (column // 3) * 3 #Needed to check the square
    yy = (row // 3) * 3 #Needed to check the square
    for i in range(0,3):
        for j in range(0,3):
            if grid[yy + i][xx + j] == number:
                return False
    return True

#This will actually solve it, uses backtracking algorithm 
def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return        
    print("This is one solution:\n")        
    print(np.matrix(grid))
    temp = input("See more possible solutions (if any?)")

solve()