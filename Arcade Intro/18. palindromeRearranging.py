def solution(inputString):
    d={}
    if len(inputString)==1:
        return True
    oddchar=-1
    even=1
    if len(inputString)%2==0:
        even=0
    for i in inputString:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for k in d.keys():
        if d[k]%2==1:
            if even==0 or oddchar==1:
                return False
            else:
                oddchar=1 
    return True

