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
            break
        else:
            print(f'wrong or empty position,Player {n+1}, choose a position {6*n} to {6*n+5}')

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






########################################################################
'''
def move(n, defboard):
    while True:
        x = int(input(f'Player {n+1}, choose a position ({6*n} to {6*n+5})'))
        if x in range(6*n,6*(n+1)) and defboard[x] > 0:
            hand = defboard[x]
            defboard[x] = 0
            while hand > 0:
                x = (x+1)%12
                defboard[x] += 1
                hand -= 1
            A = defboard[:6] + [defboard[12]]
            B = defboard[6:12] + [defboard[13]]
            print(f"last hole is {x}")
            while defboard[x] in range(2,4) and x not in range(6*n,6*(n+1)):
                defboard[12+n] += defboard[x]
                defboard[x] = 0
                x -= 1
            print('A = ',A)
            print('B = ',B)
            print(list(enumerate(defboard)))
            return defboard
            break
        else:
            print(f'wrong or empty position,Player {n+1}, choose a position {6*n} to {6*n+5}')


def endgame(defboard,n,a,b):
    if max(defboard[6*n:6*(n+1)]) <= 0 and any(a==1 and b==1 for a,b in zip(a,b)):
        return false
    else:
        return true
        
def end_game(defboard):
    
    if max(defboard[:6]) = 0 and max(defboard[6:12]) > 0 and

def endgame(defboard,n):
    if max(defboard[6*n:6*(n+1)]) <= 0 and any(a==1 and b==1 for a,b in zip(a,b)):
        return false
    else:
        return true
        
    


def gain(gainA, defx, defboard):
    if defx in range(6*n,6*(n+1)):
        gainA += 0
        return gainA
    else:
        while defboard[defx] in range(2,4):
            gainA += defboard[defx]
            defx += 1
            print(gainA)
        return gainA
'''
