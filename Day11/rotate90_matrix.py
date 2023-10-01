
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=len(matrix)
for i in range(n):
    print(matrix[i])
for i in range(n):
    for j in range(n):
        # matrix[i][j]=matrix[j][(n-1)-i]
        matrix[i][j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j]


print("\n")
for i in range(n):
    print(matrix[i])