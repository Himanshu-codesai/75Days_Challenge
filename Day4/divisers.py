a=[]
def divisors(n):
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)

    return a
n=int(input())
print(divisors(n))
    