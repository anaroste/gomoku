import sys
from .heuristiqueLine import getScore

SIZE = 19 
display = True 
def minimax (depth, maxPlayer, board):
    # if game_over() or depth = 0: #creer game_over()
    bestHit = [-1, -1]
    bestScore = 0
    if depth != 0:
        if maxPlayer == True:
            bestScore = -sys.maxsize -1
            scoreBoard = getScore(board, 'black' if maxPlayer else 'white')
            for line in range(SIZE): # Ici on pourrait utiliser Numpy pour transformer le tableau a une dimension
                for column in range(SIZE):
                    tboard = list(board)
                    tboard[line][column] = 'b' if maxPlayer else 'w' [0]
                    bestHit, bestScore = minimax (depth - 1, False, tboard)
                    # annuler le coup; on utilise plus tboard
                    if scoreBoard[line][column] > bestScore:
                        bestScore = scoreBoard[line][column]
                        bestHit = [line, column]
        else:
            bestScore = sys.maxsize
            scoreBoard = getScore(board, 'black' if maxPlayer else 'white')
            for line in range(SIZE): # Ici on pourrait utiliser Numpy pour transformer le tableau a une dimension
                for column in range(SIZE):
                    tboard = list(board)
                        
                    tboard[line][column] = 'b' if maxPlayer else 'w'[0]
                    bestHit, bestScore = minimax (depth - 1, True, tboard)
                    # annuler le coup; on utilise plus tboard
                    if scoreBoard[line][column] < bestScore:
                        bestScore = scoreBoard[line][column]
                        bestHit = [line, column]
    return bestHit, bestScore