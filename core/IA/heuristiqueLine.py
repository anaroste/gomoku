import numpy as np

EMPTY = 'x'
SIZE = 19
dictionaryDir = dict()
dictionaryDir['topR'] = [-1, 1]
dictionaryDir['top'] = [-1, 0]
dictionaryDir['topL'] = [-1, -1]
dictionaryDir['right'] = [0, 1]
dictionaryDir['left'] = [0, -1]
dictionaryDir['botR'] = [1, 1]
dictionaryDir['bot'] = [1, 0]
dictionaryDir['botL'] = [1, -1]

board = []


def combo(line, colone, sens, player, point = 0) :
    line += sens[0]
    colone += sens[1]
    if not(0 <= line < SIZE and 0 <= colone < SIZE) :
        return point, 0, 0
    
    if (board[line][colone] == player) :
        return combo(line, colone, sens, player, point + 1)

    return point, 0, 0


def heuristiqueLine(player, scoreBoard) :
    # print(combo(1, 1, [-1,-1]))

    # for sens in dictionaryDir :
    #     print(board[1][1])
    #     print(combo(1, 1, [dictionaryDir[sens]]))
    for line in range(SIZE) :
        for colone in range(SIZE) :
            if ( board[line][colone] == 'x') :
                for sens in dictionaryDir :
                    point, l, c = combo(line, colone, dictionaryDir[sens], player)
                    scoreBoard[line][colone] += point
    # for line in range(len(scoreBoard)) :
    #     print(str(line) +'\t'+ str(scoreBoard[line]))

def getScore(localBoard, player, lastMove = None) :
    global board
    board = localBoard
    scoreBoardBlack = np.zeros((19, 19))
    scoreBoardWite = np.zeros((19, 19))
    
    heuristiqueLine('b', scoreBoardBlack)

    heuristiqueLine('w', scoreBoardWite)

    if (player == 'b'):
        scorePlayer = np.subtract(scoreBoardBlack, scoreBoardWite)
    else :
        scorePlayer = np.subtract(scoreBoardWite, scoreBoardBlack)
    return scorePlayer

    
def callGetScore() :
    localBoard =    [   ['b', 'b', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['b', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'w', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'w', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'b', 'w', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'b', 'b', 'x', 'b', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['b', 'b', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'b', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'w', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], \
                    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    player = 'black'

    score = getScore(localBoard, player[0])

callGetScore()