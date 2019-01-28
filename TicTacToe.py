import random

bo = [' ' for x in range(10)]

def isBoardEmpty():
    return (bo[1]==' ' or bo[2]==' ' or bo[3]==' ' or bo[4]==' ' or
             bo[5]==' ' or bo[6]==' ' or bo[7]==' ' or bo[8]==' ' or
              bo[9]==' ')

def playerMove():
    while True:
        x=int(input('Enter your move: '))
        if isValidMove(x):
            bo[x]='X'
            break
        else:
            print('Wrong Move')

def isValidMove(x):
    return (bo[x]==' ')

def isWin(c):
    return ((bo[1]==c and bo[2]==c and bo[3]==c) or
        (bo[4]==c and bo[5]==c and bo[6]==c) or
        (bo[7]==c and bo[8]==c and bo[9]==c) or
        (bo[1]==c and bo[4]==c and bo[7]==c) or
        (bo[2]==c and bo[5]==c and bo[8]==c) or
        (bo[3]==c and bo[6]==c and bo[9]==c) or
        (bo[1]==c and bo[5]==c and bo[9]==c) or
        (bo[3]==c and bo[5]==c and bo[7]==c))

def compMove():
    print('Its computer\'s turn')
    while True:
        y=random.randint(1, 9)
        if isValidMove(y):
            bo[y]='O'
            break
    
def printBoard():
    print(bo[1]+' | '+bo[2]+' | '+bo[3])
    print('-----------')
    print(bo[4]+' | '+bo[5]+' | '+bo[6])
    print('-----------')
    print(bo[7]+' | '+bo[8]+' | '+bo[9])


while True:
        print('Welcome to Tic Tac Toe!')
        a=int(input('If you choose first move type \'1\' else choose \'2\': '))
        while a==1:
            if isBoardEmpty():
                playerMove()
                printBoard()
            else:
                print('Its a Tie game!')
                break
            if isWin('X'):
                print('You Won the game!')
                break
            if isBoardEmpty():
                compMove()
                printBoard()
            else:
                print('Its a Tie game!')
                break
            if isWin('O'):
                print('Computer Won the game!')
                break
        while a==2:
            
            if isBoardEmpty():
                compMove()
                printBoard()
            else:
                print('Its a Tie game!')
                break
            if isWin('O'):
                print('Computer Won the game!')
                break
            if isBoardEmpty():
                playerMove()
                printBoard()
            else:
                print('Its a Tie game!')
                break
            if isWin('X'):
                print('You Won the game!')
                break
        break
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            