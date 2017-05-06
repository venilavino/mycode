correct = [[1,3,2],
           [2,1,3],
           [3,2,1]]

incorrect = [[1,2,4,3],
             [2,3,1,3],
             [3,1,2,3],
             [4,2,2,4]]


def check_sudoku(game):
    n = len(game)
    if n < 1:
        return False
    for i in range(0, n):
        horizontal = []
        vertical = []
        for k in range(0, n):
            #vertical check
            if game[k][i] in vertical:
                return False
            vertical.append(game[k][i])

            if game[i][k] in horizontal:
                return False
            horizontal.append(game[i][k])
    return True

print check_sudoku(correct)
print check_sudoku(incorrect)
