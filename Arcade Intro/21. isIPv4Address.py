def solution(inputString):
    s=inputString.split(".")
    if len(s)!=4:
        return False
    for i in range(4):
        if len(s[i])==0:
            return False
        if len(s[i]) > 1 and s[i][0] == '0':
            return False
        if not s[i].isdigit() or not 0<=int(s[i])<=255:
            return False
    
    return True


 

