def binarysearch_Re(arr,low,high,target):
    
    mid=(low+high)//2

    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binarysearch_Re(arr,mid+1,high,target)
    else:
        return binarysearch_Re(arr,low,mid-1,target)

    

arr=[2,3,4,5,6,7,8]
low=0
n=len(arr)
high=n-1
target=2
print(binarysearch_Re(arr,low,high,target))