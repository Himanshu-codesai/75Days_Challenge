def fibonacci(n):
    if n==1:
        # print(n)
        return 0
    elif n==2:
        return 1
    else:   
        return fibonacci(n-1)+fibonacci(n-2)
        # print(fibonacci(n-1)+fibonacci(n-2))
n=int(input())
for i in range(1,n+1):
    print(fibonacci(i))

# print(fibonacci(n))
# fibonacci(n)
# for i in range(n):
    # fibonacci(i)