def solution(inputArray):
    maxdiff=0
    for i in range(len(inputArray)-1):
        diff=inputArray[i]-inputArray[i+1]
        if diff<0:
            diff=-1*diff   
        if diff>maxdiff:
            maxdiff=diff
    return maxdiff
        

