def maxsubarr(arr):
    n=len(arr)
    maxi=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum=sum+arr[j]
            maxi=max(maxi,sum)
    return maxi
arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsubarr(arr))


