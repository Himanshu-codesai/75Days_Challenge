# # [1,2,3,4] --> [24,12,8,6]
def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    print(n)
    print(output)

    # Calculate the product of all elements to the left of each element
    left_product = 1
    for i in range(n):
        output[i]=output[i]*left_product
        # output[i] *= left_product
        left_product=left_product*nums[i]
        # left_product *= nums[i]
        # print(left_product)

    # Calculate the product of all elements to the right of each element
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output

# Test the function with your input
input_array = [1, 2, 3, 4]
output_array = product_except_self(input_array)
print(output_array)  # Output should be [24, 12, 8, 6]

# n=5
# for i in range(n-1,-1,-1):
#     print("yes")
#     print(i)
#     # right_product=1
# for i in range(4):
#     print(i)
# print(input_array[2]) 