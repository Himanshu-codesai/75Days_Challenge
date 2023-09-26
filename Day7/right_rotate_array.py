def right_rotate_array(arr):
    if len(arr)<=1:
        return arr
    last_element = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]

    arr[0]=last_element
arr=[1,2,3,4,5]
print(arr)
right_rotate_array(arr)
print(arr)
    
# for i in range(5,0,-1):
#     print(i)    
# [1,2,3,4,5]-->[5,1,2,3,4] right






# [1,2,3,4,5]--> [2,3,4,5,1] left