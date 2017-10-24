from homework3 import *


def game_driver():
    original = [['*', 'O', '.', '.', '.'],
                ['.', '.', 'F', '.', '.'],
                ['W', '.', 'F', '.', '.'],
                ['F', 'O', 'W', '.', '.'],
                ['.', '.', '.', '.', '.']]
    board = [['*', 'O', '.', '.', '.'],
             ['.', '.', 'F', '.', '.'],
             ['W', '.', 'F', '.', '.'],
             ['F', 'O', 'W', '.', '.'],
             ['.', '.', '.', '.', '.']]

    game_over = False
    game_won = False
    quit_game = False
    while not game_over and not game_won and not quit_game:
        print_board(board)
        valid_input = False
        next_move = None
        while not valid_input:
            next_move = input('Please enter your next move, your options:\n'
                              'U/u : Go upwards one slot\n'
                              'D/d : Go downwards one slot\n'
                              'L/l : Go leftwards one slot\n'
                              'R/r : Go rightwards one slot\n'
                              'Q/q : Quit the game\n'
                              'Your choice: ')

            if next_move.upper() in ['U', 'D', 'L', 'R', 'Q']:
                valid_input = True
                if next_move.upper() == 'Q':
                    quit_game = True
                    print("Play again!")
                    break
            else:
                print('Invalid next move symbol, please input either U/u, D/d, L/l R/r or Q/q.\n')

        if not quit_game:
            result = move(board, next_move.upper())
            if result is None:
                print("Move function incomplete.")
            elif result == [-1, -1]:
                print("You can't go there!")
            elif original[result[0] - 1][result[1] - 1] == 'O':
                print("You have fallen into a pit, game over!")
                game_over = True
                print_board(board)
            else:
                print("You made a successful move!")
                # check if there are any more food left
                if not has_food(board):
                    game_won = True
                    print("You have won the game!")
                    print_board(board)
            print()


def has_food(board):
    for row in board:
        if 'F' in row:
            return True
    return False


def print_board(board):
    print("Your current game board:")
    row_num = 1
    print("   1  2  3  4  5")
    print("  ----------------")
    for row in board:
        print(str(row_num) + '| ' + '  '.join(row) + ' |')
        row_num += 1
    print("  ----------------" + "\n")


# this following line starts the driver
if __name__ == '__main__':
    game_driver()
