# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:55:12 2020

@author: Debanjan
"""

import random

bo = [' ' for x in range(10)]
adepth=0

def isBoardEmpty(li1=bo):
    return (li1[1]==' ' or li1[2]==' ' or li1[3]==' ' or li1[4]==' ' or
             li1[5]==' ' or li1[6]==' ' or li1[7]==' ' or li1[8]==' ' or
              li1[9]==' ')

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

def isWin(c,li1 = bo):
    return ((li1[1]==c and li1[2]==c and li1[3]==c) or
        (li1[4]==c and li1[5]==c and li1[6]==c) or
        (li1[7]==c and li1[8]==c and li1[9]==c) or
        (li1[1]==c and li1[4]==c and li1[7]==c) or
        (li1[2]==c and li1[5]==c and li1[8]==c) or
        (li1[3]==c and li1[6]==c and li1[9]==c) or
        (li1[1]==c and li1[5]==c and li1[9]==c) or
        (li1[3]==c and li1[5]==c and li1[7]==c))

def compMove():
    print('Its computer\'s turn')
    bestMove = []
    bestVal=-1000
    global bo
    li1 = bo
    for i in range(1,10):
        if li1[i]==' ':
            li1[i]='O'
            moveVal = minimax(li1,0,False)
            '''
            if moveVal>0:
                moveVal = moveVal-adepth
            elif moveVal<0:
                moveVal = moveVal+adepth
            '''
            li1[i]=' '
            if moveVal>bestVal:
                bestVal=moveVal
                bestMove=[]
                bestMove.append(i)
                print(bestMove,bestVal)
            elif moveVal==bestVal:
                bestMove.append(i)
                print(bestMove,bestVal)
            
    rand_idx = random.randrange(len(bestMove)) 
    finalMove = bestMove[rand_idx]
    print(bestMove,bestVal)
    bo[finalMove]='O'
    
    
def printBoard():
    print(bo[1]+' | '+bo[2]+' | '+bo[3])
    print('-----------')
    print(bo[4]+' | '+bo[5]+' | '+bo[6])
    print('-----------')
    print(bo[7]+' | '+bo[8]+' | '+bo[9])


   

def minimax(li1,depth,ismax):
    global adepth
    if isWin('O',li1):
        #adepth=depth
        return (10-depth)
    elif isWin('X',li1):
        #adepth=depth
        return (-10+depth)
    elif isBoardEmpty(li1):
        if ismax:
            bestVal= -1000
            for i in range(1,10):
                if li1[i]==' ':
                    li1[i]='O'
                    score=0
                    score=minimax(li1,depth+1,False)
                    li1[i]=' '
                    bestVal=max(bestVal,score)
            return bestVal
        else:
            bestVal= +1000
            for i in range(1,10):
                if li1[i]==' ':
                    li1[i]='X'
                    score=0
                    score=minimax(li1,depth+1,True)
                    li1[i]=' '
                    bestVal=min(bestVal,score)
            return bestVal
    else:
        return 0



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
    

    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

