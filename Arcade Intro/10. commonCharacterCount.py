def solution(s1, s2):
    d1={}
    d2={}
    for i in range(len(s1)):
        if s1[i] in d1.keys():
            d1[s1[i]]+=1
        else:
            d1[s1[i]]=1
    for i in range(len(s2)):
        if s2[i] in d2.keys():
            d2[s2[i]]+=1
        else:
            d2[s2[i]]=1
    tot=0
    for k in d1.keys():
        if k in d2.keys():
            tot+=min(d1[k],d2[k])
    return tot
    

