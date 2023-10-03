def count_subarray_sumeq_k(arr,k):
    n=len(arr)
    count=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum=sum+arr[j]
            if sum==k:
                count+=1
    return count
arr=[1,2,3]
k=5
print(count_subarray_sumeq_k(arr,k))


            

