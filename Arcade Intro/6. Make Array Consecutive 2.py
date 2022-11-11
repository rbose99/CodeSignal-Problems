def solution(statues):
    a=set(statues)
    maxi=max(a)
    mini=min(a)
    tot=0
    for i in range(mini+1,maxi):
        if i not in a:
            tot+=1
    return tot