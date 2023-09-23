def ntimes(n):
    if n>0:
        # print(n)
        ntimes(n-1)
        print(n)


n=int(input())
ntimes(n)