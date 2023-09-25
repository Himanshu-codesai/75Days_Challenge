def bubble_array_sort(arr):
    n=len(arr)
    # 4-0-1=

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[43,4,5,6,77,22]
bubble_array_sort(arr)
print(arr)
