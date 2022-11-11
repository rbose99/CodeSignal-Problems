def solution(inputArray):
    moves=0
    val=inputArray[0]
    for i in range(1,len(inputArray)):
        if inputArray[i]<=val:
            moves+=val-inputArray[i]+1
            inputArray[i]=inputArray[i]+1
            val=val+1
        else:
            val=inputArray[i]
    return moves