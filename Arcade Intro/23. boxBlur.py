def solution(image):
    m=len(image)
    n=len(image[0])
    res=[]
    for i in range(m-2):
        temp=[]
        
        for j in range(n-2):
            tot=0
            for x in range(i,i+3):
                for y in range(j,j+3):
                    tot+=image[x][y]
            temp.append(tot//9)
        res.append(temp)
    return res