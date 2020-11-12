# Sudoku Solver w/ Backtracking


board = [
    [4,0,0,6,0,0,3,0,0],
    [0,0,2,8,0,0,4,0,0],
    [3,0,0,5,9,0,0,0,0],
    [0,7,0,0,0,0,0,0,2],
    [0,2,0,0,3,0,0,1,5],
    [1,0,0,9,0,0,0,0,4],
    [0,0,0,1,7,0,9,0,0],
    [0,0,0,0,0,0,0,2,8],
    [0,9,0,0,0,0,0,0,3]
]


def solve(bo):

    find = find_empty(bo) # Finds the next empty space in the board
    if not find: # If there are no more empty spaces left in the board we can say that the board has been solved
        return True
    else: # Else we assign row, col to the empty space
        row, col = find

    for i in range(1,10): # Loop through all possible numbers
        if valid(bo, i, (row,col)): # Check if the number is valid in that space
            bo[row][col] = i # If it is valid we assign the number to the board
            if solve(bo):
                return True # If the solve returns True it means there are no more empty spaces left in the board
            bo[row][col] = 0 # Else backtracks as the number was not valid
    return False


def valid(bo, num, pos):

    # Check row
    for i in range(len(bo[0])): # Loops through the row
        if bo[pos[0]][i] == num and pos[1] != i: # If any position in that row equals the number, return False
            return False

    # Check col
    for i in range(len(bo)): # Loops through the column
        if bo[i][pos[1]] == num and pos[0] != i: # If any position in that row equals the number, return False
            return False

    # Check box
    box_x = pos[1] // 3 # Finds what 3x3 box in the board the number is in
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3): # Loops though every col inside that box
        for j in range(box_x * 3, box_x*3 + 3): # Loops through every row inside that box
            if bo[i][j] == num and (i,j) != pos: # If any position inside the box equals the number, return False
                return False

    return True # If none of the checks returns False, then we can say that the number is valid


def find_empty(bo):
    for i in range(len(bo)): # Loops through every row
        for j in range(len(bo[0])): # Loops through every col
            if bo[i][j] == 0: # If the position is empty
                return i ,j # Return co-ordinates

    return None # There are no empty positions left


def print_board(bo):
    for i in range(len(bo)): # Loops through every row
        if i % 3 == 0 and i != 0: # If the row equals either 3, 6, or 9
            print("- - - - - - - - - - - - - ") # Print a separating line, this separates the board into 9 boxes

        for j in range(len(bo[0])): # Loops through every col
            if j % 3 == 0 and j!= 0: # If the column equals either 3, 6, or 9
                print(" | ", end = "") # Print a separating character, separates the board into 9 boxes

            if j == 8: # If position is the final column
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "") # Adds a space to make board more readable


print_board(board)
solve(board)
print("\n")
print_board(board)
