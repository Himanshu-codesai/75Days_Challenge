
def movezero_to_end(arr,n):
    temp=[]

    for i in range(n):
        if arr[i] !=0:
            temp.append(arr[i])

    n2=len(temp)

    for j in range(n2,n):
        temp.append(0)

    return temp

arr=[0,2,1,4,5,0,0,6,0]
arr=sorted(arr)
n = len(arr)
print(movezero_to_end(arr,n))
