def rearrby_sign(arr):
    n=len(arr)
    positive=[]
    negative=[]
    for i in range(n):
        if arr[i]>0:
            positive.append(arr[i])
        else:
            negative.append(arr[i])
        
    for i in range(len(positive)):
        arr[2*i]=positive[i]
    for i in range(len(negative)):
        arr[2*i+1]=negative[i]
    return arr

arr=[1,2,-4,-5]
print(rearrby_sign(arr))