def solution(a):
    sa=[x for x in a if x!=-1]
    sa=sorted(sa)
    idx=0
    for i in range(len(a)):
        if a[i]!=-1:
            
            a[i]=sa[idx]
            idx+=1
    return a
