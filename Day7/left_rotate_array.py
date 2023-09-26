def left_rotate_array(arr):
    if len(arr)<=1:
        return arr
    first_element = arr[0]

    for i in range(len(arr)-1):
        arr[i]=arr[i+1]

    arr[-1]=first_element

arr=[1,2,3,4,5]
left_rotate_array(arr)
print(arr)