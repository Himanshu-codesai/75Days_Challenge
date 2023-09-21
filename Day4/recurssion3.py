#sum of first n numbers
sum=0
def func(n):
    global sum
    if n>0:  
        sum=sum+n
        func(n-1)
n=int(input())
func(n)
print(sum)