# output = input().split()
output = input()
output = [int(num) for num in output]
print(output)
def uniqueopfromip(numbers):
    uniquenumber=set()
    for num in numbers:
        if numbers.count(num)==1:
            uniquenumber.add(num)
    return list(uniquenumber)

print(uniqueopfromip(output))

# input_numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# num= [3,5,2,3,5]
# for nums in num:
#     print(num.count(nums))
# print(num.count(5))