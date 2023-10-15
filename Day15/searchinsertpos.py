def inserts(arr,x):
    n=len(arr)
    low=0
    high=n-1
    ans=n

    while low<=high:
        mid =(low+high)//2

        if arr[mid]>=x:
            ans=mid
            high =mid-1
        else:
            low=mid+1
    return ans

arr=[1,2,4,6,7]
a=inserts(arr,5)
arr.insert(a,5)
print(arr)
# print(inserts(arr,5))