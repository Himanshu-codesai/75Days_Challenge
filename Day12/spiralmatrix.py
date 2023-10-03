def matrix_spiral(matrix):
    n=len(matrix) #rows
    m=len(matrix[0]) #columns

    #left to right
    for i in range(m):
        for j in range(n):
            if i==0:
                print(matrix[i][j])
    #top to bottom
    for i in range(m):
        for j in range(n-1):
            if i==2:
                print(matrix[j+1][i])
    # right to left
    for i in range(m):
        for j in range(1,-1,-1):
            if i==2:
                print(matrix[i][j])
                
    for i in range(m):
        for j in range(2):
            if i==1:
                print(matrix[i][j])


        


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_spiral(matrix)
# print(matrix[2][0])
# for i in range(1,-1,-1):
#     print(i)