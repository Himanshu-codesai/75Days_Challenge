def markcolumn(matrix,n,m,j):
    for i in range(n):
        if matrix[i][j] !=0:
            matrix[i][j]=-1

def markrow(matrix,n,m,i):
    for j in range(m):
        if matrix[i][j] !=0:
            matrix[i][j]=-1

def zeromatrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                markcolumn(matrix,n,m,j)
                markrow(matrix,n,m,i)
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    return matrix



matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1],[1,1,0]]
n= len(matrix) #no of rows
m=len(matrix[0]) #no of column
print(matrix)
ans = zeromatrix(matrix, n, m)
for i in range(n):
    print(ans[i])
# print(ans)
# for i in range(n):
#     for j in range(m):
#         print(matrix[j])