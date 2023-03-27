def backwardStep(numOfSteps):

    cnt = 1
    while(cnt <= numOfSteps):

        numOfSpaces = numOfSteps * (6 - cnt)
        spaceCnt = 1

        while(spaceCnt <= numOfSpaces): 
            print(" ", end="")
            spaceCnt+=1

        print(cnt)
        cnt+=1

backwardStep(numOfSteps=5)


