def leader_in_array_rightmost(arr):
    n=len(arr)
    ans=[]

    for i in range(n):
        leader=True
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                leader=False
                break
        if leader:
            ans.append(arr[i])
    return ans


# def leader_in_array_rightmost(arr):
#     n=len(arr)
#     a=[]
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i]>arr[j]:
#                 a.append(arr[i])
#     return a

arr = [4, 7, 1, 0]
print(leader_in_array_rightmost(arr))

                