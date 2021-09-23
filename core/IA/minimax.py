import sys
from heuristiqueLine import getScore

SIZE = 19 

def minimax (depth, maxPlayer, colorPlayer, board):
    # if game_over() or depth = 0: #creer game_over()
    if depth == 0:
        return None
    if maxPlayer == True:
        bestScore = -sys.maxsize
        scoreBoard = getScore(board, colorPlayer)
        for line in range(SIZE): # Ici on pourrait utiliser Numpy pour transformer le tableau a une dimension
            for column in range(SIZE):
                tboard = list(board)
                tboard[line][column] = colorPlayer[0]
                score = minimax (depth - 1, False, 'white' if colorPlayer == 'black' else 'black', tboard)
                # annuler le coup; on utilise plus tboard
                if scoreBoard[line][column] > bestScore:
                    bestScore = scoreBoard[line][column]
                    bestHit = [line, column]
    else:
        bestScore = sys.maxsize
        scoreBoard = getScore(board, colorPlayer)
        for line in range(SIZE): # Ici on pourrait utiliser Numpy pour transformer le tableau a une dimension
            for column in range(SIZE):
                tboard = list(board)
                tboard[line][column] = colorPlayer[0]
                score = minimax (depth - 1, True, 'white' if colorPlayer == 'black' else 'black', tboard)
                # annuler le coup; on utilise plus tboard
                if scoreBoard[line][column] < bestScore:
                    bestScore = scoreBoard[line][column]
                    bestHit = [line, column]
    return bestHit, bestScore