def lowerband(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]>=x:
            return i
    return n

arr=[3,5,6,15,18]
x=18
print(lowerband(arr,x))