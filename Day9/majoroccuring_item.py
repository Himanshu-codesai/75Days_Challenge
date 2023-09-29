def majoroccuring(arr):
    n=len(arr)

    for i in range(n):
        count=0
        for j in range(n):
            if arr[j]==arr[i]:
                count+=1
        if count>(n//2):
            return arr[i]
        

arr = [1, 1, 1, 2, 2]
ans = majoroccuring(arr)
print("The majority element is:", ans)        