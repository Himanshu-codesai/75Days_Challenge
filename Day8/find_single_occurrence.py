def find_single_occu(arr):
    dicts={}

    for i in arr:
        if i in dicts:
            dicts[i]+=1
        else:
            dicts[i]=1
    # print(dicts)

    for a,b in dicts.items():
        if b==1:
            return a

arr=[2,3,4,5,5,5,6,1,2]
print(find_single_occu(arr))



# def find_single_occurrence(arr):
#     result = 0

#     for num in arr:
#         result ^= num

#     return result

# # Example usage:
# arr = [1,1,2,3]
# result = find_single_occurrence(arr)
# print(result)  # Output: 4 (the element occurring only once)
