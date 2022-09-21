def coord_to_index(x, y):
    '''Takes user coordinate and converts to index in array'''
    # Coordinate to index formula : row + column * width
    return ((x - 1) + (y - 1) * 3)


def win_check(player, game_grid):
    '''Checks if a player has won by row, column or diagonal'''
    # Check for row win
    if player == game_grid[0] == game_grid[1] == game_grid[2]:
        return True
    if player == game_grid[3] == game_grid[4] == game_grid[5]:
        return True
    if player == game_grid[6] == game_grid[7] == game_grid[8]:
        return True
    # Check for column win
    if player == game_grid[0] == game_grid[3] == game_grid[6]:
        return True
    if player == game_grid[1] == game_grid[4] == game_grid[7]:
        return True
    if player == game_grid[2] == game_grid[5] == game_grid[8]:
        return True
    # Check for diagonal win
    if player == game_grid[0] == game_grid[4] == game_grid[8]:
        return True
    if player == game_grid[2] == game_grid[4] == game_grid[6]:
        return True

    return False


def get_symbol(i):
    '''Returns symbol based on what number is in the game grid'''
    symbols = ["X", "O", "-"]
    return symbols[i]


def draw_board(grid):
    '''Draws a the game board'''
    for column in range(0, 4):
        for row in range(0, 4):
            if row == 0 and column == 0:
                print('', end="  ")
            elif column == 0 and row == 1:
                print("1", end=" ")
            elif column == 0 and row == 2:
                print("2", end=" ")
            elif column == 0 and row == 3:
                print("3", end=" ")
            elif column == 1 and row == 0:
                print("1", end=" ")
            elif column == 2 and row == 0:
                print("2", end=" ")
            elif column == 3 and row == 0:
                print("3", end=" ")
            else:
                # Draws the appropriate symbol based on the game grid
                symbol_index = grid[coord_to_index(row, column)]
                print(get_symbol(symbol_index), end=" ")
        print()


def check_available(x, y, game_grid):
    '''Check if the given (x, y) position is available'''
    g_index = coord_to_index(x, y)
    if game_grid[g_index] != 2:
        return False
    return True


def player_move(player, game_grid):
    '''Takes an int input that is either 1, 2 or 3'''
    symbol = get_symbol(player)
    while True:
        try:
            x1 = int(input(f"Player {symbol}, which row do you play? "))
            y1 = int(input(f"Player {symbol}, wich column do you play? "))
            if 0 < x1 < 4 and 0 < y1 < 4:
                if check_available(x1, y1, game_grid):
                    return x1, y1
                else:
                    print("Position is taken please try again")
            else:
                print("Please input 1, 2 or 3")
        except ValueError:
            print("Please input a valid number")


def main():
    game_grid = [
        2, 2, 2,
        2, 2, 2,
        2, 2, 2
    ]
    current_player = 0
    run_game = True

    # Use max(game_grid) to check if board is full
    # If board is full and win_check does not return True, announce a draw
    while run_game:
        draw_board(game_grid)

        if max(game_grid) != 2:
            run_game = False
            print("It's a draw!")
        else:
            # Updates the game board with the players move
            row, column = player_move(current_player, game_grid)
            g_index = coord_to_index(row, column)

            # Check if the move was a winning move
            game_grid[g_index] = current_player
            if win_check(current_player, game_grid):
                run_game = False
                draw_board(game_grid)
                print(f"Player {get_symbol(current_player)} has won!")

            # Switch players
            current_player = (current_player + 1) % 2


if __name__ == "__main__":
    main()
