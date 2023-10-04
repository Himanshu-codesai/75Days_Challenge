def majorityele_n3(arr):
    n=len(arr)
    for i in range(n):
        count=0
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                count+=1
        if count>=n//3:
            print(arr[i])

arr=[11,22,22,11,11]
majorityele_n3(arr)
