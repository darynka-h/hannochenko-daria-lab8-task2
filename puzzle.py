def validate_board(board: list) -> bool:
    """
    (list) -> bool
    The function checks if game board ready to game.
    If the board ready it returns True, otherwise returns False
    >>> validate_board(["**** ****", "***1 1****", "**  3****", \
"* 4 7****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 5****", "**  3****", \
"* 4 7****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    colors_dict = {'yellow': board[-1][:5] + board[4][0] + board[5][0] + board[6][0] + board[7][0],
                   'green': board[-2][1:6] + board[3][1] + board[4][1] + board[5][1] + board[6][1],
                   'light_green': board[-3][2:7] + board[2][2] + board[3][2] + board[4][2] + board[5][2],
                   'purple': board[-4][3:8] + board[1][3] + board[2][3] + board[3][3] + board[4][3],
                   'pink': board[-5][4:] + board[0][4] + board[1][4] + board[2][4] + board[3][4],}
    for value in colors_dict.values():
        for element in value:
            if element.isdigit() and value.count(element) > 1:
                return False