def coord_to_index(x, y):
    '''Takes user coordinate and converts to index in array'''
    # Coordinate to index formula : row + column * width
    return ((x - 1) + (y - 1) * 3)


def index_to_coord(i):
    '''Returns x, y coordinates based on index'''
    # Index to coordinate formula: x = index % width
    # alternatively if you have y, x = index - (width * y)
    # y = index / width
    x = (i % 3) + 1
    y = (i // 3) + 1
    return (x, y)


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
    symbols = ["-", "X", "O"]
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


def user_input(player, position):
    symbol = get_symbol(player)
    while True:
        try:
            p = int(input(f"Player {symbol}, which {position} do you play? "))
            if 0 < p < 4:
                return p
            else:
                print("Please input 1, 2 or 3")
        except ValueError:
            print("Please input a valid number")


def main():
    game_grid = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]
    # Storing player moves as tuples
    # player_one = []
    # player_two = []
    current_player = 1
    run_game = True
    # Use min(game_grid) to check if board is full
    # If board is full and win_check does not return True, announce a draw
    while run_game:
        draw_board(game_grid)

        if min(game_grid) != 0:
            run_game = False
            win_check(current_player, game_grid)

        row = user_input(current_player, "row")
        column = user_input(current_player, "column")

        debug_temp = input("Do you want to continue? y/n")
        if debug_temp == "n":
            run_game = False


if __name__ == "__main__":
    main()
