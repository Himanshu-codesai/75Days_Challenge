def reversepairs(arr):
    n=len(arr)
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>2*arr[j]:
                cnt+=1
    return cnt
arr =[40,25,19,12,9,6,2]
print(reversepairs(arr))