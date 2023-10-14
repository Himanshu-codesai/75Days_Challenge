def binarysearch(arr,target):
    n=len(arr)
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            low=mid+1
        else:
            high = mid-1
    return -1

arr=[3,4,5,6,7,8,9]
target=2
print(binarysearch(arr,target))