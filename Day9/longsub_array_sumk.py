def longest_subarray_sumk(arr,kk):
    n=len(arr)
    length=0
    # s=0
    for i in range(n):
        s=0
        for j in range(i,n):
                s+=arr[j] 

                if s==kk:
                     length=max(length,j-i+1)
    return length
    # for i in range(n):
    #     for j in range(i,n):
    #             s=0
    #             for k in range(i,j+1):
    #              s+=arr[k]

    #              if s==kk:
    #                  length=max(length,j-i+1)
    # return length

arr=[2,2,3,1,5,1,1,2,9]
kk=4
print(longest_subarray_sumk(arr,kk))
                 
                 

