
from ArrayHandler import ArrayHandler
import os

#user input for board radius
n = 0
while (n < 4):
    n = input('Enter the radius of the board you are trying to complete: ')
    if (n.isdigit()):
        n = int(n)    
        if (n<4):
            print("Number needs to be greater than 3.\n")
            n = 0
    else:
        n = 0
        print("Please enter in an integer.\n")

    
Generation = 0
listChildren = []
listChildren = ArrayHandler.initChildren(listChildren, n, n*75)
Found = False
#when solution is found it will output it
while(Found == False):
    print("Generation " + str(Generation))
    for board in listChildren:
        if (board[n] == 0):
            print("SOLUTION FOUND IN " + str(Generation) + " GENERATIONS.\n")
            for i in range(0,n):
                print("[" + str(board[i][0]) + "," + str(board[i][1]) + "] ")
            Found = True
            break 
    if Found == False:
        listChildren = ArrayHandler.nextGeneration(listChildren,n)
        Generation += 1
    if Generation == 100:
        listChildren = []
        listChildren = ArrayHandler.initChildren(listChildren, n, n*75)
        Generation = 0
