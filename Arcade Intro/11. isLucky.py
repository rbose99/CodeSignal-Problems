def solution(n):
    n=str(n)
    split=len(n)//2
    s1=0
    s2=0
    n1=n[:split]
    n2=n[split:]
    s1= sum(int(x) for x in n1)
    s2= sum(int(x) for x in n2)
    return s1==s2
