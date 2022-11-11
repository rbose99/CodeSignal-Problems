def solution(matrix):
    cost=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i==0 or matrix[i-1][j]!=0:
                cost+=matrix[i][j]
            else:
                matrix[i][j]=0
    return cost

