def solution(matrix):
    m=len(matrix)
    n=len(matrix[0])

    res=[[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==True:
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if 0<=x<=m-1 and 0<=y<=n-1 and not(x==i and y==j):
                            res[x][y]+=1
                       
    return res