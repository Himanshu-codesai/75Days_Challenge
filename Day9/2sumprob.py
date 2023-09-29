def sum_prob(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            # print(j)
            if arr[i]+arr[j]==target:
                print(i,j)

arr=[3,5,6,8,9]
target=11
sum_prob(arr,target)


