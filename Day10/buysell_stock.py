def buysell_stock(arr):
    n=len(arr)
    maxpro=0
    buy_index = sell_index = 0
    for i in range(n):
        for j in range(i+1,n):
                
            # if arr[j]>arr[i]:
            #     maxpro=max(maxpro,arr[j]-arr[i])
                if arr[j] - arr[i] > maxpro:
                    maxpro=max(maxpro,arr[j]-arr[i])
                    buy_index=i
                    sell_index=j


    return maxpro,buy_index,sell_index
arr=[7,1,5,3,6,4]
print(buysell_stock(arr))
# arr=[7,1,5,3,6,4]
