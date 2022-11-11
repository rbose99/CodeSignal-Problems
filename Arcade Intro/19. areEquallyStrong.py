def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return min(yourLeft,yourRight)==min(friendsLeft,friendsRight) and max(yourLeft,yourRight)==max(friendsLeft,friendsRight)

