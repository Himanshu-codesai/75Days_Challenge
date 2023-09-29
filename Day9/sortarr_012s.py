def sortarr_012s(arr):
    a0=0
    b1=0
    c2=0
    for num in arr:
        if num==0:
            a0+=1
        elif num==1:
            b1+=1
        elif num==2:
            c2+=1
        
    for i in range(a0):
        arr[i]=0
    
    for i in range(a0,a0+b1):
        arr[i]=1

    for i in range(a0+b1,len(arr)):
        arr[i]=2

    return arr

arr=[2,0,2,1,1,0]
print(sortarr_012s(arr))


# def sortarr_012s(arr):
#     return sorted(arr)

# arr=[2,0,2,1,1,0]
# print(sortarr_012s(arr))