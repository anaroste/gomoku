import sys
from .heuristiqueLine import getScore

SIZE = 19 
display = True 
# def minimax (depth, maxPlayer, board):
#     # if game_over() or depth = 0: #creer game_over()
#     bestHit = [-1, -1]
#     bestScore = 0
#     if depth != 0:
#         if maxPlayer == True:
#             bestScore = -sys.maxsize -1
#             scoreBoard = getScore(board, 'black' if maxPlayer else 'white')
#             for line in range(SIZE): # Ici on pourrait utiliser Numpy pour transformer le tableau a une dimension
#                 for column in range(SIZE):
#                     tboard = list(board)
#                     tboard[line][column] = 'b' if maxPlayer else 'w' [0]
#                     bestHit, bestScore = minimax (depth - 1, False, tboard)
#                     # annuler le coup; on utilise plus tboard
#                     if scoreBoard[line][column] > bestScore:
#                         bestScore = scoreBoard[line][column]
#                         bestHit = [line, column]
#         else:
#             bestScore = sys.maxsize
#             scoreBoard = getScore(board, 'black' if maxPlayer else 'white')
#             for line in range(SIZE): # Ici on pourrait utiliser Numpy pour transformer le tableau a une dimension
#                 for column in range(SIZE):
#                     tboard = list(board)
                        
#                     tboard[line][column] = 'b' if maxPlayer else 'w'[0]
#                     bestHit, bestScore = minimax (depth - 1, True, tboard)
#                     # annuler le coup; on utilise plus tboard
#                     if scoreBoard[line][column] < bestScore:
#                         bestScore = scoreBoard[line][column]
#                         bestHit = [line, column]
#     return bestHit, bestScore

#retourn un boleen, true si la partie est fini
def game_over():
    pass

def max(maxScore, score):
    if maxScore > score:
        return maxScore
    return score

def min(minScore, score):
    if minScore < score:
        return minScore
    return score

def minimax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or game_over():
        return position
    if maximizingPlayer:
        maxScore =  sys.maxsize * -1
        for child in position:
            score = minimax(child, depth - 1, alpha, beta, False)
            maxScore = max(maxScore, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
            return maxScore
    else:
        minScore =  sys.maxsize
        for child in position:
            score = minimax(child, depth - 1, alpha, beta, True)
            minScore = min(minScore, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
            return minScore

            # https://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=1491&context=creativecomponents
