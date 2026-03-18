'''
def search(defboard, defn):
    for defx in range(6*n,6*n+6):
        cdefboard = defboard[:]
        cdefx = defx
        hand = cdefboard[cdefx]
        cdefboard[cdefx] = 0
        cgain = 0
        while hand > 0:
            cdefx = (cdefx+1)%12
            cdefboard[cdefx] += 1
            hand -= 1
'''     

def endgame(defboard,a,b):
    if max(defboard[:6]) <= 0 or max(defboard[6:12]) <= 0 or (any(a==1 and b==1 for a,b in zip(a,b)) and sum(a)==1 and sum(b)==1):
        return False
    else:
        return True
def comp_move(defboard):
    gain = 0
    realx = random.randint(6,11)
    while defboard[realx] == 0:
        realx = random.randint(6,11)
    for defx in range(6,12):
        cdefboard = defboard[:]
        cdefx = defx
        hand = cdefboard[cdefx]
        cdefboard[cdefx] = 0
        cgain = 0
        while hand > 0:
            cdefx = (cdefx+1)%12
            cdefboard[cdefx] += 1
            hand -= 1
        B = cdefboard[6:12] + [cdefboard[13]]
        while cdefboard[cdefx] in range(2,4) and cdefx not in range(6,12):
            cgain += cdefboard[cdefx]
            cdefboard[cdefx] = 0
            cdefx -= 1
        if cgain > gain and cdefboard[defx] !=0:
            gain = cgain
            realx = defx
        else:
            pass
    return realx
        

def move(n, defboard):
    while True:
        if n == 0:
            defx = int(input(f'Player {n+1}, choose a position ({6*n} to {6*n+5})'))
            print(f'you chose position {defx}')
        else:
            defx = comp_move(board)
            print(f'the computer chose position {defx}')
        if defx in range(6*n,6*(n+1)) and defboard[defx] > 0:
            defboard = move0(defx,defboard)
            break
        else:
            print(f'wrong or empty position,Player {n+1}, choose a position {6*n} to {6*n+5}')

def move0(defx,defboard):
    hand = defboard[defx]
    defboard[defx] = 0
    while hand > 0:
        defx = (defx+1)%12
        defboard[defx] += 1
        hand -= 1
    A = defboard[:6] + [defboard[12]]
    B = defboard[6:12] + [defboard[13]]
    print(f"last hole is {defx}")
    while defboard[defx] in range(2,4) and defx not in range(6*n,6*(n+1)):
        defboard[12+n] += defboard[defx]
        defboard[defx] = 0
        defx -= 1
    print('A = ',A)
    print('B = ',B)
    print(list(enumerate(defboard)))
    return defboard
#######################################################################
import random
board = [4] * 12  + [0,0]
A = board[:6] + [board[12]]
B = board[6:12] + [board[13]]
while endgame(board,board[:6],board[6:12]) == True:
    #player 1
    n = 0
    board = move(n, board)
    #player 2
    n = 1
    board = move(n, board)





