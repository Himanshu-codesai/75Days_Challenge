def array_sorted(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                return False
    return True

arr=[1,22,3,4,5]
n=len(arr)
print(array_sorted(arr,n))








# def a(n):
#     if n==2:
#         return False
#     return True

# n=3
# print(a(n))