def solution(sequence):
    n=len(sequence)
    removed=0
    if n==1:
        return True
    i=0
    while i <n-1:
        if sequence[i]>=sequence[i+1]:
            if removed==1:
                return False
            if i==n-2:
                return True
            elif (i>0 and sequence[i-1]<sequence[i+1]) or i==0:
                removed+=1
                i=i+1
            elif sequence[i]<sequence[i+2]:
                removed+=1 
                i=i+2
            
            else: 
                return False
        else:
            i=i+1
    return True
        
        

