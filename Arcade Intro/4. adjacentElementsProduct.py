def solution(inputArray):
    n=len(inputArray)
    maxprod=inputArray[0]*inputArray[1]
    for i in range(1,n-1):
        prod=inputArray[i]*inputArray[i+1]
        if maxprod<prod:
            maxprod=prod
    return maxprod

