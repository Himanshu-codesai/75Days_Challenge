def union_of_array(arr1,arr2):
    arr=arr1+arr2
    arr = sorted(arr)
    n=len(arr)
    newarr=[]
    set1=set(arr1)
    print(set1)
    for i in arr:
        if i not in newarr:
            newarr.append(i)
    return newarr
    # for i in range(n):
    #     if arr[i] is in 
    # print(arr)

arr1=[2,4,5,5,7,8,9]
arr2=[0,0,1,8,8]
print(union_of_array(arr1,arr2))
