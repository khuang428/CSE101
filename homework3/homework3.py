# Karen Huang
# KARHUANG
# 111644515
# CSE 101
# Homework #3

# In this part of the file it is very important that you write code inside
# the functions only. If you write code in between the functions, then the
# grading system will not be able to read your code or grade your work!

# Part I
def find_starman(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '*':
                return [i+1, j+1]
    return [-1, -1]


# Part II
def move_up(board):
    location = find_starman(board)
    target = [location[0] - 1, location[1]]
    if location == [-1, -1] or target[0] == 0 or board[target[0] - 1][target[1] - 1] == 'W':
        return [-1, -1]
    if board[target[0] - 1][target[1] - 1] == 'F':
        board[target[0] - 1][target[1] - 1] = '*'
        board[location[0] - 1][location[1] - 1] = '.'
    elif board[target[0] - 1][target[1] - 1] == 'O':
        board[target[0] - 1][target[1] - 1] = 'X'
        board[location[0] - 1][location[1] - 1] = '.'
    else:
        board[target[0] - 1][target[1] - 1] = '*'
        board[location[0] - 1][location[1] - 1] = '.'
    return target

# Part III
def move_down(board):
    location = find_starman(board)
    target = [location[0] + 1, location[1]]
    if location == [-1, -1] or target[0] == 6 or board[target[0] - 1][target[1] - 1] == 'W':
        return [-1, -1]
    if board[target[0] - 1][target[1] - 1] == 'F':
        board[target[0] - 1][target[1] - 1] = '*'
        board[location[0] - 1][location[1] - 1] = '.'
    elif board[target[0] - 1][target[1] - 1] == 'O':
        board[target[0] - 1][target[1] - 1] = 'X'
        board[location[0] - 1][location[1] - 1] = '.'
    else:
        board[target[0] - 1][target[1] - 1] = '*'
        board[location[0] - 1][location[1] - 1] = '.'
    return target


# Part IV
def move_left(board):
    location = find_starman(board)
    target = [location[0], location[1] - 1]
    if location == [-1, -1] or target[1] == 0 or board[target[0] - 1][target[1] - 1] == 'W':
        return [-1, -1]
    if board[target[0] - 1][target[1] - 1] == 'F':
        board[target[0] - 1][target[1] - 1] = '*'
        board[location[0] - 1][location[1] - 1] = '.'
    elif board[target[0] - 1][target[1] - 1] == 'O':
        board[target[0] - 1][target[1] - 1] = 'X'
        board[location[0] - 1][location[1] - 1] = '.'
    else:
        board[target[0] - 1][target[1] - 1] = '*'
        board[location[0] - 1][location[1] - 1] = '.'
    return target


# Part V
def move_right(board):
    location = find_starman(board)
    target = [location[0], location[1] + 1]
    if location == [-1, -1] or target[1] == 6 or board[target[0] - 1][target[1] - 1] == 'W':
        return [-1, -1]
    if board[target[0] - 1][target[1] - 1] == 'F':
        board[target[0] - 1][target[1] - 1] = '*'
        board[location[0] - 1][location[1] - 1] = '.'
    elif board[target[0] - 1][target[1] - 1] == 'O':
        board[target[0] - 1][target[1] - 1] = 'X'
        board[location[0] - 1][location[1] - 1] = '.'
    else:
        board[target[0] - 1][target[1] - 1] = '*'
        board[location[0] - 1][location[1] - 1] = '.'
    return target


# Part VI
def move(board, movement):
    if movement == 'U':
        return move_up(board)
    if movement == 'D':
        return move_down(board)
    if movement == 'L':
        return move_left(board)
    if movement == 'R':
        return move_right(board)
    return [-1, -1]



def print_board(board):
    print("The updated game board:")
    row_num = 1
    print("   1  2  3  4  5")
    print("  ----------------")
    for row in board:
        print(str(row_num) + '| ' + '  '.join(row) + ' |')
        row_num += 1
    print("  ----------------" + "\n")


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.
# Upload your homework3.py file to CodeLoad to see how it matches up against other
# test cases!
if __name__ == '__main__':
    # Testing Part I
    board1 = [['*', '.', '.', '.', '.'],
              ['.', 'W', '.', '.', 'F'],
              ['.', '.', '.', 'W', '.'],
              ['.', '.', '.', 'W', '.'],
              ['F', '.', 'O', '.', '.']]

    board2 = [['.', 'W', 'W', 'W', 'W'],
              ['F', 'W', '.', '.', 'F'],
              ['.', 'O', '.', 'W', '.'],
              ['.', '.', '*', 'W', '.'],
              ['O', '.', 'O', '.', '.']]

    board3 = [['O', '.', '.', '.', '.'],
              ['.', '*', '.', '.', 'F'],
              ['.', '.', '.', 'O', '.'],
              ['.', '.', '.', 'O', '.'],
              ['F', '.', '.', '.', '.']]
    print("##### Part I ##### ")
    print("Testing find_starman() with board = board1: " + str(find_starman(board1)))
    print("Testing find_starman() with board = board2: " + str(find_starman(board2)))
    print("Testing find_starman() with board = board3: " + str(find_starman(board3)))
    print()

    # Testing Part II
    board1 = [['.', '.', '.', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['.', 'F', '*', 'F', '.'],
              ['.', '.', 'O', '.', 'W'],
              ['.', '.', 'O', '.', '.']]

    board2 = [['.', '*', '.', 'F', '.'],
              ['.', '.', 'W', 'F', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', 'W', '.', 'O', '.'],
              ['.', '.', '.', '.', '.']]

    board3 = [['.', 'O', '.', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', '.', 'F', '.', '.'],
              ['*', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part II ##### ")
    print("Testing move_up() with board = board1: " + str(move_up(board1)))
    print_board(board1)
    print("Testing move_up() with board = board2: " + str(move_up(board2)))
    print_board(board2)
    print("Testing move_up() with board = board3: " + str(move_up(board3)))
    print_board(board3)

    # Testing Part III
    board1 = [['.', '.', '.', '.', 'W'],
              ['.', '*', '.', '.', '.'],
              ['.', 'F', 'O', 'F', '.'],
              ['.', '.', 'O', '.', 'W'],
              ['.', '.', 'O', '.', '.']]

    board2 = [['.', '.', '.', 'F', '.'],
              ['.', '.', 'W', 'F', '.'],
              ['.', '*', 'F', '.', '.'],
              ['W', 'W', '.', 'O', '.'],
              ['.', '.', '.', '.', '.']]

    board3 = [['.', 'O', '.', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', '*', 'F', '.', '.'],
              ['W', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part III ##### ")
    print("Testing move_down() with board = board1: " + str(move_down(board1)))
    print_board(board1)
    print("Testing move_down() with board = board2: " + str(move_down(board2)))
    print_board(board2)
    print("Testing move_down() with board = board3: " + str(move_down(board3)))
    print_board(board3)

    # Testing Part IV
    board1 = [['.', '.', '.', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['.', 'F', 'O', 'F', '.'],
              ['.', '.', 'O', '.', 'W'],
              ['*', '.', 'O', '.', '.']]

    board2 = [['.', 'F', '.', 'F', '.'],
              ['.', '.', 'O', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', 'W', '.', 'O', '*'],
              ['.', '.', '.', '.', '.']]

    board3 = [['.', 'O', '.', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', '*', 'F', '.', '.'],
              ['W', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part IV ##### ")
    print("Testing move_left() with board = board1: " + str(move_left(board1)))
    print_board(board1)
    print("Testing move_left() with board = board2: " + str(move_left(board2)))
    print_board(board2)
    print("Testing move_left() with board = board3: " + str(move_left(board3)))
    print_board(board3)

    # Testing Part V
    board1 = [['F', 'F', 'F', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['.', 'F', 'O', 'F', '.'],
              ['.', '*', '.', '.', '.'],
              ['.', 'O', 'O', '.', '.']]

    board2 = [['F', 'W', 'F', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['.', '*', 'O', 'F', '.'],
              ['W', '.', '.', '.', '.'],
              ['.', 'W', 'O', '.', '.']]

    board3 = [['.', 'O', '.', '.', '.'],
              ['.', '.', 'F', '.', '.'],
              ['W', '*', 'F', '.', '.'],
              ['W', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part IV ##### ")
    print("Testing move_right() with board = board1: " + str(move_right(board1)))
    print_board(board1)
    print("Testing move_right() with board = board2: " + str(move_right(board2)))
    print_board(board2)
    print("Testing move_right() with board = board3: " + str(move_right(board3)))
    print_board(board3)

    # Testing Part VI
    board1 = [['.', 'W', 'W', '.', 'W'],
              ['F', 'F', '.', '.', 'F'],
              ['.', 'O', '.', 'W', '*'],
              ['.', '.', '.', 'W', '.'],
              ['O', '.', 'O', '.', '.']]

    board2 = [['.', 'F', '.', 'F', '.'],
              ['.', '.', 'O', '.', '.'],
              ['.', '.', 'O', '*', '.'],
              ['W', 'W', '.', 'O', '.'],
              ['.', '.', '.', 'W', '.']]

    board3 = [['F', 'W', 'F', '.', 'W'],
              ['.', '.', '.', '.', '.'],
              ['W', '*', 'O', 'F', '.'],
              ['W', '.', '.', '.', '.'],
              ['.', 'W', 'O', '.', '.']]

    board4 = [['.', 'O', '.', '.', '.'],
              ['.', 'F', 'F', '.', '.'],
              ['W', '*', 'F', 'F', '.'],
              ['F', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', 'F']]
    print("##### Part VI ##### ")
    print("Testing move() with board = board1, movement = 'U': " + str(move(board1, 'U')))
    print_board(board1)
    print("Testing move() with board = board2, movement = 'D': " + str(move(board2, 'D')))
    print_board(board2)
    print("Testing move() with board = board3, movement = 'L': " + str(move(board3, 'L')))
    print_board(board3)
    print("Testing move() with board = board4, movement = 'R': " + str(move(board4, 'R')))
    print_board(board4)