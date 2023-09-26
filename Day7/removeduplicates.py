def removeduplicates(nums):
    newarr=[]

    for num in nums:
        if num not in newarr:
            newarr.append(num)
    return newarr

a = [1,1,1,2,3,4,5,5,5]
print(removeduplicates(a))