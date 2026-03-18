def run(AB):
    while max(AB) > 3:
        #player 1
        while True:
            x = int(input('Player 1, choose a position (0 to 5) '))
            if x in range(0,6):
                hand = AB[x]
                AB[x] = 0
                while hand > 0:
                    x = (x+1)%12
                    AB[x] = AB[x] + 1
                    hand = hand - 1
                A = AB[:6]
                print('A = ',A)
                print(AB)
                break
            else:
                print('wrong position,Player 1, choose a position (0 to 5)')
            

        #player 2
        while True:
            x = int(input('Player 2, choose a position (6 to 11) '))
            if x in range(6,12):
                hand = AB[x]
                AB[x] = 0
                while hand > 0:
                    x = (x+1)%12
                    AB[x] = AB[x] + 1
                    hand = hand - 1
                B = AB[6:]
                print('B = ',B)
                print(AB)
                break
            else:
                 print('wrong position,Player 2, choose a position (6 to 11)')
############################################################################

AB = [4] * 12
run(AB)
'''
AB = [4] * 12
while max(AB) > 3:
    #player 1
    while True:
        x = int(input('Player 1, choose a position (0 to 5) '))
        if x in range(0,6):
            hand = AB[x]
            AB[x] = 0
            while hand > 0:
                x = (x+1)%12
                AB[x] = AB[x] + 1
                hand = hand - 1
            A = AB[:6]
            print('A = ',A)
            print(AB)
            break
        else:
            print('wrong position,Player 1, choose a position (0 to 5)')
        

    #player 2
    while True:
        x = int(input('Player 2, choose a position (6 to 11) '))
        if x in range(6,12):
            hand = AB[x]
            AB[x] = 0
            while hand > 0:
                x = (x+1)%12
                AB[x] = AB[x] + 1
                hand = hand - 1
            B = AB[6:]
            print('B = ',B)
            print(AB)
            break
        else:
             print('wrong position,Player 2, choose a position (6 to 11)')
            
'''
