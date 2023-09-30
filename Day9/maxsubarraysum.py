# import sys
def max_subarr(arr,n):
    maxi=0
    start=0
    end=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum=sum+arr[k]

            maxi=max(maxi,sum)
            # start=i
            # end=j
        
    return maxi,start,end

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n=len(arr)
# print(n)
print(max_subarr(arr,n))
# maxi = -sys.maxsize - 1  # maximum sum
# print(maxi)





# def maxsub_array(arr):
#     n=len(arr)
#     max_current=max_global=arr[0]

#     for i in range(1,n):
#         # a=0
#         # for j in range(i+1,n):
#         # a=arr[i]+arr[j]
#         max_current=max(arr[i],max_current+arr[i])

#         if max_current>max_global:
#             max_current=max_global
        
#     return max_global
# arr=[-2,1,1,-2,3,4,2,2,-4,-6]
# result=maxsub_array(arr)
# print(result)
# # def maxsubarraysum(arr):
# #     n=len(arr)
# #     for i in range(n):
# #         for j in range(i,n):
# #             for k in range(i,j+1):
# #                 sum+=arr[k]
# #             maxi=max(maxi)


        

