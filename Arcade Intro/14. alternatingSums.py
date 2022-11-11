def solution(a):
    b=[0,0]
    for i in range(len(a)):
        if i%2==1:
            b[1]+=a[i]
        else:
            b[0]+=a[i]
    return b