def solution(inputString):
    left=0
    right=len(inputString)-1
    while left<right:
        if inputString[left]!=inputString[right]:
            return False
        left=left+1
        right=right-1
    return True

