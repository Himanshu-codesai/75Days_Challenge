def search(arr,n):
    no = len(arr)
    for i in range(no):
        if arr[i]==n:
            print("index - ",i)
arr = [2,3,4,5,7,8,9]
n=int(input())
search(arr,n)
