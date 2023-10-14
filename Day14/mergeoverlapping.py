

# def mergeoverlapping(arr):
#     n=len(arr)
#     # ans=[]
#     # print(arr[2][1])
#     # for i in range(n):
#     #     start,end=arr[i][0],arr[i][1]
        
#     #     for j in range(i+1,n):
#     #         if end>=arr[j][0]:
#     #             end=arr[j][1]
#     #     ans.append([start,end])
#     # return ans
#     ans = [arr[0]]

#     for i in range(1, n):
#         current_start, current_end = arr[i]

#         # Checking for overlap with the last interval in 'ans'
#         last_start, last_end = ans[-1]

#         if current_start <= last_end:
#             # Merge the overlapping intervals
#             ans[-1] = [last_start, max(last_end, current_end)]
#         else:
#             # No overlap, add the current interval to the result
#             ans.append([current_start, current_end])

#     return ans


# arr=[[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18]]
# # print(sorted(arr))
# arr=sorted(arr)
# print(arr)
# # print(arr[1][1])
# print(mergeoverlapping(arr))
# print(5**2)
# mylist=[2,3,4,5]
# # mylist.remove(2)
# # mylist.clear()
# mylist.extend([3])
# print(mylist)

# a=['s','a','w','d']
# print('e'.join(a))
# my_dict={
#     'a':'aa','b':'bb',1:2
# }
# print(my_dict)
# del my_dict['b']
# print(my_dict)
# my_dict['a']='a'
# print(my_dict)
# # my_dict.pop(0)
# # my_dict.clear()
# otherdict=my_dict.copy()
# print(otherdict)
# Traditional loop
squares = []
# for x in range(10):
#     squares.append(x**2)

# Using list comprehension
squares = [x**2 for x in range(10)]
print(squares)