#handles everything to do with an array
#from Calculate import Calculate
import random
class ArrayHandler(object):
    #creates a board with n children
    def board(n):
            b = []
            for count in range(0,n):
                b.append(ArrayHandler.generateRChild(n))
            b.append(ArrayHandler.fitness(b,n))
            return b
    #creates random child
    def generateRChild(n):
        x = random.randrange(1,n+1)
        y = random.randrange(1,n+1)
        child = [x,y]      
        return child

    #creates board states
    def initChildren(list, n, child):
        for count in range(0,child):
            list.append(ArrayHandler.board(n))
        return list
    #fitness function to determine a solution or not
    def fitness(b,n):
        cntAttack = 0
        for i in range(0,n):
            if (i != n):
                for j in range(i+1,n):
                    if b[i][0] == b[j][0]:
                        cntAttack+=1
                    if b[i][1] == b[j][1]:
                        cntAttack+=1
                    if abs(b[i][0]-b[j][0]) == abs(b[i][1] - b[j][1]):
                        cntAttack+=1
       

        return int(cntAttack)

                
    #function that chooses where the split should be for cross breeding
    def chooseSplit(n):
        x = random.randrange(0,n-1)
        return x
    #random chance of mutation
    def mutationCheck():
        randomNumber = random.randrange(1,100,1)
        if randomNumber == 1:
            return True
        else:
            return False
    #makes amount of children based on number using best and second best from previous generation
    def reproduce(n,best,secondBest):
        
        lstChildren = []
        for count in range(0,n*75):
            board = []
            split = ArrayHandler.chooseSplit(n)
            for count in range(0,split+1):
                if ArrayHandler.mutationCheck():
                    board.append(ArrayHandler.generateRChild(n))
                else:
                    board.append(best[count])
            for count in range(split+1,n):
                if ArrayHandler.mutationCheck():
                    board.append(ArrayHandler.generateRChild(n))
                else:
                    board.append(secondBest[count])
            board.append(ArrayHandler.fitness(board,n))
            lstChildren.append(board)
        lstChildren.append(best)
        lstChildren.append(secondBest)
        return lstChildren

    #gives next generation
    def nextGeneration(lst,n):
        best = []
        secondBest = []
        worst = []
        average = 0
        for count in range(0,n+1):
            best.append(99999999)
            secondBest.append(99999999)
            worst.append(0)
        for item in lst:
            average += item[n]
            if item[n] < best[n]:
                best = item
            else:
                if item[n] < secondBest[n]:
                    secondBest = item
                else:
                    if item[n] > worst[n]:
                        worst = item

        print("best: " + str(best[n]) + " worst: " + str(worst[n]) + " average: %.2f" % (average/(n*75)))
        return ArrayHandler.reproduce(n,best,secondBest)
