a = int(input())
b = int(input())
ans=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        ans=i
print(ans)
print(4%20)
print(4//20)
print(4/20)
