def solution(inputString):
    ns=''
    bo=[]
    idx=0

    ns=inputString
    
    for i in range(len(inputString)):
        if inputString[i]=='(':
            bo.append(i)
        elif inputString[i]==')':
            ss=ns[bo[-1]:i+1]
            ns=ns[:bo[-1]]+ss[::-1]+ns[i+1:]
            bo=bo[:-1]
    res=""
    for n in ns:
        print(n)
        if n!="(" and n!=")":
            res=res+n
    return res
            
