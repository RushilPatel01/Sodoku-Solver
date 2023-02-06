board = [
    [0,3,2,0,4,0,0,0,0],
    [4,1,0,0,0,0,0,2,6],
    [0,0,0,9,0,0,3,0,0],
    [0,0,0,8,6,0,2,0,5],
    [1,0,0,0,2,0,0,0,0],
    [0,0,8,4,0,0,0,3,9],
    [6,0,0,0,9,5,0,0,0],
    [9,8,1,0,7,3,4,0,2],
    [0,2,5,0,8,4,6,9,7]
]

def solve_sodoku(sodoku_board):

    find = get_empty_square(sodoku_board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if valid(sodoku_board, i, (row, column)):
            sodoku_board[row][column] = i

            if solve_sodoku(sodoku_board):
                return True

            sodoku_board[row][column] = 0

    return False


def valid(sodoku_board, number, position):

    # Check row
    for i in range(9):
        if sodoku_board[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(9):
        if sodoku_board[i][position[1]] == number and position[0] != i:
            return False

    # Check box
    box_X = position[1] // 3
    box_Y = position[0] // 3

    for i in range(box_Y * 3, box_Y*3 + 3):
        for j in range(box_X * 3, box_X * 3 + 3):
            if sodoku_board[i][j] == number and (i, j) != position:
                return False

    return True

def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def get_empty_square(sodoku_board):
    for i in range(9):
        for j in range(9):
            if sodoku_board[i][j] == 0:
                return (i, j) # row, column

    return None

print_board(board)
print(" ")
print("Solved:")
solve_sodoku(board)
print_board(board)