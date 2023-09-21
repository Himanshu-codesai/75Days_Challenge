def func(n):
    if n>0:
        # print(n) Starts from n to 1
        func(n-1)
        print(n) #start from 1 to n

N = int(input())
func(N)