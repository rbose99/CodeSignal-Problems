def solution(picture):
    lenn=len(picture[0])
    border= '*' * (lenn+2)
    res=[]
    res.append(border)
    for i in range(len(picture)):
        res.append('*'+picture[i]+'*')
    res.append(border)
    return res