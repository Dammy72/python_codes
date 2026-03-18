
def endgame(defboard,a,b):
    if max(defboard[:6]) <= 0 or max(defboard[6:12]) <= 0 or (any(a==1 and b==1 for a,b in zip(a,b)) and sum(a)==1 and sum(b)==1):
        return False
    else:
        return True
'''  
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
'''

def move(n, defboard, depth):
    plays = []
    while endgame(board,board[:6],board[6:12]) == True:
        n = 1-n
        a = 0
        preX = None
        while True:
            if n == 0:
                defx = int(input(f'Player {n+1}, choose a position ({6*n} to {6*n+5})'))
                print(f'you chose position {defx}')
                preX = defx
                
            else: 
                if plays == []:
                    tree = search(None,defboard,1,depth)
                    print_tree(tree)
                    a = 0
                    plays, best = max_diff(tree,n=1)
                    print(plays)
                    defx = plays[a]
                    print(f'the computer chose position {defx}')
                else:
                    if preX != plays[a+1]:
                        tree = search(None,defboard,1,depth)
                        a = 0
                        plays, best = max_diff(tree,n=1)
                        defx = plays[a]
                        print(f'the computer chose position {defx}')
                    else:
                        a += 2
                        defx = play[a]
            if defx in range(6*n,6*(n+1)) and defboard[defx] > 0:
                defboard = move0(defx,defboard,n)
                A = defboard[:6] + [defboard[12]]
                B = defboard[6:12] + [defboard[13]]
                #print('A = ',A)
                #print('B = ',B)
                #print(list(enumerate(defboard)))
                display_board(defboard)
                break
            else:
                print(f'wrong or empty position,Player {n+1}, choose a position {6*n} to {6*n+5}')

import time

def search(hole,defboard,n,depth):
    childtree = []
    if depth == 0:
        return [hole,defboard,[]]
    for defx in range(6*n, (6*n)+6):
        if defboard[defx]==0:
            continue
        parent = defboard[:]
        child = move0(defx,parent,n)
        n = 1-n
        # depth -= 1
        childbranch = search(defx,child,n,depth - 1)
        childtree.append(childbranch)
    return [hole,defboard,childtree]

def max_diff(tree,n):
    defx, board , children = tree
    best = -float('inf')
    plays = []
    if children == []:
        diff = board[12+n] - board[12+(1-n)]
        return [], diff
    for child in children:
        play, childboard, baby = child
        xs,difference = max_diff(child,n)
        if difference > best:
            best = difference
            plays = [play] + xs
    return plays , best 
   
        
def move0(defx,defboard,n):
    hand = defboard[defx]
    defboard[defx] = 0
    while hand > 0:
        defx = (defx+1)%12
        defboard[defx] += 1
        hand -= 1
    A = defboard[:6] + [defboard[12]]
    B = defboard[6:12] + [defboard[13]]
    #print(f"last hole is {defx}")
    while defboard[defx] in range(2,4) and defx not in range(6*n,6*(n+1)):
        defboard[12+n] += defboard[defx]
        defboard[defx] = 0
        defx -= 1
    #print('A = ',A)
    #print('B = ',B)
    #print(list(enumerate(defboard)))
    return defboard

def print_tree(node, depth=0):
    defx,board, children = node
    indent = "  " * depth
    
    #print(f"{indent}Depth {depth}: {defx}{board}")

    for child in children:
        print_tree(child, depth + 1)

def display_board(defboard):
    for hole in range(11,5,-1):
        print(defboard[hole], end=" ")
    print(" ",defboard[13])
    for hole in range(0,6):
        print(defboard[hole], end=" ")
    print(" ",defboard[12])
    print()
#######################################################################



import random
board = [4] * 12  + [0,0]
print
depth = 4
start = time.perf_counter()
board = move(1, board,4)
end = time.perf_counter()

print(f"Time taken: {end - start:.6f} seconds")


'''
A = board[:6] + [board[12]]
B = board[6:12] + [board[13]]
while endgame(board,board[:6],board[6:12]) == True:
    #player 1
    n = 0
    board = move(n, board)
    #player 2
    n = 1
    board = move(n, board)
if board[12] > board[13]:
    winner = 'hum_player'
elif board[13] > board[12]:
    winner = 'comp_player'
elif board[12] == board[13]:
    winner = 'both players'
print('GAME_OVER')
print(f'winner is {winner}')
'''


