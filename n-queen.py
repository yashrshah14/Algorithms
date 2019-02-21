def printBoard(board):
    for i in range(4):
        for j in range(4):
            print board[i][j],
        print("")


def solveBoard(board,col):
    if solveNQueen(board,0)==False:
        print("Solution does not exist")
        return False
    printBoard(board)
    return True

def solveNQueen(board,col):
    if col>=4:
        return True
    for row in range(4):
        if isSafe(board,row,col):
            board[row][col]=1
            if solveNQueen(board,col+1)==True:
                return True
            board[row][col]=0
    return False

def isSafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,4,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True

def main():
    board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    solveBoard(board,0)


main()
