def minsort(arr):
    n=len(arr)
    mini=arr[0]
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            mini=min(arr[i+1],mini)
        elif arr[i]<arr[i+1]:
            mini=min(arr[i],mini)
    return mini

arr=[4,5,6,7,0,1,2,3]
print(minsort(arr))