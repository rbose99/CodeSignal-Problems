def solution(inputArray):
    maxlen=0
    n=len(inputArray)
    for i in range(n):
        if len(inputArray[i])>maxlen:
            maxlen=len(inputArray[i])
    res=[]
    for i in range(n):
        if len(inputArray[i])==maxlen:
            res.append(inputArray[i])
    return res
            