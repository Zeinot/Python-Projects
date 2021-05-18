def find_next_empty(puzzle):
    # Finds the next row, col on the puzzle that's not filled yet  => Replace with -1
    # Return row, col tuple (or (None, None) if ther is none)

    # Don't forget that we are zero-indexing and the last index is 8
    for r in range(9):
        for c in range(9):  # range(9) is 0 to 8
            if puzzle[r][c] == -1:
                return r, c

        return None, None  # if no spaces are empty (-1)


def is_valid(puzzle, guess, row, col):
    # Figure out whether the guess at the row/col of the puzzle is a valid guess
    # Returns True if is valid, False otherwise

    # Lets start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Now the colums
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
        col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # And then the square
    # we want to get where 3x3 suare starts
    # and iterate over the 3 values in the row/colum
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, row_start + 3):
            if puzzle[r][c] == guess:
                return False

    # If we get here, these checks pass
    return True


def solve_sudoku(puzzle):
    # Solvee sudoku using backtracking
    # the puzzle is a list of lists , and every inner list is a row in the sudoku
    # return whetther a solution existes
    # mutates puzzle to be the solution if solution doen't existe
    # Step 1: choose somewhere to start making guesses on the puzzle
    row, col = find_next_empty(puzzle)
    # Step 1.1 if there's noewhere left, then we are dont because we only allowed valid inputs
    if row is None:
        return True
    # Step 2 if ther is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # Step 3 checking if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3.1if this is the valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # step 4: recursively call our fonction
            if solve_sudoku(puzzle):
                return True

        # Step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        # Backtrack and try a new nbr
        puzzle[row][col] = -1  # reset the guess
        # Step 6 : if none of the numbers that we try work, means the puzzle is unsolvable
    return False


# You can change this board by putting -1 on the empty places , and numbers on the full ones
if __name__ == '__main__':
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)

print("press any key to exit")
input()
# Made by Omar Sarsar @Zeinot on github // Zeinotgaming@gmail.com
