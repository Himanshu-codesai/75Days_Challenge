def findfloor(arr,x):
    low=0
    n=len(arr)
    high=n-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]<=x:
            ans=arr[mid]
            low=mid+1

        else:
            high=mid-1
    return ans

def findceil(arr,x):
    low=0
    n=len(arr)
    high=n-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]>=x:
            ans=arr[mid]
            high=mid-1

        else:
            low=mid+1
    return ans

def findboth(arr,x):
    f=findfloor(arr,x)
    c=findceil(arr,x)
    return (f,c)

arr=[3,4,4,5,6,9]
x=7
print(findboth(arr,x))