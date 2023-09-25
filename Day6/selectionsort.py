def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr=[1,9,3,2,8,7,3,5,6,1,2]

print(selection_sort(arr))
# print(arr)

