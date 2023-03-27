def forwardStep(numOfSteps):

    cnt = 1 
    while(cnt <= numOfSteps):

        numOfSpace = cnt * 5
        spaceCnt = 1

        while(spaceCnt <= numOfSpace):
            print(" ", end="")
            spaceCnt+=1

        print(cnt)
        cnt+=1

forwardStep(numOfSteps=5)
