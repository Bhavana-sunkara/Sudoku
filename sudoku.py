def isValid(board):
    for i in range(9):
        row = {}
        col = {}
        block = {}
        rowCube = 3*(i//3)
        colCube = 3*(i%3)
        for j in range(9):
            if board[i][j]!="." and board [i][j] in row:
                return False
            row[board[i][j]] = 1
            if board[j][i]!="." and board [j][i] in col:
                return False
            col[board[j][i]] = 1
            rc = rowCube + j//3
            cc = colCube + j%3
            if board[rc][cc]!="." and board [rc][cc] in block:
                return False
            block[board[rc][cc]] = 1
    return True


