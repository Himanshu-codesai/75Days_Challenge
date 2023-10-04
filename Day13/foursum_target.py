def foursum_totarget(arr,target):
    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]+arr[j]+arr[k]+arr[l]==target:
                        print(arr[i],arr[j],arr[k],arr[l])

arr=[1,0,-1,0,-2,2]
target=0
foursum_totarget(arr,target)
