# a = input()
# print(len(a))

def countit(n):
    count=0
    x=n
    while x!=0:
        x//=10
        count+=1
    return count
# n=234656
n=int(input())
print(countit(n))